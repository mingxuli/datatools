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
import codecs
import shutil
import zipfile


def writekml(picture,kmzfile):
    Title=picture.Title
    Copyright= picture.Copyright
    Filename= picture.Filename
    Longitude= picture.Longitude
    Latitude =picture.Latitude
    Elevation =picture.Elevation
    Description= picture.Description
    Template_path=picture.Template
    
    Default_Template="""
<div id="Title" align="center"><font size="6">{{Title}}</font></div>
<hr>
<div id="context">{{Description}}</div>
<div id="pic" align="enter"><img  src="{{filepath}}" width="800"></div>
<hr>
<div id="Copyright">{{Copyright}}</div>
"""
    
    if Template_path=='Default':
        Template=Default_Template
    else:
        f=open(Template_path)
        Template=f.readlines()
        f.close()
        Template=string.join(Template)
    pathname=os.path.dirname(kmzfile)
    
    basename=os.path.basename(kmzfile)
    basename=string.split(basename,'.')
    basename=string.join(basename[0:-1],'_')
    kmlfile=pathname+os.sep+basename+'.kml'
    zipfilename=pathname+os.sep+basename+'.zip'
    kmzfilename=pathname+os.sep+basename+'.kmz'
    z=zipfile.ZipFile(zipfilename, 'w',zipfile.ZIP_DEFLATED)        
    
    ##for create new kml file
    impl = minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'kml', None)
    root = dom.documentElement
    Document_Node=dom.createElement('Document')
    root.appendChild(Document_Node)
    name_Node=dom.createElement('name')
    Document_Node.appendChild(name_Node)
    Text=dom.createTextNode('doc.kml')
    name_Node.appendChild(Text)
    
    for i in range(len(Filename)): 
        coor=str(Longitude[i])+','+str(Latitude[i])+','+str(Elevation[i])
        Placemark_Node=dom.createElement('Placemark')
        Document_Node.appendChild(Placemark_Node)
        
        name_Node=dom.createElement('name')
        Placemark_Node.appendChild(name_Node)
        Text=dom.createTextNode(Title[i])
        name_Node.appendChild(Text)
        
        filepath=os.path.basename(Filename[i])
        filepath=string.replace(filepath,' ','_')             
        z.write(Filename[i],'files'+os.sep+filepath)
        Template=string.replace(Template,'{{Title}}',Title[i])
        Template=string.replace(Template,'{{Description}}',Description[i])
        Template=string.replace(Template,'{{filepath}}','files/'+filepath)
        Template=string.replace(Template,'{{Copyright}}',Copyright)
        
        description_Node=dom.createElement('description')
        Placemark_Node.appendChild(description_Node)
        Text=dom.createCDATASection(Template)
        description_Node.appendChild(Text)
        
        Point_Node=dom.createElement('Point')
        Placemark_Node.appendChild(Point_Node)
        coordinates_Node=dom.createElement('coordinates')
        Point_Node.appendChild(coordinates_Node)
        Text=dom.createTextNode(coor)
        coordinates_Node.appendChild(Text)
    kml=root.toxml()

    f=open(kmlfile, 'w')
    writer = codecs.lookup('utf-8')[3](f)
    dom.writexml(writer, encoding='utf-8')
    writer.close()
    f.close()
    z.write(kmlfile,'doc.kml')    
    z.close()
    ## delete temp kml file
    os.system('del '+kmlfile)
    ## rename zip to kmz    
    os.rename(zipfilename,kmzfilename)
class Picture:
    Copyright=''
    template=''
    Filename=[]
    Title=[]        
    Longitude=[]
    Latitude=[]
    Elevation=[]
    Description=[]
    
def read_metainfo(metafile):
    ##for read picture_info.xml file
    picture=Picture()
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
            Copyright=Copyright_Node.data
            picture.Copyright=Copyright
            
    Template_Nodelist=root.getElementsByTagName('Template')    
    if len(Template_Nodelist)==0:
        print 'There is no Template Tag in the Picture_info file,Are you sure?'            
    else:
        Template_Node=Template_Nodelist[0].firstChild
        if type(Template_Node) is NoneType:            
            print 'You not set special template.'                
        else:
            Template=Template_Node.data
            if os.path.isfile(Template):
                picture.Template=Copyright
            else:
                print 'You have set the template, but the path is not right,Check it!'
                picture.Template='Default'
            
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
                else:
                    (picture.Filename).append(Filename)
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
                (picture.Title).append(Title)
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
                picture.Longitude.append(Longitude)
                    
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
                picture.Latitude.append(Latitude)
                    
                    
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
                picture.Elevation.append(Elevation)
                    
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
                picture.Description.append(Description)
        if flag==1:
            print ''

        gid=gid+1
    return picture

   

if __name__=='__main__':    
    kmlfile=r'D:\Python\pictures\out.kmz'    
    metafile=r'D:\Python\pictures\picture_info.xml'
    
    P=read_metainfo(metafile)
    if type(P) is NoneType:
        print 'error'
    else:
        result=writekml(P,kmlfile)
    print '---end----'    



