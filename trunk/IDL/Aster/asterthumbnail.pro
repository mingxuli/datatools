;����ASTER����ͼ�ĳ���,v0.1
;����ͼ����Aster band1,band2,band3��ϣ���СΪԭ���ݿɼ��ⲿ�ֵ�5/1����Ҫ�ı�����ͼ�Ĵ�С������������е�datasize
;datasize=size(red)/5,���Բ��ù̶�ֵ
;����������IDL���������У�������ֱ�����У�Ȼ��Ӵ򿪴�����ѡȡ�ļ������ɵ�����ͼ����ԭ����ASTER�ļ�Ŀ¼�У�
;�ļ�����ԭ�ļ���ͬ,��׺Ϊ.jpg
;Author:wulizong
;Create data:2006-8-6
;History:
;        v0.1:ֻ�ʺ�ASTER L1A����
;        v0.2:�ʺ�ASTER L1B��ASTER L1A ����
pro asterthumbnail
  Compile_opt strictarr
  workspace = 'D:\IDLWorkspace\aster\data\'
  filelist=FILE_SEARCH(workspace+'*.hdf',count=n)

  For i=0,n-1 Do Begin
    outfile=filelist[i]+'.jpg'
    fileid=HDF_OPEN(filelist[i],/read)
    If(fileid Eq -1) Then Begin
      PRINT,'The Error File Name is: '+filename[i]
      Continue
    Endif
    hdfid=HDF_SD_START(filelist[i],/read)
    ;Create a arrary variable to story the datasets name
    CATCH, Error_status
    ;This statement begins the error handler:
    If Error_status Ne 0 Then Begin
      PRINT, 'Error index: ', Error_status
      PRINT, 'Error message: ', !ERROR_STATE.MSG
      PRINT, 'the error file is:'+filename[i]
      Continue
    Endif
    ;��ȡhdf�еı�������
    varnames = ''

    HDF_SD_FILEINFO, hdfid, n_vars, n_glo_atts
    print,filelist[i]
    print,n_vars
    ;=====for L1A========
    ;Aster L1A���ݲ�Ʒ��194������,��L1Bֻ��26������
    ;Aster L1A�����в��εı�������Ϊ'ImageData'
    ;Aster L1B��ǰ3�����ε����Ʒֱ�ΪImageData1,ImageData2,ImageData3N

    If (n_vars Gt 26) Then Begin
      index=WHERE(varnames Eq 'ImageData')
      index_r=index[0]
      index_g=index[0]
      index_b=index[0]
    Endif else begin
    	index_r=HDF_SD_NAMETOINDEX(hdfid,'ImageData1')
      index_g=HDF_SD_NAMETOINDEX(hdfid,'ImageData2')
      index_b=HDF_SD_NAMETOINDEX(hdfid,'ImageData3N')
    endelse

    ;��ȡ����
    datasetid_r=HDF_SD_SELECT(hdfid,index_r)
    datasetid_g=HDF_SD_SELECT(hdfid,index_g)
    datasetid_b=HDF_SD_SELECT(hdfid,index_b)
    ;Get data
    HDF_SD_GETDATA,datasetid_r,red
    HDF_SD_GETDATA,datasetid_g,green
    HDF_SD_GETDATA,datasetid_b,blue
    ;get data info
    datasize=SIZE(red)/5

    thumbnail=BYTARR(3,datasize[1],datasize[2])
    thumbnail[0,*,*]=CONGRID(blue,datasize[1],datasize[2])
    thumbnail[1,*,*]=CONGRID(green,datasize[1],datasize[2])
    thumbnail[2,*,*]=CONGRID(red,datasize[1],datasize[2])

    HDF_SD_END,hdfid
    HDF_CLOSE,fileid

    window,xsize=datasize[1],ysize=datasize[2],/free,/pixmap
    tvscl,thumbnail,/order
    WRITE_JPEG,outfile,tvrd(true=1),TRUE = 1,QUALITY = 100,/order
  Endfor
  PRINT,'programe is end'
End