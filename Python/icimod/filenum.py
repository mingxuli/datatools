## file number
import glob
import string

workspace_1=u"F:\\Himalaya_Lakes\\images\\Landsat_B543\\"
workspace_2=u"H:\\Himalaya_lake\\data\\unziped\\"
filelist=glob.glob(workspace_1+"*.tif")
folderlist=glob.glob(workspace_2+"*")
path1=[]
path2=[]
for filename in filelist:
    filename=string.split(filename,"\\")
    filename=filename[4]
    gid=filename[0:2]
    if gid=='L5':
        path=filename[2:8]
        path1.append(path)
    if gid=='L7':
        path=filename[3:9]
        path1.append(path)
    
for folder in folderlist:
    folder=string.split(folder,"\\")
    folder=folder[4]
    path=folder[3:9]
    path2.append(path)

for path in set(path2):
    if path1.count(path)<>path2.count(path):
        print path,path1.count(path),path2.count(path)

print 'total path:'
print len(set(path1)),len(set(path2))
    

