;
; IDL Event Callback Procedures
; GIMMS_TOOLS_eventcb
;
; Generated on:	03/23/2008 19:38.03
;
;
; Empty stub procedure used for autoloading.;

;������ʼ��
pro InitShow, wWidget

	Boundary_id=Widget_Info(wWidget, FIND_BY_UNAME='Boundary_DROPLIST')
	OutFormate_id=Widget_Info(wWidget,Find_By_UName='OutFormate_DROPLIST')
	Message_id=Widget_Info(wWidget,Find_By_UName='Message_TEXT')

	Boundary=['�й�������������������ר�ã�','�ں�����','�Զ���']
	Widget_Control,Boundary_id,set_value=Boundary
	Formate=['ENVI (.img)','Geo TIFF','ESRI GRID','ESRI ASCII','ERDAS IMAGE']
	Widget_Control,OutFormate_id,set_value=Formate
	MessageText=['�汾:2.0'+string(13b),$
	            '����:2008-3-25'+string(13b),$
	            '����:Wulizong'+string(13b),$
	            'Email:wulizong@lzb.ac.cn'+string(13b),$
	            '��λ:�й���ѧԺ�������������빤���о���'+string(13b),$
	            '��ַ:����ʡ�����ж�����·320��'+string(13b),$
	            '�ʱ�:730000'+string(13b),$
	            '�绰:0931-4967298'+string(13b),$
	            '��л:�������ܵ�����ί������̬�����������ĺ͵���ϵͳ��ѧ�������ĵ���������'+string(13b),$
	            '����ʹ��˵��:'+string(13b),$
	            '1.��������Ҫ����ENVI�ĺ���,��ȷ�ϼ�������Ѿ���װ��ENVI.'+string(13b),$
	            '2.���ݵ�������Ŀ¼��ʽΪ:'+string(13b),$
	            '    ���Ŀ¼/'+string(13b),$
	            '            1981/'+string(13b),$
	            '            1982/'+string(13b),$
	            '            ..../'+string(13b),$
	            '*****�����޸���ʷ***********'+string(13b),$
	            'v2,0 2008-3-25 �����޸�Ϊ����'+string(13b),$
              'v1.1 2008-3-16 ������ڴ�Gimms FTPվ�������ص�ԭʼ���������еģ������Զ���ѹ����Ȼ�����и������������������ݸ�ʽ'+string(13b),$
              'v1.0 2007-8-1  �����Ѿ�ת���õ�ENVI��ʽ��ȫ�����ݽ����и�ģ����ܶ�������ʽ�����ݽ��ж�ȡ']

	Widget_Control,Message_id,set_value=messageText
  ;����ȫ�ֱ���
  out_message=['---�������---'+string(13b),'','','','','']
  bound={north:0.0,south:0.0,west:0.0,east:0.0}
  help,out_message
  info={bound_Type:'',bound:bound,inpath:'',outpath:'',OutFormate:'',$
        out_message:out_message}
  pinfo=ptr_new(info,/No_Copy)
  Widget_Control,wWidget,set_uvalue=pinfo
end
;-------ѡ����������Ŀ¼----------------------
pro OpenGIMMS, Event
	wWidget =  Event.top
  Widget_Control,wWidget,get_Uvalue=pinfo

	Message_id=Widget_Info(wWidget,Find_By_UName='Message_TEXT')
	FilePath_id=Widget_Info(wWidget,Find_By_UName='FilePath_TEXT')
   Workspace=DIALOG_PICKFILE(/DIRECTORY)
   filelist=File_Search(Workspace,'*.gz',count=count)

   Out_Message='Ŀ¼�й���*.gz��ʽ���ļ�'+strtrim(string(count),2)+'��'

   (*pinfo).Out_Message[1]=Out_message+string(13b)
   Widget_Control,FilePath_id,set_value=workspace
   Widget_Control,Message_id,set_value=(*pinfo).Out_Message
   (*pinfo).inpath=workspace

end

;-----------------------------------------------------------------
;�����иΧ
pro Set_Boundary, Event
  wWidget =  Event.top
  Widget_Control,wWidget,get_Uvalue=pinfo

  Message_id=Widget_Info(wWidget,Find_By_UName='Message_TEXT')

  Boundary_id=Widget_Info(wWidget, FIND_BY_UNAME='Boundary_DROPLIST')
  North_id=Widget_Info(wWidget, FIND_BY_UNAME='North_TEXT')
  South_id=Widget_Info(wWidget, FIND_BY_UNAME='South_TEXT')
  West_id=Widget_Info(wWidget, FIND_BY_UNAME='West_TEXT')
  East_id=Widget_Info(wWidget, FIND_BY_UNAME='East_TEXT')
  index=widget_info(Boundary_id,/DROPLIST_SELECT)
  widget_control,Boundary_id,get_value=bound_type
  (*pinfo).bound_Type=bound_type[index]
  case index of
  0:begin
  widget_Control,North_id,set_value='45',Editable=0
  widget_Control,South_id,set_value='15',Editable=0
  widget_Control,West_id,set_value='70',Editable=0
  widget_Control,East_id,set_value='140',Editable=0

	(*pinfo).bound.north=45.0
	(*pinfo).bound.south=15.0
	(*pinfo).bound.west=70.0
	(*pinfo).bound.east=140.0
	(*pinfo).Out_Message[2]='��ѡ����иΧ���й�����'+string(13b)
  end
  1:begin
  widget_Control,North_id,set_value='41',Editable=0
  widget_Control,South_id,set_value='38',Editable=0
  widget_Control,West_id,set_value='99',Editable=0
  widget_Control,East_id,set_value='102',Editable=0

	(*pinfo).bound.north=41.0
	(*pinfo).bound.south=38.0
	(*pinfo).bound.west=99.0
	(*pinfo).bound.east=102.0
	(*pinfo).Out_Message[2]='��ѡ����иΧ�Ǻں�����'+string(13b)
  end
  2:begin
  widget_Control,North_id,set_value='', EDITABLE=1
  widget_Control,South_id,set_value='', EDITABLE=1
  widget_Control,West_id,set_value='', EDITABLE=1
  widget_Control,East_id,set_value='', EDITABLE=1
  (*pinfo).Out_Message[2]='��ѡ����иΧ���Զ�������'+string(13b)
  end
  endcase
  Widget_Control,Message_id,set_value=(*pinfo).Out_Message
