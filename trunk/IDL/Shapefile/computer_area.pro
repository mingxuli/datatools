;*******************************************************************************
;* ����:������
;* ��λ���й���ѧԺ�������������빤���о���
;* E-mail:wulizong at lzb.ac.cn
;* �������ڣ�2008-
;* ������¼�¼��
;*
;* ����������
;*     ���������ڣ��ھ�γ��ͶӰ�¼������ε����
;********************************************************************************


Pro Computer_Area
  shapefile='D:\��ͼ��\10���ͼ��.shp'  ;��Ҫ�����shapefile�ļ�
  out_shapefile='D:\test\world.shp'               ;����ļ�
  Area_Fieldname='new_area'                       ;�洢������ֶ����ƣ�ע�����ԭ�е��ֶ������ظ�
  Precision=4                                     ;������ȣ���С�����λ����
  
  ;��ȡԭʼ��shapefile�ļ�
  oshp=OBJ_NEW('IDLffShape',shapefile)
  ;��ȡ����
  oshp->GetProperty,N_Entities=n_ent,n_attributes=n_attr,ENTITY_TYPE=ent_type,attribute_info=attr_info
  If ent_type Ne 5 Then Begin
    PRINT,'���������������������ļ����Ƕ����ʵ�壬����������ݣ�'
    RETURN
  Endif
  
  ; �����µ�shapefile�ļ�
  new_shp=OBJ_NEW('IDLffShape',out_shapefile,entity_type=ent_type,/update)
  ;Ϊ����ļ���������
  new_shp->AddAttribute,Area_Fieldname,5,16,Precision=precision      ;����ֶΣ�16λ��ȣ�
  For i=0,n_attr-1 Do Begin
    new_shp->AddAttribute, (attr_info.name)[i],(attr_info.type)[i],$
      (attr_info.width)[i],Precision=(attr_info.Precision)[i]      ;����ԭ���ֶ�
  Endfor
  
  
  Albers=MAP_PROJ_INIT('Albers Equal Area',$
    SEMIMAJOR_AXIS=6378245.0 ,SEMIMINOR_AXIS=6356863.0188,$
    STANDARD_PAR1=25.0,STANDARD_PAR2=47.0,$
    CENTER_LATITUDE=0.0,CENTER_LONGITUDE=105.0,$
    FALSE_EASTING=0.0, FALSE_NORTHING=0.0,/GCTP)
    
    
    
    
    
  new_ent = {IDL_SHAPE_ENTITY}
  new_ent.Shape_Type=5
  
  For i=0,n_ent-1 Do Begin
    ent=oshp->getentity(i)
    attr=oshp->getattributes(i)
    vert=*(ent.vertices)
    new_vert=MAP_PROJ_FORWARD(vert,map_structure=albers)
    
    ;����ͼ��
    new_ent.Ishape=i
    new_ent.bounds=[MIN(new_vert[0,*]),MIN(new_vert[1,*]),0,0,MAX(new_vert[0,*]),MAX(new_vert[1,*]),0,0]
    new_ent.n_vertices=ent.n_vertices
    new_ent.vertices=PTR_NEW(new_vert)
    
    new_ent.n_parts=ent.n_parts
    new_ent.parts=ent.parts
    new_ent.part_types=ent.part_types
    
   
    ;�������       
    ROI=Obj_new('IDLanROI',new_vert)
    result=ROI->ComputeGeometry(Area=area,Centroid=Center_xy)
     ;д��ͼ��
    new_shp->putEntity,new_ent
    ;��������
    new_attr=new_shp->GetAttributes(/ATTRIBUTE_STRUCTURE)
    
    ;д������
    
    new_attr.(0)=area    ;���Գ���1000000
    for index=1,n_attr do begin
    new_attr.(index)=attr.(index-1)
    endfor
    
    new_shp->setAttributes,i,new_attr
    
    oshp->DestroyEntity,ent
    obj_destroy,roi
  Endfor
  new_shp->DestroyEntity,new_ent
  
  OBJ_DESTROY, new_shp
  OBJ_DESTROY, oshp
  
  PRINT,'end'
  
  
  
End
