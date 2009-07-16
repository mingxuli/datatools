#conding=utf8
#!/usr/bin/env python
###############################################################################
# Merge_Tiles.py
#
# 作者: Wu Lizong
# 邮件: wulizong@lzb.ac.cn
# 单位: 中国科学院寒区旱区环境与工程研究所
# 项目: 中国基金委西部环境与生态数据中心
# 目的: 将GDAL2Tiles工具产生（gdal2tiles.py) 的分幅结果拼成一个大图.
#       程序使用了gdal_merge.py源代码,修改了参数输入方式,以便python可以直接调用
# 使用说明：
#     1. 需要用到gdal模块和PYNumic模块,可在python网站下载
#     2. 程序参数说明：在主程序部分(即__name__="__main__"部分),修改:
#        2.1    workspace=u"D:\\website\\TMS\\" #输入文件目录
#        2.2    outpath=u"D:\\website\\out\\"   #输出文件目录
#        2.3    gdal_translate=u"C:\\gdalwin32-1.6\\bin\\gdal_translate.exe" #gdal_translate工具的目录
#        2.4    #kml_url="files:///" ##KML文件的超级链接路径,如果是本地浏览则用files,如果是服务器则用
#               kml_url="http://map.westgis.ac.cn/tms/test/"
#               为了在大多数服务器下有效,请注意大小写                 
#        2.2 输入路径和输出路径
#     3. 输入路径的文件夹结构,如输入目录为d:\input,Tile输出结果应该并列的位于该目录下,且该目录下不应有其他文件,
#        另外在拼接前清确认所有待拼接的分幅数据的缩放等级是一样的(目录中5,6,7,8即为缩放等级):
#        D:\input\
#        ├─N-46-30
#        │  ├─5
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─6
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─7
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─8
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─x
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─doc.kml
#        │  ├─googlemaps.html
#        │  ├─openlayers.html
#        │  └─tilemapresource.xml
#        ├─N-46-35
#        │  ├─5
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─6
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─7
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─8
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─x
#        │  │  ├─xx
#        │  │  └─xx
#        │  ├─doc.kml
#        │  ├─googlemaps.html
#        │  ├─openlayers.html
#        │  └─tilemapresource.xml
#     4.输出路径不应放在输入路径的下面,否则的话，程序可能陷入死循环.
#     5.部分拼接结果如果要与其他分幅数据继续拼接,则可将部分拼接结果作为一个目录，与其他分幅目录并列,再行拼接皆可
#     6.如果只修改kml的服务器地址,则将原来的输出目录作为输入目录，再行本程序即可
#代码修改日志:
#   2009-7-1 v0.1  可以进行拼接了,输出结果合并了kml文件和xml元数据文件,googlemap和openlayer没有合并,仅用随意选取了一个


###############################################################################

import os,string,glob,sys,shutil,codecs
from xml.dom import minidom
try:
    from osgeo import gdal
except ImportError:
    import gdal

global verbose,gdal_translate
verbose = 0
## 以下为gdalmerge.py的代码
# =============================================================================
def raster_copy( s_fh, s_xoff, s_yoff, s_xsize, s_ysize, s_band_n,
                 t_fh, t_xoff, t_yoff, t_xsize, t_ysize, t_band_n,
                 nodata=None ):

    if nodata is not None:
        return raster_copy_with_nodata(
            s_fh, s_xoff, s_yoff, s_xsize, s_ysize, s_band_n,
            t_fh, t_xoff, t_yoff, t_xsize, t_ysize, t_band_n,
            nodata )

    if verbose != 0:
        print 'Copy %d,%d,%d,%d to %d,%d,%d,%d.' \
              % (s_xoff, s_yoff, s_xsize, s_ysize,
             t_xoff, t_yoff, t_xsize, t_ysize )

    s_band = s_fh.GetRasterBand( s_band_n )
    t_band = t_fh.GetRasterBand( t_band_n )

    data = s_band.ReadRaster( s_xoff, s_yoff, s_xsize, s_ysize,
                              t_xsize, t_ysize, t_band.DataType )
    t_band.WriteRaster( t_xoff, t_yoff, t_xsize, t_ysize,
                        data, t_xsize, t_ysize, t_band.DataType )
        

    return 0
    
