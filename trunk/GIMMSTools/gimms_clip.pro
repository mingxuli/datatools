;������Ϣ
;ver 1.1
;date:2008-3-16
;Author:wulizong
;e-mail:wulizong@lzb.ac.cn
;�й���ѧԺ�������������빤���о���
;����ʡ�����ж�����·320�� �ʱࣺ730000
;�绰��0931-4967298
;�������ܵ����һ���ί������̬�뻷���������ĺͿƼ�������ϵͳ��ѧ���ݹ�������������
;=========����ʹ��˵��================================================================
;
;1.��������������������Ҫ��IDL+ENVI�Ļ�����ִ��
;2.�иΧ�����ݴ�ŵ�ַ�Ȳ���������def_globalvar��������޸�
;3.���ݵĴ�Žṹ
;4.����Ŀ¼�ṹ���������Ŀ¼��ͬ������������޷�����ִ��
;����Ŀ¼/
;        input/     ����ԭʼ����·��
;             1981/
;             1982/
;             1983/
;             1984/
;             1985/
;             1986/
;             ..../
;        output/    �����������·��
;����Ҫ���������Ŀ¼����������д���
;              1981/
;              1982/
;              1983/
;              1984/
;              1985/
;              1986/
;              ..../

;�������������������޸���ʷ��������������������
;v1.2 2008-2-17 �Ľ��˳��������Ŀ¼�����ƣ�ֻ��Ҫ��ԭʼ���ݰ���ֱ��ţ������������Ŀ¼���ж��ټ����ļ��У����򶼿��Զ�ȡ���ݣ�����������������
;v1.1 2008-3-16 ������ڴ�Gimms FTPվ�������ص�ԭʼ���������еģ������Զ���ѹ����Ȼ�����и������������������ݸ�ʽ
;v1.0 2007-8-1  �����Ѿ�ת���õ�ENVI��ʽ��ȫ�����ݽ����и�ģ����ܶ�������ʽ�����ݽ��ж�ȡ

;���벿��
;���ڴ˴����������������ı���
Pro Def_Globalvar
  Common global_var,inpath,outpath,data_type,thumbnail,west_bound,south_bound,east_bound,north_bound
  ;=====���ù���Ŀ¼·��=====
  inpath='H:\Gimms_NDVIg\GLCF_Global\'
  ;=====��������ļ�·��=====
  outpath='H:\Gimms_NDVIg\China\'
  ;�����иΧ��Ҫ�и�ĸ���Ȥ����
  ;����Ϊ������������Ĭ�ϵ��й�������Χ
  west_bound=70           ;����     ��λ����
  south_bound=15          ;����
  east_bound=140          ;����
  north_bound=55          ;����
  ;�Ƿ���Ҫ�������ͼ,1Ϊ��,0Ϊ��
  thumbnail=1
  ;���������ʽ
  ;0 = envi img ��ʽ
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

Pro Gimms_Clip    ;�ļ����������������ͬ�������޷�����
  Common global_var
  Compile_opt strictarr
  Def_Globalvar
  root=sourceroot()
  Sep=PATH_SEP()
  unzip=root+'7z'


  ;��ʼENVI������ģʽ
  envi, /restore_base_save_files
  envi_batch_init, log_file='batch.txt'

  ;
  Folderlist=FILE_SEARCH(inpath+'*',/TEST_DIRECTORY,count=num);�����ļ���

  For i=0,num-1 Do Begin
    ;������ݴ�ŵ�һ��Ŀ¼
    Folder=FolderList[i]                          ;���һ����Ŀ¼
    ;������ļ����д�����Ŀ¼
    Pos=STRPOS(Folder,sep,/REVERSE_SEARCH)
    Subdir=STRMID(Folder,Pos+1,STRLEN(Folder)-Pos)

    FILE_MKDIR, outpath+Subdir    ;�����Ŀ¼�д����ļ���

    filelist=FILE_SEARCH(Folder,'*.gz',count=n)   ;��ȡ�����嵥
    For k=0,n-1 Do Begin

      ;��ѹ���ļ���Ĭ���ǽ�ѹ�������Ŀ¼�ĸ�Ŀ¼�£�
      ;��ѹ���������ļ�Ϊ��ʱ�ļ����и���ֱ��ɾ��������ռ̫��Ĵ��̿ռ�
      cmd=unzip+' e ' +Filelist[k]+' -o'+outpath
      SPAWN,cmd,/hide
      tifflist=FILE_SEARCH(outpath+'*.tif',count=c)
      If c Eq 0 Then Begin
        PRINT, Filelist[K] + 'û�б���ѹ�����������ص������Ƿ���ȷ��'
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
          ;��ʼ���Ǵ����Ͻǿ�ʼ��
          start_x=ROUND((west_bound-mc[2])/ps[0])
          end_x=ROUND((east_bound-mc[2])/ps[0])
          start_y=ROUND((mc[3]-north_bound)/ps[1])
          end_y=ROUND((mc[3]-south_bound)/ps[1])
          ;ִ���и����
          envi_doit,'resize_doit',fid=fid, pos=0,$
            dims=[-1,start_x,end_x,start_y,end_y],$
            interp=0,rfact=[1,1], /IN_MEMORY,r_fid=rfid
          envi_file_query,rfid,ns=ns,nl=nl,dims=dims
          ;�������
          ;0 = envi ��ʽ
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
          ;�������ͼ
          If thumbnail Eq 1 Then Begin
            image = ENVI_GET_DATA(fid=rfid, dims=dims, pos=0)
            WRITE_JPEG,outfilename+'.jpg',image,/order,QUALITY=100
          Endif
          FILE_DELETE,filename        ;ɾ����ѹ������ʱ�ļ�
        Endif
        Endelse
    Endfor
  Endfor

  Envi_batch_exit     ;�˳�������ģʽ
  PRINT,'====end===='
End