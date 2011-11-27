class Facet:

  v1x = 0.0
  v1y = 0.0
  v1z = 0.0
  v2x = 0.0
  v2y = 0.0
  v2z = 0.0
  v3x = 0.0
  v3y = 0.0
  v3z = 0.0
  nx = 0.0
  ny = 0.0
  nz = 0.0


class STL:

  facets = []
  facet = None
  state = 0

  def load(self, filename):
    f = open(filename, 'r')
    for l in f.readlines():
      l = l.strip().split(' ')
      if len(l) == 0:
        continue
      if l[0] == 'facet':
        facet = Facet()
        facet.nx = float(l[2])
        facet.ny = float(l[3])
        facet.nz = float(l[4])
        state = 0
      if l[0] == 'vertex':
        if state == 0:
          facet.v1x = float(l[1])
          facet.v1y = float(l[2])
          facet.v1z = float(l[3])
        elif state == 1:
          facet.v2x = float(l[1])
          facet.v2y = float(l[2])
          facet.v2z = float(l[3])
        elif state == 2:
          facet.v3x = float(l[1])
          facet.v3y = float(l[2])
          facet.v3z = float(l[3])
        state += 1
      if l[0] == 'endfacet' and facet != None:
        self.facets.append(facet)
        facet = None
    f.close()

  # inspired by http://stackoverflow.com/questions/2083771/a-method-to-calculate-the-centre-of-mass-from-a-stl-stereo-lithography-file
  def calcVolume(self):

    self.volume = 0.0
    self.xCenter = 0.0
    self.yCenter = 0.0
    self.zCenter = 0.0

    for f in self.facets:
      currentVolume = (f.v1x*f.v2y*f.v3z - f.v1x*f.v3y*f.v2z - f.v2x*f.v1y*f.v3z + f.v2x*f.v3y*f.v1z + f.v3x*f.v1y*f.v2z - f.v3x*f.v2y*f.v1z) / 6
      self.volume += currentVolume
      self.xCenter += ((f.v1x + f.v2x + f.v3x) / 4) * currentVolume
      self.yCenter += ((f.v1y + f.v2y + f.v3y) / 4) * currentVolume
      self.zCenter += ((f.v1z + f.v2z + f.v3z) / 4) * currentVolume

  def output(self):
    for f in self.facets:
      print 'v1(', f.v1x, ',', f.v1y, ',', f.v1z, ')'
      print 'v2(', f.v2x, ',', f.v2y, ',', f.v2z, ')'
      print 'v3(', f.v3x, ',', f.v3y, ',', f.v3z, ')'
      print ' n(', f.nx, ',', f.ny, ',', f.nz, ')'
      print