# =============================================================================
def raster_copy_with_nodata( s_fh, s_xoff, s_yoff, s_xsize, s_ysize, s_band_n,
                             t_fh, t_xoff, t_yoff, t_xsize, t_ysize, t_band_n,
                             nodata ):
    try:
        import numpy as Numeric
    except ImportError:
        import Numeric
    
    if verbose != 0:
        print 'Copy %d,%d,%d,%d to %d,%d,%d,%d.' \
              % (s_xoff, s_yoff, s_xsize, s_ysize,
             t_xoff, t_yoff, t_xsize, t_ysize )

    s_band = s_fh.GetRasterBand( s_band_n )
    t_band = t_fh.GetRasterBand( t_band_n )

    data_src = s_band.ReadAsArray( s_xoff, s_yoff, s_xsize, s_ysize,
                                   t_xsize, t_ysize )
    data_dst = t_band.ReadAsArray( t_xoff, t_yoff, t_xsize, t_ysize )

    nodata_test = Numeric.equal(data_src,nodata)
    to_write = Numeric.choose( nodata_test, (data_src, data_dst) )
                               
    t_band.WriteArray( to_write, t_xoff, t_yoff )

    return 0
    
# =============================================================================
def names_to_fileinfos( names ):
    """
    Translate a list of GDAL filenames, into file_info objects.

    names -- list of valid GDAL dataset names.

    Returns a list of file_info objects.  There may be less file_info objects
    than names if some of the names could not be opened as GDAL files.
    """
    
    file_infos = []
    for name in names:        
        fi = file_info()
        if fi.init_from_name( name ) == 1:
            file_infos.append( fi )

    return file_infos

