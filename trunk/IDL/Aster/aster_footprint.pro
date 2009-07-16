;=======================================================================
;��������Ҫ��IDL���������У�����IDL6.X-7.x�����µĲ��ԡ�
;�뾡����Ҫ�޸ĳ����ļ����ƣ������޸ģ��뽫��������������ļ����Ʊ���һ�£�����ᵼ�³����޷��������С�
;Author:wulizong
;data:2006-7
;e-mail:wulizong@lzb.ac.cn
;�й���ѧԺ�������������빤���о���
;History:v0.1  /2006-7-30:export shapefile using 'ENVI_EVF_TO_SHAPEFILE' Routines
;        v0.2  /2006-7-30:export shapefile using IDL's 'IDLffShape' object,only read attribute of aster data
;        v0.3.1/2006-8-6:���Ӵ������Ĵ���
;        v0.4  /2007-2-1:��filename�ֶ���ֻ�洢�ļ�����ȥ����ǰ���·�������Ա�֤filename���Ȳ������
;        v0.5  /2007-12-10:�Ż��˲��֣��޶������shapefile�ļ��޷���arcgis�д򿪵�����,
;               ������aster����UTM�������ֶκ�aster����λ���ֶ�

;===========˵��=====================
;ͼ���ĸ��ǵ�λ����Ϣ�Ǵ����hdf��ȫ�����Ա��У�����ı���ʽ����
;GROUP                  = SCENEFOURCORNERS

;      OBJECT                 = UPPERLEFT
;        NUM_VAL              = 2
;        VALUE                = (37.5778999276982, 103.791291574291)
;      END_OBJECT             = UPPERLEFT
;
;      OBJECT                 = UPPERRIGHT
;        NUM_VAL              = 2
;        VALUE                = (37.4517375704332, 104.621551361705)
;      END_OBJECT             = UPPERRIGHT
;
;      OBJECT                 = LOWERLEFT
;        NUM_VAL              = 2
;        VALUE                = (37.0196378138701, 103.661625220573)
;      END_OBJECT             = LOWERLEFT
;
;      OBJECT                 = LOWERRIGHT
;        NUM_VAL              = 2
;        VALUE                = (36.8943161860939, 104.485971865434)
;      END_OBJECT             = LOWERRIGHT
;
;END_GROUP              = SCENEFOURCORNERS

