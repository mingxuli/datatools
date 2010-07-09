# To change this template, choose Tools | Templates
# and open the template in the editor.
from attribute_load_compositor import AttributeLoadCompositor
class AttributePointCompositor(AttributeLoadCompositor):
    def __init__(self,layerName,point):
        AttributeLoadCompositor.__init__(self,layerName)
        self.x = point[0]
        self.y = point[1]

    def getDatas(self,cur,columns):
        names = ','.join(columns)
        cur.execute("select %s from %s where MbrWithin(MakePoint(%f, %f,4326),Geometry)" % (names, self.name, self.x, self.y))
        return cur.fetchone()

