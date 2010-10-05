# To change this template, choose Tools | Templates
# and open the template in the editor.
from attribute_point_compositor import AttributePointCompositor

class AttributeGeometryCompositor(AttributePointCompositor):
    def __init__(self,layerName,point):
        AttributePointCompositor.__init__(self,layerName,point)

    def getColumns(self, cur):
        return ['geometry']

    def getDatas(self, cur, columns):
        cur.execute("select AsText(geometry) from %s where MbrWithin(MakePoint(%f, %f,4326),geometry)" % (self.name, self.x, self.y))
        return cur.fetchone()