# *****************************************************************************
class file_info:
    """A class holding information about a GDAL file."""

    def init_from_name(self, filename):
        """
        Initialize file_info from filename

        filename -- Name of file to read.

        Returns 1 on success or 0 if the file can't be opened.
        """

        fh = gdal.Open( filename )
        if fh is None:
            return 0

        self.filename = filename
        self.bands = fh.RasterCount
        self.xsize = fh.RasterXSize
        self.ysize = fh.RasterYSize
        self.band_type = fh.GetRasterBand(1).DataType
        self.projection = fh.GetProjection()
        self.geotransform = fh.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize

        ct = fh.GetRasterBand(1).GetRasterColorTable()
        if ct is not None:
            self.ct = ct.Clone()
        else:
            self.ct = None

        return 1

    def report( self ):
        print 'Filename: '+ self.filename
        print 'File Size: %dx%dx%d' \
              % (self.xsize, self.ysize, self.bands)
        print 'Pixel Size: %f x %f' \
              % (self.geotransform[1],self.geotransform[5])
        print 'UL:(%f,%f)   LR:(%f,%f)' \
              % (self.ulx,self.uly,self.lrx,self.lry)

    def copy_into( self, t_fh, s_band = 1, t_band = 1, nodata_arg=None ):
        """
        Copy this files image into target file.

        This method will compute the overlap area of the file_info objects
        file, and the target gdal.Dataset object, and copy the image data
        for the common window area.  It is assumed that the files are in
        a compatible projection ... no checking or warping is done.  However,
        if the destination file is a different resolution, or different
        image pixel type, the appropriate resampling and conversions will
        be done (using normal GDAL promotion/demotion rules).

        t_fh -- gdal.Dataset object for the file into which some or all
        of this file may be copied.

        Returns 1 on success (or if nothing needs to be copied), and zero one
        failure.
        """
        t_geotransform = t_fh.GetGeoTransform()
        t_ulx = t_geotransform[0]
        t_uly = t_geotransform[3]
        t_lrx = t_geotransform[0] + t_fh.RasterXSize * t_geotransform[1]
        t_lry = t_geotransform[3] + t_fh.RasterYSize * t_geotransform[5]

        # figure out intersection region
        tgw_ulx = max(t_ulx,self.ulx)
        tgw_lrx = min(t_lrx,self.lrx)
        if t_geotransform[5] < 0:
            tgw_uly = min(t_uly,self.uly)
            tgw_lry = max(t_lry,self.lry)
        else:
            tgw_uly = max(t_uly,self.uly)
            tgw_lry = min(t_lry,self.lry)
        
        # do they even intersect?
        if tgw_ulx >= tgw_lrx:
            return 1
        if t_geotransform[5] < 0 and tgw_uly <= tgw_lry:
            return 1
        if t_geotransform[5] > 0 and tgw_uly >= tgw_lry:
            return 1
            
        # compute target window in pixel coordinates.
        tw_xoff = int((tgw_ulx - t_geotransform[0]) / t_geotransform[1] + 0.1)
        tw_yoff = int((tgw_uly - t_geotransform[3]) / t_geotransform[5] + 0.1)
        tw_xsize = int((tgw_lrx - t_geotransform[0])/t_geotransform[1] + 0.5) \
                   - tw_xoff
        tw_ysize = int((tgw_lry - t_geotransform[3])/t_geotransform[5] + 0.5) \
                   - tw_yoff

        if tw_xsize < 1 or tw_ysize < 1:
            return 1

        # Compute source window in pixel coordinates.
        sw_xoff = int((tgw_ulx - self.geotransform[0]) / self.geotransform[1])
        sw_yoff = int((tgw_uly - self.geotransform[3]) / self.geotransform[5])
        sw_xsize = int((tgw_lrx - self.geotransform[0]) \
                       / self.geotransform[1] + 0.5) - sw_xoff
        sw_ysize = int((tgw_lry - self.geotransform[3]) \
                       / self.geotransform[5] + 0.5) - sw_yoff

        if sw_xsize < 1 or sw_ysize < 1:
            return 1

        # Open the source file, and copy the selected region.
        s_fh = gdal.Open( self.filename )

        return \
            raster_copy( s_fh, sw_xoff, sw_yoff, sw_xsize, sw_ysize, s_band,
                         t_fh, tw_xoff, tw_yoff, tw_xsize, tw_ysize, t_band,
                         nodata_arg )
def format_translate(input_file,output_file,out_format):    
    cmd_str=gdal_translate+' -of '+out_format+' '+input_file+' '+output_file    
    os.system(cmd_str)
    cmd_str=None
    os.remove(input_file)

# =============================================================================
def Usage():
    print 'Usage: gdal_merge([-o out_filename] [-of out_format] [-co NAME=VALUE]*'
    print '                     [-ps pixelsize_x pixelsize_y] [-separate] [-v] [-pct]'
    print '                     [-ul_lr ulx uly lrx lry] [-n nodata_value] [-init value]'
    print '                     [-ot datatype] [-createonly] input_files'
    print '                     [--help-general])'
    print

# =============================================================================
#
# Program mainline.
#

