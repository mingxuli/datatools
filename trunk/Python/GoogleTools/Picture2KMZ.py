#coding=utf8
##Author:Wu Lizong
##Create_Date:2009-7-3
##Description:
##  import picture into google earth and save as KMZ fromate
##  pictures will include in kmz file.so it will so big.
##Version:0.1.0
##History:


import glob,os,string
from xml.dom import minidom
from types import *




def writekml(outpath):
    ##for create new kml file
    impl = minidom.getDOMImplementation()
    new_dom = impl.createDocument(None, 'kml', None)
    new_root = new_dom.documentElement
    print new_root.nodeName



    ##text = unicode('汉字示例', 'cp936')
    ##item = makeEasyTag(dom, 'item', text)
    ##root.appendChild(item)
    ##root.toxml()
    ##f=file('d:/test.xml', 'w')
    ##import codecs
    ##riter = codecs.lookup('utf-8')[3](f)
    ##dom.writexml(writer, encoding='utf-8')
    ##writer.close()
class Picture:
    Copyright=''
    Filename_list=[]
    Title_list=[]        
    Longitude_list=[]
    Latitude_list=[]
    Elevation_list=[]
    Description_list=[]
    def read_metainfo(metafile):
        ##for read picture_info.xml file
        dom=minidom.parse(metafile)
        root=dom.documentElement
        flag=0
        gid=1
        Copyright_Nodelist=root.getElementsByTagName('Copyright')
        if len(Copyright_Nodelist)==0:
            print 'There is no Copyright Tag in the Picture_info file,Are you sure?'            
        else:
            Copyright_Node=Copyright_Nodelist[0].firstChild
            if type(Copyright_Node) is NoneType:            
                print 'There is no Copyright infomation.Are you sure?'                
            else:
                self.Copyright=Copyright_Node.data
            
        Picture_path_Nodelist=root.getElementsByTagName('Picture_path')
        if len(Picture_path_Nodelist)==0:
            print 'There is no Picture_path Tag,Check it!'
        else:
            Picture_path_Node=Picture_path_Nodelist[0].firstChild
            if type(Picture_path_Node) is NoneType:
                print 'You need to set Picture path!'
                flag=1
            else:
                Picture_path=Picture_path_Node.data
                if os.path.isdir(Picture_path) is False:
                    print 'The Picture path is not right,Check it please.'
                    flag=1
                else:
                    if Picture_path[-1]<>'\\':
                        Picture_path=Picture_path+'\\'

        Picture_Nodelist=root.getElementsByTagName('Picture')
        for Picture_Node in Picture_Nodelist:
            Filename_Nodelist=Picture_Node.getElementsByTagName('Filename')
            if len(Filename_Nodelist)==0:
                print 'There is no <Filename> Tag in '+str(gid)+' <Picture> Node.'
            else:
                Filename_Node=Filename_Nodelist[0].firstChild        
                if type(Filename_Node) is NoneType:
                    print 'You need to set picture file name for the '+str(gid)+' <Picture> Node.'
                    print 'The program will stop!'
                    flag=1
                else:
                    Filename=Picture_path+Filename_Node.data            
                    if os.path.isfile(Filename) is False:
                        print Filename,' is not right,Check it.'
                        flag=1
            Title_Nodelist=Picture_Node.getElementsByTagName('Title')
            if len(Title_Nodelist)==0:
                print 'There is no <Tile> Tag in '+str(gid)+' <Picture> Node.'
                print 'Set the picture file name as default picture title.'
                Title=Filename
            else:
                Title_Node=Title_Nodelist[0].firstChild
                if type(Title_Node) is NoneType:
                    print 'You have not set picture file name for the '+str(gid)+' <Picture> Node.'
                    print 'But the program will continue'
                else:
                    Title=Title_Node.data
            Longitude_Nodelist=Picture_Node.getElementsByTagName('Longitude')
            if len(Longitude_Nodelist)==0:
                print 'There is no <Longitude> Tag in '+str(gid)+' <Picture> Node.'
                print 'You need to set the location where you take this photo.'        
            else:
                Longitude_Node=Longitude_Nodelist[0].firstChild
                if type(Longitude_Node) is NoneType:
                    print 'You have not set Longitude value for the '+str(gid)+' <Picture> Node.'
                    print 'The program will stop!'
                else:
                    Longitude=Longitude_Node.data
                    try:            
                        Longitude=float(Longitude)                    
                    except:
                        print Longitude ,'is not digital number in the '+str(gid)+' <Picture> Node.'
                    
            Latitude_Nodelist=Picture_Node.getElementsByTagName('Latitude')
            if len(Latitude_Nodelist)==0:
                print 'There is no <Latitude> Tag in '+str(gid)+' <Picture> Node.'
                print 'You need to set the location where you take this picture.'        
            else:
                Latitude_Node=Latitude_Nodelist[0].firstChild
                if type(Latitude_Node) is NoneType:
                    print 'You have not set Latitude value for the '+str(gid)+' <Picture> Node.'
                    print 'The program will stop!'
                else:
                    Latitude=Latitude_Node.data
                    try:
                        Latitude=float(Latitude)                    
                    except:
                        print Latitude ,'is not digital number in the '+str(gid)+' <Picture> Node.'
                    
                    
            Elevation_Nodelist=Picture_Node.getElementsByTagName('Elevation')
            if len(Elevation_Nodelist)==0:
                print 'There is no <Elevation> Tag in '+str(gid)+' <Picture> Node.'
                print 'Have set 0 meter as default Elevation value.'        
            else:
                Elevation_Node=Elevation_Nodelist[0].firstChild
                if type(Elevation_Node) is NoneType:
                    print 'You have not set Elevation value for the '+str(gid)+' <Picture> Node.'
                    print 'Have set 0 meter as default Elevation value.' 
                    print 'The program will continue!'
                else:
                    Elevation=Elevation_Node.data                          
                    try:
                        Elevation=float(Elevation)                    
                    except:
                        print Elevation ,'is not digital number in the '+str(gid)+' <Picture> Node.'
                    
            Description_Nodelist=Picture_Node.getElementsByTagName('Description')
            if len(Description_Nodelist)==0:
                print 'There is no <Description> Tag in '+str(gid)+' <Picture> Node.'
                print 'Have set '' as default Elevation value.'        
            else:
                Description_Node=Description_Nodelist[0].firstChild
                if type(Description_Node) is NoneType:
                    print 'You have not set Description value for the '+str(gid)+' <Picture> Node.'
                    print 'Have set '' as default Description value.' 
                    print 'The program will continue!'
                else:
                    Description=Description_Node.data
            if flag==1:
                print ''
            Filename_list.append(Filename)
            print Filename_list
            Title_list.append(Title)        
            Longitude_list.append(Longitude)
            Latitude_list.append(Latitude)
            Elevation_list.append(Elevation)
            Description_list.append(Description)
            gid=gid+1
##        picture_info={'Copyright':Copyright,'Filename':Filename_list,'Title':Title_list,'Longitude':Longitude_list,'Latitude':Latitude_list,'Elevation':Elevation_list,'Description':Description_list}
##        return picture_info
    ##=====create kml file====
class test:
    t='sss'
    a=0
    def __init__(self):
        title='ppppptile'
        self.a=1
        b=2
    def funct():
        c=a+b

    

if __name__=='__main__':    
    outpath=r'D:\Python\pictures'    
    metafile=r'D:\Python\pictures\picture_info.xml'
    p=Picture()
    print p.Copyright
    t=test()
    print t.a
##    Picture=read_metainfo(metafile)
##    if type(Picture) is NoneType:
##        print 'error'
##    else:
##        print Picture.Copyright]
    print '---end----'    