end


;-----------------------------------------------------------------
;���������ʽ
pro Set_OutFormate, Event
   wWidget =  Event.top
   Widget_Control,wWidget,get_Uvalue=pinfo

	 OutFormate_id=Widget_Info(wWidget,Find_By_UName='OutFormate_DROPLIST')
   Message_id=Widget_Info(wWidget,Find_By_UName='Message_TEXT')

   index=Widget_Info(OutFormate_id,/DROPLIST_SELECT)
   widget_control,OutFormate_id,get_value=OutFormate

   (*pinfo).OutFormate=OutFormate[index]
   (*pinfo).Out_Message[3]='��ѡ��������ʽΪ '+OutFormate[index]+string(13b)
   Widget_Control,Message_id,set_value=(*pinfo).Out_Message
end
;�������·��
pro Set_Outpath, Event
   wWidget =  Event.top
   Widget_Control,wWidget,get_Uvalue=pinfo

	 OutPath_id=Widget_Info(wWidget,Find_By_UName='OutPath_TEXT')
	 Message_id=Widget_Info(wWidget,Find_By_UName='Message_TEXT')
   Outpath=DIALOG_PICKFILE(/DIRECTORY)


   Widget_Control,OutPath_id,set_value=OutPath
   (*pinfo).Out_Message[4]='���·��Ϊ '+Outpath+string(13b)
   (*pinfo).outpath=Outpath
   Widget_Control,Message_id,set_value=(*pinfo).Out_Message
end


;-----------------------------------------------------------------
pro Run, Event
  Compile_opt strictarr

  wWidget =  Event.top
  Widget_Control,wWidget,get_uValue=pinfo


	Message_id=Widget_Info(wWidget,Find_By_UName='Message_TEXT')

  info=*pinfo
  if info.bound_Type eq '�Զ���' then begin
  	North_id=Widget_Info(wWidget, FIND_BY_UNAME='North_TEXT')
  	South_id=Widget_Info(wWidget, FIND_BY_UNAME='South_TEXT')
  	West_id=Widget_Info(wWidget, FIND_BY_UNAME='West_TEXT')
  	East_id=Widget_Info(wWidget, FIND_BY_UNAME='East_TEXT')
  	Widget_Control,North_id,Get_value=north_str
  	Widget_Control,South_id,Get_value=south_str
  	Widget_Control,West_id,Get_value=west_str
  	Widget_Control,East_id,Get_value=east_str

  	(*pinfo).bound.north=float(north_str)
  	(*pinfo).bound.south=float(south_str)
  	(*pinfo).bound.west=float(west_str)
  	(*pinfo).bound.east=float(east_str)
  endif
  if info.inpath eq '' then begin
    Widget_Control,Message_id,set_value='û����������·��!'
    return
  endif
  if info.bound_Type eq '' then begin
    Widget_Control,Message_id,set_value='û�������иΧ!'
    return
  endif
  if info.outformate eq '' then begin
  	Widget_Control,Message_id,set_value='û�����������ʽ!'
    return
  endif
  if info.outpath eq '' then begin
  	Widget_Control,Message_id,set_value='û���������·��!'
    return
  endif
  ;�����������·��
  Filelist=File_Search(info.inpath,'*.gz',count=count)
  Year_str=strmid(file_basename(Filelist),0,2)
  Year_index = Year_str[UNIQ(Year_str, SORT(Year_str))]
  For i=0,n_elements(Year_index)-1 do begin
     if strmid(Year_index[i],0,1) eq '0' then begin
     File_MKDir,info.outPath+'20'+Year_index[i]
     endif else begin
     File_MKDir,info.outPath+'19'+Year_index[i]
     endelse
  Endfor




;	;��ʼENVI������ģʽ
;  envi, /restore_base_save_files
;  envi_batch_init, log_file='batch.txt'
;
;  ;�Ƴ�������ģʽ
;	envi_batch_exit     ;�˳�������ģʽ
end



pro Cancle, Event
  wWidget =  Event.top
end
