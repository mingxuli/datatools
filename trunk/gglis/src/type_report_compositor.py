from attribute_load_compositor import AttributeLoadCompositor
class TypeReportCompositor(AttributeLoadCompositor):
    def __init__(self,layerName):
        AttributeLoadCompositor.__init__(self,layerName)

    def getColumns(self,cur):
        return ['Main Type','Sub Type','Code','Lake Number','Lake Number(%)','Total Area(quart km)','Total Area(%)','Mean Area(quart km)','Max Area(quart km)','Min Area(quart km)']

    def getDatas(self,cur,columns):        
        cur.execute("select main_type,sub_type,code,lake_number,lake_number_percent,total_area,total_area_percent,mean_area,max_area,min_area from lake_type_statis")
        return cur.fetchall()

