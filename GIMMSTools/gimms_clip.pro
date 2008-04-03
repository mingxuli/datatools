;程序信息
;ver 1.1
;date:2008-3-16
;Author:wulizong
;e-mail:wulizong@lzb.ac.cn
;中国科学院寒区旱区环境与工程研究所
;甘肃省兰州市东岗西路320号 邮编：730000
;电话：0931-4967298
;本程序受到国家基金委西部生态与环境数据中心和科技部地球系统科学数据共享网联合资助
;=========程序使用说明================================================================
;
;1.程序运行条件本程序需要在IDL+ENVI的环境下执行
;2.切割范围，数据存放地址等参数，请在def_globalvar程序块中修改
;3.数据的存放结构
;4.工作目录结构：如果工作目录不同，本程序可能无法正常执行
;数据目录/
;        input/     －－原始数据路径
;             1981/
;             1982/
;             1983/
;             1984/
;             1985/
;             1986/
;             ..../
;        output/    －－输出数据路径
;不需要创建下面的目录，程序会自行创建
;              1981/
;              1982/
;              1983/
;              1984/
;              1985/
;              1986/
;              ..../

;※※※※※※※程序修改历史※※※※※※※※※※
;v1.2 2008-2-17 改进了程序对数据目录的限制，只需要将原始数据按年分别存放，而不管年代的目录下有多少级子文件夹，程序都可以读取数据，并将输出结果按年存放
;v1.1 2008-3-16 程序基于从Gimms FTP站点上下载的原始数据上运行的，程序自动解压缩，然后再切割，可以设置输出多种数据格式
;v1.0 2007-8-1  基于已经转换好的ENVI格式的全球数据进行切割的，不能对其它格式的数据进行读取

;代码部分
;请在此处定义程序运行所需的变量
Pro Def_Globalvar
  Common global_var,inpath,outpath,data_type,thumbnail,west_bound,south_bound,east_bound,north_bound
  ;=====设置工作目录路径=====
  inpath='H:\Gimms_NDVIg\GLCF_Global\'
  ;=====定义输出文件路径=====
  outpath='H:\Gimms_NDVIg\China\'
  ;设置切割范围需要切割的感兴趣区域
  ;以下为西部数据中心默认的中国子区范围
  west_bound=70           ;西至     单位：度
  south_bound=15          ;南至
  east_bound=140          ;东至
  north_bound=55          ;北至
  ;是否需要输出缩略图,1为是,0为否
  thumbnail=1
  ;设置输出格式
  ;0 = envi img 格式
  ;1 = Tiff
  ;2 = Erdas Image
  ;3 = ASCII
  ;4 = PCI
  ;5 = Esri Grid

  data_type=0

End
Function SourceRoot

  Compile_opt StrictArr

  HELP, Calls = Calls
  UpperRoutine = (StrTok(Calls[1], ' ', /Extract))[0]
  Skip = 0
  CATCH, ErrorNumber
  If (ErrorNumber Ne 0) Then Begin
    CATCH, /Cancel
    ThisRoutine = ROUTINE_INFO(UpperRoutine, /Functions, /Source)
    Skip = 1
  Endif
  If (Skip Eq 0) Then Begin
    ThisRoutine = ROUTINE_INFO(UpperRoutine, /Source)
    If (thisRoutine.Path Eq '') Then Begin
      MESSAGE,'',/traceback
    Endif
  Endif
  CATCH,/cancel
  If (STRPOS(thisroutine.path,PATH_SEP()) Eq -1 ) Then Begin
    CD, current=current
    sourcePath = FILEPATH(thisrouitine.path, root=current)
  Endif Else Begin
    sourcePath = thisroutine.path
  Endelse
  Root = STRMID(sourcePath, 0, STRPOS(sourcePath, PATH_SEP(), /Reverse_Search) + 1)
  RETURN, Root
End

