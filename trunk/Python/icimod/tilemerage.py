##Tilemerage.py
import string
import glob
import os
workspace='F:\\website\\data_dir\\geocover\\geocover_2k\\'
outpath='F:\\temp_outpath\\'
result=os.walk(workspace)
basename=[]
path_list=[]
fullname=[]
shortname=[]
for folder,sub_folder,filelist in result:
    path_list.append(folder)
    short_folder=string.replace(folder,workspace,'')
    short_folder=string.split(short_folder,'\\')
    short_folder=string.join(short_folder[1:len(short_folder)],'\\')+'\\'
    for filename in filelist:        
        fullname.append(folder+'\\'+filename)        
        shortname.append(filename)
        basename.append(short_folder+filename)
print len(basename),len(set(basename))

for path in sorted(set(path_list)):
        path=string.replace(path,workspace,'')
        path=string.split(path,'\\')
        path=path[1:len(path)]
        outdir=outpath+string.join(path,'\\')        
        if os.path.exists(outdir)is not True:
            os.mkdir(outdir)


for name in sorted(set(basename)):
    fix=name[-3:len(name)]
    if fix=='png':
        filelist=[]
        for i in range(len(basename)):
            filename=basename[i]
            if filename ==name:
                filelist.append(fullname[i])
        path=filelist[0]
        kmlfile=string.replace(path,'png','kml')
        path=string.replace(path,workspace,'')
        path=string.split(path,'\\')
        path=path[1:len(path)]
        outfile=outpath+name        
        outfile_tif=string.replace(outfile,'png','tif')
        
        filelist=string.join(filelist,' ')
        cmd_str='c:\\python26\\python.exe c:\\gdalwin32-1.6\\bin\\gdal_merge.py -o '+outfile_tif+' -n 0 '+filelist
        os.system(cmd_str)
        cmd_str1='c:\\gdalwin32-1.6\\bin\\gdal_translate -of PNG '+outfile_tif+' '+outfile
        print outfile
        os.system(cmd_str1)
        os.system('del '+outfile_tif)
        os.system('copy '+kmlfile+' '+string.replace(outfile,'png','kml'))
  
        
    
print '-----------end----------------'
                        
    
