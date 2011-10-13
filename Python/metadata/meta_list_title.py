# encoding=utf8
##metadata
import string
from psycopg2 import connect
from xml.dom.minidom import parse, parseString
import win32com
import win32com.client


##---start-----
filepath=u'D://Hiehe_Meta//'
msword=win32com.client.DispatchEx('Word.Application')

conn = connect("host=210.77.68.237 dbname=geonetwork252 user=wlz password=glacier")
curs=conn.cursor()
sql_str="""select b.categoryid,a.uuid,a.data,a.createdate,a.changedate 
    from metadata a full join metadatacateg b on a.id=b.metadataid 
    where a.istemplate='n'
    order by b.categoryid;"""
curs.execute(sql_str)
rows=curs.fetchall()
titles=[]
index=1



for group_id,uuid,meta,createdate,changedate in rows:
    dom=parseString(meta)
    root=dom.documentElement
    #标题
    Title=root.getElementsByTagName('resTitle')[0]
    Title=Title.firstChild.data
    #副标题
    AltTitle=root.getElementsByTagName('resAltTitle')
    for node in AltTitle:
        if node.hasChildNodes():            
            AltTitle=AltTitle[0].firstChild.data
        else:
            AltTitle=u'没有英文标题'
    #关键词
    ##主题关键词为:theme
    ##位置关键词为:place
    ##时间关键词为:temporal
    Keyword_temporal=''
    Keyword_place=''
    Keyword_theme=''
    descKeys=root.getElementsByTagName('descKeys')
    for node in descKeys:
        KeyTypCd=node.getElementsByTagName('KeyTypCd')
        if KeyTypCd.length==1:
            code=KeyTypCd[0].getAttribute('value')
            if code=='temporal':
                keywords=node.getElementsByTagName('keyword')
                if keywords.length>0:
                    for keyword in keywords:
                        for childnode in keyword.childNodes:
                            Keyword_temporal=Keyword_temporal+','+childnode.data        
            if code=='place':
                keywords=node.getElementsByTagName('keyword')
                if keywords.length>0:
                    for keyword in keywords:
                        for childnode in keyword.childNodes:
                            Keyword_place=Keyword_place+','+childnode.data
            if code=='theme':
                keywords=node.getElementsByTagName('keyword')
                if keywords.length>0:
                    for keyword in keywords:
                        for childnode in keyword.childNodes:
                            Keyword_theme=Keyword_theme+','+childnode.data
    ##摘要
    Abstract=root.getElementsByTagName('idAbs')
    for node in Abstract:
        if node.hasChildNodes():
            Abstract=Abstract[0].firstChild.data
##        else:
            Abstract=''
    ##DOI
    citID=root.getElementsByTagName('citId')
    for node in citID:
        if node.hasChildNodes():
            citID=citID[0].firstChild.data
        else:
            citID=''
    citIdType=root.getElementsByTagName('citIdType')
    for node in citIdType:
        if node.hasChildNodes():
            citIdType=citIdType[0].firstChild.data
        else:
            citIdType=''
    ##数据使用声明
    useLimit=root.getElementsByTagName('useLimit')
    for node in useLimit:
        if node.hasChildNodes():
            useLimit=useLimit[0].firstChild.data
        else:
            useLimit=''
    ##项目支持信息
    suppInfo=root.getElementsByTagName('suppInfo')
    for node in suppInfo:
        if node.hasChildNodes():
            suppInfo=suppInfo[0].firstChild.data
        else:
            suppInfo=''
    
    print index,group_id, Title, uuid
#    print u'    英文标题:',AltTitle
##    print u'    创建时间:',createdate,'  最后修改时间:',changedate
##    print u'    关键词:'
##    print u'        主题关键词:',Keyword_theme
##    print u'        地点关键词:',Keyword_place
##    print u'        时间关键词:',Keyword_temporal
##    print u'    摘 要:'
##    ##print Abstract
##    print u'      ',citIdType,':',citID
####    print u'    数据引用方式:'
####    print u'    建议参考文献:'
##    print u'    数据使用声明:',useLimit
#    print u'    项目支持信息:',suppInfo
##    print u'    相关链接:'
##
##    
    index=index+1
    ##存为MS Word格式的文件
##    filename=filepath+uuid+'.doc'
##    print filename
##    newdoc=msword.Documents.Open(FileName=filename)
##    range=newdoc.Range()
##    range.InsertAfter(Title)
##    newdoc.Save()
##msword.Quit()
curs.close()
conn.close()
print 'end'
