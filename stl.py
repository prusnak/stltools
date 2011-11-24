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

  def loadFromFile(filename):
    pass

  # inspired by http://stackoverflow.com/questions/2083771/a-method-to-calculate-the-centre-of-mass-from-a-stl-stereo-lithography-file
  def computeVolume():

    totalVolume = 0.0
    xCenter = 0.0
    yCenter = 0.0
    zCenter = 0.0

    for f in facets:
      currentVolume = (f.v1x*f.v2y*f.v3z - f.v1x*f.v3y*f.v2z - f.v2x*f.v1y*f.v3z + f.v2x*f.v3y*f.v1z + f.v3x*f.v1y*f.v2z - f.v3x*f.v2y*f.v1z) / 6
      totalVolume += currentVolume
      xCenter += ((f.v1x + f.v2x + f.v3x) / 4) * currentVolume
      yCenter += ((f.v1y + f.v2y + f.v3y) / 4) * currentVolume
      zCenter += ((f.v1z + f.v2z + f.v3z) / 4) * currentVolume