def gdal_merge(argv):

    names = []
    format = 'GTiff'
    out_file = 'out.tif'

    ulx = None
    psize_x = None
    separate = 0
    copy_pct = 0
    nodata = None
    create_options = []
    pre_init = None
    band_type = None
    createonly = 0
    verbose = 0

    #gdal.AllRegister()
    #argv = gdal.GeneralCmdLineProcessor( sys.argv )
    if argv is None:
        ##sys.exit( 0 )
        print u'没有参数！'
    else:
        argv=string.split(argv)
    

    # Parse command line arguments.
    i = 0
    while i < len(argv):
        arg = argv[i]

        if arg == '-o':
            i = i + 1
            out_file = argv[i]            

        elif arg == '-v':
            verbose = 1

        elif arg == '-createonly':
            createonly = 1

        elif arg == '-separate':
            separate = 1

        elif arg == '-seperate':
            separate = 1

        elif arg == '-pct':
            copy_pct = 1

        elif arg == '-ot':
            i = i + 1
            band_type = gdal.GetDataTypeByName( argv[i] )
            if band_type == gdal.GDT_Unknown:
                print 'Unknown GDAL data type: ', argv[i]
                sys.exit( 1 )

        elif arg == '-init':
            i = i + 1
            pre_init = float(argv[i])

        elif arg == '-n':
            i = i + 1
            nodata = float(argv[i])
           

        elif arg == '-f':
            # for backward compatibility.
            i = i + 1
            format = argv[i]

        elif arg == '-of':
            i = i + 1
            format = argv[i]

        elif arg == '-co':
            i = i + 1
            create_options.append( argv[i] )

        elif arg == '-ps':
            psize_x = float(argv[i+1])
            psize_y = -1 * abs(float(argv[i+2]))
            i = i + 2

        elif arg == '-ul_lr':
            ulx = float(argv[i+1])
            uly = float(argv[i+2])
            lrx = float(argv[i+3])
            lry = float(argv[i+4])
            i = i + 4

        elif arg[:1] == '-':
            print 'Unrecognised command option: ', arg
            Usage()
            sys.exit( 1 )

        else:
            names.append( arg )
            
        i = i + 1

    if len(names) == 0:
        print 'No input files selected.'
        Usage()
        sys.exit( 1 )   
    
    
    Driver = gdal.GetDriverByName(format)
    if Driver is None:
        print 'Format driver %s not found, pick a supported driver.' % format
        sys.exit( 1 )

    DriverMD = Driver.GetMetadata()
    if not DriverMD.has_key('DCAP_CREATE'):
        if verbose != 0:
            print """GDAL不支持%s格式精确输出,程序将创建一个临时GTiff文件,然后转换为目标格式""" % format
        out_file=out_file+'.tif'
        temp_format='GTiff'
        Driver=gdal.GetDriverByName(temp_format)
        #sys.exit( 1 )

    # Collect information on all the source files.
    file_infos = names_to_fileinfos( names )

    if ulx is None:
        ulx = file_infos[0].ulx
        uly = file_infos[0].uly
        lrx = file_infos[0].lrx
        lry = file_infos[0].lry
        
        for fi in file_infos:
            ulx = min(ulx, fi.ulx)
            uly = max(uly, fi.uly)
            lrx = max(lrx, fi.lrx)
            lry = min(lry, fi.lry)

    if psize_x is None:
        psize_x = file_infos[0].geotransform[1]
        psize_y = file_infos[0].geotransform[5]

    if band_type is None:
        band_type = file_infos[0].band_type

    # Try opening as an existing file.
    gdal.PushErrorHandler( 'CPLQuietErrorHandler' )
    t_fh = gdal.Open( out_file, gdal.GA_Update )
    gdal.PopErrorHandler()
    
    # Create output file if it does not already exist.
    if t_fh is None:
        geotransform = [ulx, psize_x, 0, uly, 0, psize_y]

        xsize = int((lrx - ulx) / geotransform[1] + 0.5)
        ysize = int((lry - uly) / geotransform[5] + 0.5)

        if separate != 0:
            bands = len(file_infos)
        else:
            bands = file_infos[0].bands

        t_fh = Driver.Create( out_file, xsize, ysize, bands,
                              band_type, create_options )
        if t_fh is None:
            print 'Creation failed, terminating gdal_merge.'
            sys.exit( 1 )
            
        t_fh.SetGeoTransform( geotransform )
        t_fh.SetProjection( file_infos[0].projection )

        if copy_pct:
            t_fh.GetRasterBand(1).SetRasterColorTable(file_infos[0].ct)
    else:
        if separate != 0:
            bands = len(file_infos)
        else:
            bands = min(file_infos[0].bands,t_fh.RasterCount)

    # Do we need to pre-initialize the whole mosaic file to some value?
    if pre_init is not None:
        for i in range(t_fh.RasterCount):
            t_fh.GetRasterBand(i+1).Fill( pre_init )

    # Copy data from source files into output file.
    t_band = 1
    for fi in file_infos:
        if createonly != 0:
            continue
        
        if verbose != 0:
            print
            fi.report()

        if separate == 0 :
            for band in range(1, bands+1):
                fi.copy_into( t_fh, band, band, nodata )
        else:
            fi.copy_into( t_fh, 1, t_band, nodata )
            t_band = t_band+1
            
    # Force file to be closed.
    t_fh = None
    # 转换为格式,删除临时文件
    if temp_format=="GTiff":
        input_file=out_file
        output_file=string.replace(input_file,'.tif','')
        out_format=format
        format_translate(input_file,output_file,out_format)
