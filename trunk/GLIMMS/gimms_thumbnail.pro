;本程序需要在ENVI环境下运行
pro gimms_thumbnail
	compile_opt strictarr                 ;可避免编译器不能识别ENVI函数
	envi, /restore_base_save_files        ;恢复ENVI sav文件
  envi_batch_init, log_file='batch.txt' ;开始批处理模式
	inpath='D:\Gimms\output1'
	outpath='d:\Gimms\thumbnail\'
	CD,inpath
  Foldlist=file_search('*',/TEST_DIRECTORY,/FULLY_QUALIFY_PATH,count=num_folder);搜索文件夹
  FOR i=0,num_folder-1 DO BEGIN
		cd,Foldlist[i]
    filelist=file_search('*.img',count=n)   ;获取图像文件名称
		FOR j=0,n-1 DO BEGIN
			filename=foldlist[i]+'\'+filelist[j]
			envi_open_file, filename, r_fid=fid
      if (fid eq -1) then begin
        envi_batch_exit
        return
      endif
   	 	envi_file_query, fid, ns=ns, nl=nl, nb=nb
    	dims = [-1, 0, ns-1, 0, nl-1]
   		pos  = lindgen(nb)
			data = ENVI_GET_DATA(fid=fid,dims=dims,pos=pos)
			filename1=outpath+filelist[j]+'.jpg'
			;
			mydevice=!D.NAME
			SET_PLOT, 'Z'
			DEVICE,SET_RESOLUTION=[ns,nl],Z_BUFFERING=0,SET_FONT='Times Bold',SET_CHARACTER_SIZE=[10,15]
			Erase,color=255
			map_set,limit=[15,70,55,140],title=filelist[j]+'!C',$
			        xmargin=[3,3],ymargin=[3,5] ;设置显示范围
			image=map_image(data,x0,y0,xsize,ysize,latmin=15,lonmin=70,latmax=55,lonmax=140,compress=1)
			tv,image,x0,y0,xsize=xsize,ysize=ysize,order=1
			map_continents,/countries,/coasts
			map_grid,/box
			nanhaifile='D:\DataTools\GLIMMS\nanhai.img'
 			envi_open_file, nanhaifile, r_fid=fid
 			envi_file_query,fid, ns=ns, nl=nl, nb=nb
    	dims = [-1, 0, ns-1, 0, nl-1]
   		pos  = lindgen(nb)
			nanhai_data = ENVI_GET_DATA(fid=fid,dims=dims,pos=pos)
			nanhai_image=map_image(nanhai_data,x0,y0,xsize,ysize,latmin=15,lonmin=140-(15*0.8),latmax=30,lonmax=140,compress=1)
			tv,nanhai_image,x0,y0,xsize=xsize,ysize=ysize,order=1
			xyouts,70,11,'Environmental and Ecological Science Data Center For West China      (http://westdc.westgis.ac.cn)';,color=1,charsize=1;,CHARTHICK=2
			TVImage=TVRD()

			DEVICE, /CLOSE
			SET_PLOT, mydevice
			;输出缩略图
			WRITE_JPEG, filename1, TVImage, ORDER=0
		ENDFOR
	ENDFOR
	envi_batch_exit     ;退出批处理模式
end