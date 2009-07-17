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
;2.�иΧ�����ݴ�ŵ�ַ�Ȳ���������Gimms_Clip��������޸�
;3.���ݵĴ�Žṹ
;4.����Ŀ¼�ṹ���������Ŀ¼��ͬ������������޷�����ִ��
;����Ŀ¼/
;        input/     ����ԭʼ����·����Ĭ������Ϊinput,����ļ������Ƹı䣬���ڳ�����Ҳ��Ӧ�ı�
;             1981/
;             1982/
;             1983/
;             1984/
;             1985/
;             1986/
;             ..../
;        output/    �����������·����Ĭ������Ϊoutput,����ļ������Ƹı䣬���ڳ�����Ҳ��Ӧ�ı�
;              1981/
;              1982/
;              1983/
;              1984/
;              1985/
;              1986/
;              ..../

;�������������������޸���ʷ��������������������
;v1.1 2008-3-16 ������ڴ�Gimms FTPվ�������ص�ԭʼ���������еģ���Ҫ���Ƚ�ѹ����Ȼ�����и�
;v1.0 2007-8-1  �����Ѿ�ת���õ�ENVI��ʽ��ȫ�����ݽ����и�ģ����ܶ�������ʽ�����ݽ��ж�ȡ

;���벿��
;���ڴ˴����������������ı���
PRO Def_Globalvar
    Comman_black

END
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


  ;=====���ù���Ŀ¼·��=====
  inpath='d:\Gimms\input\'
  ;=====��������ļ�·��=====
  outpath='d:\Gimms\output\'
  ;�����иΧ��Ҫ�и�ĸ���Ȥ����
  ;=================����Ϊ������������Ĭ�ϵ��й�������Χ====================
  west_x=70           ;����     ��λ����
  south_y=15          ;����
  east_x=140          ;����
  north_y=55          ;����


  ;��ʼENVI������ģʽ
  envi, /restore_base_save_files
  envi_batch_init, log_file='batch.txt'
  ;����GIMMS����

  Foldlist=FILE_SEARCH(inpath+'*',/TEST_DIRECTORY,count=num_folder);�����ļ���

  For i=0,num_folder-1 Do Begin
    ;������ļ����д�����Ŀ¼
    CD,outpath
    pathpos=STRPOS(foldlist[i],'\',/REVERSE_SEARCH)
    Subdir=STRMID(foldlist[i],pathpos+1,4)
    FILE_MKDIR, Subdir    ;Create a subdirectory

    filelist=FILE_SEARCH(Foldlist[i]+'*.img',count=n)   ;��ȡͼ���ļ�����
    For j=0,n-1 Do Begin
      filename=foldlist[i]+'\'+filelist[j]
      PRINT,filename
      envi_open_file, filename, r_fid=fid
      If (fid Eq -1) Then Begin
        envi_batch_exit
        RETURN
      Endif
      envi_file_query, fid, ns=ns, nl=nl, nb=nb
      dims = [-1, 0, ns-1, 0, nl-1]
      pos  = LINDGEN(nb)
      out_name = outpath+STRMID(foldlist[i],pathpos+1,4)+'\'+filelist[j]
      ;===================���и�������Ϣ=======================================
      ;������Ϣ��ͷ�ļ��ж�ȡ��ע����ʼ��ľ�γ�Ȳ���-180�Ⱥ�-90��
      resolution=0.07272             ;�ֱ���,��λ:��
      start_x=-179.55302900                  ;����     ��λ����
      start_y=90.03636360                   ;����
      ;ENVI/IDL��ʼ���Ǵ����Ͻǿ�ʼ��
      start_sample=ROUND((west_x-start_x)/resolution)
      end_sample=ROUND((east_x-start_x)/resolution)
      start_line=ROUND((start_y-north_y)/resolution)
      end_line=ROUND((start_y-south_y)/resolution)
      ;ִ���и����
      envi_doit, 'resize_doit',$
        fid=fid, pos=pos, dims=[-1,start_sample,end_sample,start_line,end_line],$
        ;dims=[-1, 3432,4394,483,1032], $
        interp=0, rfact=[1,1],out_name=out_name, r_fid=r_fid
      ;�������ͼ
      data = ENVI_GET_DATA(fid=fid, dims=dims, pos=0)
      ; TV,data
      WRITE_JPEG,out_name+'.jpg',data,/order,QUALITY=100
    Endfor
  Endfor

  envi_batch_exit     ;�˳�������ģʽ
End