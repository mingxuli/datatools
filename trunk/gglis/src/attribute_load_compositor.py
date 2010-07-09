# To change this template, choose Tools | Templates
# and open the template in the editor.
class AttributeLoadCompositor:
    def __init__(self,layerName):
        self.name = layerName

    def getColumns(self,cur):
        cur.execute("PRAGMA table_info(%s)" % (self.name))
        columns = cur.fetchall()
        return [column[1] for column in columns if column[1] != 'Geometry']

    def getDatas(self,cur,columns):
        names = ",".join(columns)
        cur.execute("select %s from %s order by gid" % (names, self.name))
        return cur.fetchall()