Pro Gimms_Clip    ;文件名必须与程序名相同，否则无法编译
  Common global_var
  Compile_opt strictarr
  Def_Globalvar
  root=sourceroot()
  Sep=PATH_SEP()
  unzip=root+'7z'


  ;开始ENVI批处理模式
  envi, /restore_base_save_files
  envi_batch_init, log_file='batch.txt'

  ;
  Folderlist=FILE_SEARCH(inpath+'*',/TEST_DIRECTORY,count=num);搜索文件夹

  For i=0,num-1 Do Begin
    ;获得数据存放的一级目录
    Folder=FolderList[i]                          ;年代一级的目录
    ;在输出文件夹中创建子目录
    Pos=STRPOS(Folder,sep,/REVERSE_SEARCH)
    Subdir=STRMID(Folder,Pos+1,STRLEN(Folder)-Pos)

    FILE_MKDIR, outpath+Subdir    ;在输出目录中创建文件夹

    filelist=FILE_SEARCH(Folder,'*.gz',count=n)   ;获取数据清单
    For k=0,n-1 Do Begin

      ;解压缩文件，默认是解压缩在输出目录的根目录下，
      ;解压缩出来的文件为临时文件，切割后就直接删除，避免占太多的磁盘空间
      cmd=unzip+' e ' +Filelist[k]+' -o'+outpath
      SPAWN,cmd,/hide
      tifflist=FILE_SEARCH(outpath+'*.tif',count=c)
      If c Eq 0 Then Begin
        PRINT, Filelist[K] + '没有被解压缩，请检查下载的数据是否正确！'
      Endif Else Begin
        filename=tifflist[0]
        If (FILE_INFO(filename)).exists Then Begin
          b_name=FILE_BASENAME(filename)
          outfilename=outpath+subdir+sep+STRMID(b_name,0,STRLEN(b_name)-4)
          envi_open_file, filename, r_fid=fid

          If (fid Eq -1) Then Begin
            RETURN
          Endif
          envi_file_query, fid, ns=ns, nl=nl, nb=nb

          mapinfo=envi_get_map_info(fid=fid)
          mc=mapinfo.mc
          ps=mapinfo.ps

          ;
          ;起始点是从左上角开始的
          start_x=ROUND((west_bound-mc[2])/ps[0])
          end_x=ROUND((east_bound-mc[2])/ps[0])
          start_y=ROUND((mc[3]-north_bound)/ps[1])
          end_y=ROUND((mc[3]-south_bound)/ps[1])
          ;执行切割操作
          envi_doit,'resize_doit',fid=fid, pos=0,$
            dims=[-1,start_x,end_x,start_y,end_y],$
            interp=0,rfact=[1,1], /IN_MEMORY,r_fid=rfid
          envi_file_query,rfid,ns=ns,nl=nl,dims=dims
          ;输出数据
          ;0 = envi 格式
          ;1 = Tiff
          ;2 = Erdas Image
          ;3 = ASCII
          ;4 = PCI
          ;5 = Esri Grid
          Case data_type Of
            0:ENVI_OUTPUT_TO_EXTERNAL_FORMAT,fid=rfid,pos=0,dims=dims,out_name=outfilename+'.img',/ENVi
            1:ENVI_OUTPUT_TO_EXTERNAL_FORMAT,fid=rfid,pos=0,dims=dims,out_name=outfilename+'.tif',/Tiff
            2:ENVI_OUTPUT_TO_EXTERNAL_FORMAT,fid=rfid,pos=0,dims=dims,out_name=outfilename+'img',/imagine
            3:ENVI_OUTPUT_TO_EXTERNAL_FORMAT,fid=rfid,pos=0,dims=dims,out_name=outfilename+'.dat',/ASCII
            4:ENVI_OUTPUT_TO_EXTERNAL_FORMAT,fid=rfid,pos=0,dims=dims,out_name=outfilename,/PCI
            5:ENVI_OUTPUT_TO_EXTERNAL_FORMAT,fid=rfid,pos=0,dims=dims,out_name=outfilename,/grid

          Endcase
          ;输出缩略图
          If thumbnail Eq 1 Then Begin
            image = ENVI_GET_DATA(fid=rfid, dims=dims, pos=0)
            WRITE_JPEG,outfilename+'.jpg',image,/order,QUALITY=100
          Endif
          FILE_DELETE,filename        ;删除解压缩的临时文件
        Endif
        Endelse
    Endfor
  Endfor

  Envi_batch_exit     ;退出批处理模式
  PRINT,'====end===='
End