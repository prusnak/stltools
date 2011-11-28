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
  minx = +1e9
  maxx = -1e9
  miny = +1e9
  maxy = -1e9
  minz = +1e9
  maxz = -1e9

  def load(self, filename):
    facet = None
    state = 0
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
        x = float(l[1])
        y = float(l[2])
        z = float(l[3])
        if x < self.minx: self.minx = x
        if y < self.miny: self.miny = y
        if z < self.minz: self.minz = z
        if x > self.maxx: self.maxx = x
        if y > self.maxy: self.maxy = y
        if z > self.maxz: self.maxz = z
        if state == 0:
          facet.v1x = x
          facet.v1y = y
          facet.v1z = z
        elif state == 1:
          facet.v2x = x
          facet.v2y = y
          facet.v2z = z
        elif state == 2:
          facet.v3x = x
          facet.v3y = y
          facet.v3z = z
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
