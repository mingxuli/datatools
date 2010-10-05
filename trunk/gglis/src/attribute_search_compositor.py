# To change this template, choose Tools | Templates
# and open the template in the editor.
from attribute_load_compositor import AttributeLoadCompositor

class AttributeSearchCompositor(AttributeLoadCompositor):
    def __init__(self,layerName,filter):
        AttributeLoadCompositor.__init__(self,layerName)
        self.column = filter[0]
        self.value = filter[1]
        self.compare = filter[2]

    def getDatas(self, cur, columns):
        names = ",".join(columns)
        cur.execute("select %s from %s where %s %s '%s' order by id" % (names, self.name, self.column, self.compare, self.value))
        return cur.fetchall()