;=======================================================================
Pro aster_footprint

  ;*****************�޸��ļ������������**************************
  workspace='D:\IDLWorkspace\aster\data\'                       ;AsterӰ��Ĵ�ŵ�ַ
  logfile='D:\IDLWorkspace\aster\data\errlog.txt'               ;������־�ļ�������洢λ��
  shapefile='D:\IDLWorkspace\aster\data\ASTER_L1A_Indexmap.shp' ;�����shapefile�ļ�������洢λ��
  boundary_file='D:\IDLWorkspace\boundary\boundary_poly.shp'
  ;*************************************************************
  
  filelist=FILE_SEARCH(workspace+'*.hdf',count=n)
  If n Eq 0 Then Begin
    PRINT,'no hdf file'
    RETURN
  Endif
  
  ;�򿪴�����־�ļ���׼��������д��Ϣ
  OPENW,lun,logfile,/get_lun
  ;���й��߽����ݣ������ж�asterλ���Ǹ�ʡ��
  obound=OBJ_NEW('IDLffShape',boundary_file)
  obound->GetProperty,N_Entities=n_bound_ent
  
  oshp=OBJ_NEW('IDLffShape',shapefile,/update,ENTITY_TYPE=5)
  ;����shape���Ա��ļ�
  oshp->AddAttribute, 'ID', 3, 4,PRECISION=0
  oshp->AddAttribute, 'FileName',7, 50,PRECISION=0
  oshp->AddAttribute, 'FileSize',7,10,PRECISION=0
  oshp->AddAttribute, 'Cent_Lon',5,8,PRECISION=4
  oshp->AddAttribute, 'Cent_Lat',5,8,PRECISION=4
  oshp->AddAttribute, 'UTM_Zone',7,8,PRECISION=0
  oshp->AddAttribute, 'Province',7,20,PRECISION=0
  
  entity={IDL_SHAPE_ENTITY}
  entity.SHAPE_TYPE = 5
  j=0L
  
  For i=0,n-1 Do Begin
    fileid=HDF_OPEN(filelist[i],/read) ;����hdf�����Ƿ���Ч���Ƿ���Դ򿪣�������ܴ����ļ�����¼����־�ļ���
    If (fileid Eq -1) Then Begin
      PRINT,'The error file name is: ' + filelist[i]
      PRINTF,  lun,filelist[i]+'can not open!'
      Continue
    Endif Else Begin
      hdfid=HDF_SD_START(filelist[i],/read);��hdf��ʽ���ļ�,��ȡidֵ
      
      metaindex=HDF_SD_ATTRFIND(hdfid,'productmetadata.0')               ;
      
      HDF_SD_ATTRINFO,hdfid,metaindex,DATA=meta;��ȡ��Ԫ���ݴ洢��mete������
      HDF_SD_END,hdfid
      HDF_CLOSE,fileid
      ;�Ľ�����
      firstpos=STRPOS(meta,'SCENEFOURCORNERS')
      lastpos=STRPOS(meta,'SCENEFOURCORNERS',/REVERSE_SEARCH)
      Scene4Corners=STRMID(meta,firstpos,lastpos-firstpos)
      ;��ȡ4����������ַ�
      upperleft=STRMID(Scene4Corners,STRPOS(Scene4Corners,'UPPERLEFT'),STRPOS(Scene4Corners,'UPPERLEFT',/REVERSE_SEARCH)-STRPOS(Scene4Corners,'UPPERLEFT'))
      upperright=STRMID(Scene4Corners,STRPOS(Scene4Corners,'UPPERRIGHT'),STRPOS(Scene4Corners,'UPPERRIGHT',/REVERSE_SEARCH)-STRPOS(Scene4Corners,'UPPERRIGHT'))
      lowerleft=STRMID(Scene4Corners,STRPOS(Scene4Corners,'LOWERLEFT'),STRPOS(Scene4Corners,'LOWERLEFT',/REVERSE_SEARCH)-STRPOS(Scene4Corners,'LOWERLEFT'))
      lowerright=STRMID(Scene4Corners,STRPOS(Scene4Corners,'LOWERRIGHT'),STRPOS(Scene4Corners,'LOWERRIGHT',/REVERSE_SEARCH)-STRPOS(Scene4Corners,'LOWERRIGHT'))
      
      ;��ȡ��γ��ֵ,ע��Ԫ��������������(y,x)��ʾ��
      upperleft_x=FLOAT(STRMID(upperleft,STRPOS(upperleft,',')+1,STRPOS(upperleft,')')-STRPOS(upperleft,',')-1))
      upperleft_y=FLOAT(STRMID(upperleft,STRPOS(upperleft,'(')+1,STRPOS(upperleft,',')-STRPOS(upperleft,'(')-1))
      
      upperright_x=FLOAT(STRMID(upperright,STRPOS(upperright,',')+1,STRPOS(upperright,')')-STRPOS(upperright,',')-1))
      upperright_y=FLOAT(STRMID(upperright,STRPOS(upperright,'(')+1,STRPOS(upperright,',')-STRPOS(upperright,'(')-1))
      
      lowerleft_x=FLOAT(STRMID(lowerleft,STRPOS(lowerleft,',')+1,STRPOS(lowerleft,')')-STRPOS(lowerleft,',')-1))
      lowerleft_y=FLOAT(STRMID(lowerleft,STRPOS(lowerleft,'(')+1,STRPOS(lowerleft,',')-STRPOS(lowerleft,'(')-1))
      
      lowerright_x=FLOAT(STRMID(lowerright,STRPOS(lowerright,',')+1,STRPOS(lowerright,')')-STRPOS(lowerright,',')-1))
      lowerright_y=FLOAT(STRMID(lowerright,STRPOS(lowerright,'(')+1,STRPOS(lowerright,',')-STRPOS(lowerright,'(')-1))
      ;ͼ�����ĵ�����
      firstpos=STRPOS(meta,'SCENECENTER')
      lastpos=STRPOS(meta,'SCENECENTER',/REVERSE_SEARCH)
      center_string=STRMID(meta,firstpos,lastpos-firstpos)
      
      ;��ȡ��γ��ֵ,ע��Ԫ��������������(y,x)��ʾ��
      center_x = FLOAT(STRMID(center_string,STRPOS(center_string,',')+1,STRPOS(center_string,')')-STRPOS(center_string,',')-1))
      center_y = FLOAT(STRMID(center_string,STRPOS(center_string,'(')+1,STRPOS(center_string,',')-STRPOS(center_string,'(')-1))
      
      Zone = STRTRIM(STRING(FIX(center_x/6)+31),2)
      ;�ж�aster�����Ǹ�ʡ��,Ҫ���������жϣ�
      ;ʡ����aster�߽��м��ֹ�ϵ��1��asterͼ�������ĳһʡ���ڣ�2��ʡ����asterʡ���ཻ��3��ĳһʡ�������asterͼ��Χ
      
      name='�й���������'
      points=[[upperleft_x,upperleft_y],[upperright_x,upperright_y],[lowerleft_x,lowerleft_y],[lowerright_x,lowerright_y]]
      oROI_1=OBJ_NEW('IDLanROI',[[upperleft_x,upperleft_y],[upperright_x,upperright_y],$
        [lowerleft_x,lowerleft_y],[lowerright_x,lowerright_y],[upperleft_x,upperleft_y]])
      For k =0,n_bound_ent-1 Do Begin
        bound_ent=obound->Getentity(k)
        vert=*(bound_ent.vertices)
        index=oROI_1->ContainsPoints(vert)
        res=WHERE(index Eq 1,num )
        If num Gt 0 Then Begin
          bound_attr=obound->GetAttributes(k)
          temp_name=bound_attr.(6)             ;6����ʡ�����ڵ��ֶ���ţ��������ʹ�ó����ṩ�ı߽����ݣ���Ҫ�����趨�����
          name=[name,temp_name]
        Endif
        oROI = OBJ_NEW('IDLanROI',vert)
        index=oROI->ContainsPoints(points)
        res=WHERE(index Eq 1,num )
        
        If num Gt 0 Then Begin
          bound_attr=obound->GetAttributes(k)
          temp_name=bound_attr.(6)             ;6����ʡ�����ڵ��ֶ���ţ��������ʹ�ó����ṩ�ı߽����ݣ���Ҫ�����趨�����
          name=[name,temp_name]
        Endif
      Endfor
      
      If N_ELEMENTS(name) Gt 1 Then Begin
        name=name[1:*]
        name=name[UNIQ(name,SORT(name))]
        
      Endif 
      
      province_name =''
      For k=0,N_ELEMENTS(name)-1 Do Begin
        if  k eq 0 then province_name=name[k] else $
          province_name=province_name+','+name[k]
      Endfor
      
      
      ;д��shapefile
      
      attr= oshp->GetAttributes(/ATTRIBUTE_STRUCTURE)
      entity.ISHAPE = j
      entity.N_VERTICES=5
      
      entity.bounds=[MIN([upperleft_x,upperright_x,lowerleft_x,lowerright_x],max=max_x),$
        MIN([upperleft_y,upperright_y,lowerleft_y,lowerright_y],max=max_y),0,0,$
        max_x,max_y,0,0]
      pvertice=[upperleft_x,upperleft_y,upperright_x,upperright_y,$
        lowerright_x,lowerright_y,lowerleft_x,lowerleft_y,upperleft_x,upperleft_y]
        
      entity.VERTICES=PTR_NEW(pvertice,/no_copy)
      
      basename=FILE_BASENAME(filelist[i])
      fileinfo=FILE_INFO(filelist[i])
      filesize=STRTRIM(STRING((fileinfo.size)/1024.0/1024.0),2)
      
      attr.(0) = j
      attr.(1) = basename
      attr.(2) = filesize+' Mb'
      attr.(3) = center_x
      attr.(4) = center_y
      attr.(5) = zone
      attr.(6) = province_name
      oshp->PutEntity,entity
      oshp->SetAttributes,j,attr
      j=TEMPORARY(j)+1
    Endelse
  Endfor
  oshp->DestroyEntity, entity
  OBJ_DESTROY, oshp;�ͷŶ���
  OBJ_DESTROY,obound
  FREE_LUN,lun
  print,'=====end====='
End