def Merge_Tiles(workspace,outpath,gdal_translate,kml_url):
    folder_list=[]
    fullname_list=[]
    basename_list=[]
    for dir,subdir,basename in os.walk(workspace):    
        if len(basename)>0:
            for filename in basename:
                basename_list.append(filename)
                fullname=dir+os.sep+filename
                fullname_list.append(fullname)
                foldername=string.replace(dir,workspace,'')            
                foldername=string.split(foldername,os.sep)            
                foldername=string.join(foldername[1:len(foldername)],os.sep)            
                folder_list.append(foldername)
    ##处理输出目录
    if outpath[-1]<>os.sep:
        outpath=outpath+os.sep
    ##处理url地址
    if kml_url[-1]!='/':
        kml_url=kml_url+'/'
    
    ##进行拼接
    for tile in set(folder_list):
        ##创建输出目录
        if os.path.exists(outpath+tile) is False:        
            folder=string.split(tile,os.sep)
            out_dir=outpath
            for i in range(len(folder)):
                out_dir=out_dir+folder[i]+os.sep
                if os.path.exists(out_dir) is False:
                    os.mkdir(out_dir) 
        index = [i for i in range(len(folder_list)) if folder_list[i]==tile]    
        basenames=[basename_list[i] for i in index]
        for shortname in set(basenames):
            len_filename=len(shortname)
            file_format=shortname[len_filename-3:len_filename]        
            outfile=outpath+tile+os.sep+shortname
            new_index=[i for i in index if basename_list[i]==shortname]
            if string.lower(file_format)=='png':                
                ##如果有多个同名文件，则合并                
                if len(new_index)>1:
                    if verbose != 0:
                        print u'合并形成',outfile
                    inputfiles=[fullname_list[i] for i in new_index]
                    inputfiles=string.join(inputfiles,' ')                    
                    argv="-o "+outfile+" -n 0 -of PNG "+inputfiles                    
                    gdal_merge(argv)
                if len(new_index)==1:
                    if verbose != 0:
                        print u'复制转移',outfile
                    shutil.copyfile(fullname_list[new_index[0]], outfile)
            if string.lower(file_format)=='kml':
                for i in range(len(new_index)):
                    kmlfile=fullname_list[new_index[i]]   
                    dom=minidom.parse(kmlfile)
                    root=dom.documentElement
                    if i==0:
                        new_dom=dom
                        new_root=new_dom.documentElement
                        Document_Node=new_root.getElementsByTagName('Document')[0]
                    else:
                        new_NetworkLink_nodelist=new_root.getElementsByTagName('NetworkLink')
                        for Node in new_NetworkLink_nodelist:
                            new_name=Node.getElementsByTagName('name')[0].firstChild.data
                            old_NetworkLink_nodelist=root.getElementsByTagName('NetworkLink')
                            for old_Node in old_NetworkLink_nodelist:
                                old_name=old_Node.getElementsByTagName('name')[0].firstChild.data
                                if old_name!=new_name:
                                    Document_Node.appendChild(old_Node)
                        
                NetworkLink_nodelist=new_root.getElementsByTagName('NetworkLink')
                for Node in NetworkLink_nodelist:
                    name_node=Node.getElementsByTagName('name')[0]
                    href_node=Node.getElementsByTagName('href')[0]
                    name=name_node.firstChild.data
                    url=kml_url+name
                    url=string.replace(url,'png','kml')
                    Text=new_dom.createTextNode(url)
                    Old_Text=href_node.firstChild
                    href_node.replaceChild(Text,Old_Text)
                
                    
                f=open(outfile,'w')
                writer = codecs.lookup('utf-8')[3](f)
                new_dom.writexml(writer,encoding='utf-8')
                writer.close()
                f.close()
            if string.lower(file_format)=='xml':
                for i in range(len(new_index)):
                    xmlfile=fullname_list[new_index[i]]
                    dom=minidom.parse(xmlfile)
                    root=dom.documentElement
                    if i==0:
                        new_dom=dom
                        new_root=new_dom.documentElement
                        Title_Node=new_root.getElementsByTagName('Title')[0]
                        Text=new_dom.createTextNode('ETM Mosaic 2000')
                        Old_Text=Title_Node.firstChild
                        Title_Node.replaceChild(Text,Old_Text)
                        BoundingBox=new_root.getElementsByTagName('BoundingBox')[0]
                        minx=float(BoundingBox.getAttribute('minx'))
                        miny=float(BoundingBox.getAttribute('miny'))
                        maxx=float(BoundingBox.getAttribute('maxx'))
                        maxy=float(BoundingBox.getAttribute('maxy'))
                        
                        Origin=new_root.getElementsByTagName('Origin')[0]
                        start_x=float(Origin.getAttribute('x'))
                        start_y=float(Origin.getAttribute('y'))
                        TileSet=new_root.getElementsByTagName('TileSet')
                        for node in TileSet:
                            order=node.getAttribute('order')
                            node.setAttribute('href',kml_url+order)
                    else:
                        temp_BoundingBox=root.getElementsByTagName('BoundingBox')[0]
                        temp_minx=float(temp_BoundingBox.getAttribute('minx'))
                        temp_miny=float(temp_BoundingBox.getAttribute('miny'))
                        temp_maxx=float(temp_BoundingBox.getAttribute('maxx'))
                        temp_maxy=float(temp_BoundingBox.getAttribute('maxy'))
                        
                        temp_Origin=root.getElementsByTagName('Origin')[0]
                        sx=float(temp_Origin.getAttribute('x'))
                        sy=float(temp_Origin.getAttribute('y'))
                        if minx>temp_minx:
                            minx=temp_minx
                        if miny>temp_miny:
                            miny=temp_miny
                        if maxx<temp_maxx:
                            maxx=temp_maxx
                        if maxy<temp_maxy:
                            maxy=temp_maxy
                        if start_x>sx:
                            start_x=sx
                        if start_y>sy:
                            start_y=sy
                BoundingBox.setAttribute('minx',str(minx))
                BoundingBox.setAttribute('miny',str(miny))
                BoundingBox.setAttribute('maxx',str(maxx))
                BoundingBox.setAttribute('maxy',str(maxy))
                
                Origin.setAttribute('x',str(start_x))
                Origin.setAttribute('y',str(start_y))

                f=open(outfile,'w')
                writer = codecs.lookup('utf-8')[3](f)
                new_dom.writexml(writer,encoding='utf-8')
                writer.close()
                f.close()
            if string.lower(file_format)=='tml':
                for i in range(len(new_index)):
                    htmlfile=fullname_list[new_index[i]]
                    shutil.copyfile(htmlfile, outfile)
    print 'Totla file count is',len(fullname_list)
    print len(folder_list)
    print len(set(folder_list))
if __name__=="__main__":
    workspace=u"D:\\website\\TMS\\"
    outpath=u"D:\\website\\out\\"    
    gdal_translate=u"C:\\gdalwin32-1.6\\bin\\gdal_translate.exe" 
    #kml_url="files:///" ##for local file   #针对本地文件
    kml_url="http://map.westgis.ac.cn/tms/test/"
    Merge_Tiles(workspace,outpath,gdal_translate,kml_url)
    print 'end'
