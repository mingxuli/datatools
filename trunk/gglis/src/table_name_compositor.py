# To change this template, choose Tools | Templates
# and open the template in the editor.
class TableNameCompositor:
    def __init__(self,name):
        self.name=name

    def getColumns(self, cur):
        return ["f_table_name"]

    def getDatas(self, cur, columns):
        names = ",".join(columns)
        cur.execute("select %s from %s " % (names, self.name))
        return cur.fetchall()


