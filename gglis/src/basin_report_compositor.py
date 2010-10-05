# To change this template, choose Tools | Templates
# and open the template in the editor.
from attribute_load_compositor import AttributeLoadCompositor

class BasinReportCompositor(AttributeLoadCompositor):
    def __init__(self,layerName,basin):
        AttributeLoadCompositor.__init__(self,layerName)
        self.basin = basin.toString()

    def getColumns(self,cur):
        return ['Basin Name','Basin Code','Lake Number','Lake Number(%)','Total Area(quart km)','Total Area(%)','Mean Area(quart km)','Max Area(quart km)','Min Area(quart km)']

    def getDatas(self,cur,columns):  
        params = str(self.basin)+'%'
        if self.basin=='all':
            sql = "select basin,code,lake_number,lake_number_percent,total_area,total_area_percent,mean_area,max_area,min_area from lake_basin_statis where type=1"
            cur.execute(sql)
        else:
            sql = "select basin,code,lake_number,lake_number_percent,total_area,total_area_percent,mean_area,max_area,min_area from lake_basin_statis where type=2 and code like ?"
            cur.execute(sql,[params])
        return cur.fetchall()