# To change this template, choose Tools | Templates
# and open the template in the editor.
from attribute_point_compositor import AttributePointCompositor

class AttributeGeometryCompositor(AttributePointCompositor):
    def __init__(self,layerName,point):
        AttributePointCompositor.__init__(self,layerName,point)

    def getColumns(self, cur):
        return ['Geometry']

    def getDatas(self, cur, columns):
        cur.execute("select AsText(Geometry) from %s where MbrWithin(MakePoint(%f, %f,4326),Geometry)" % (self.name, self.x, self.y))
        return cur.fetchone()



