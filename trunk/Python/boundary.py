#encoding=utf8
import os
import glob
import string
workspace=u'H:\\test\\'
dirlist=os.listdir(workspace)


for folder in dirlist:
    files=glob.glob(workspace+folder+'/*.KZB')
    
    
    for filename in files:
        print filename
        RZB_file=string.replace(filename,'KZB','RZB')
        outfile=u'H:\\test\\'+os.path.basename(string.replace(filename,'KZB','txt'))
        f1=open(outfile,'w')
        f=open(RZB_file)
        lines=f.readlines()
        for line in lines:
            text=string.split(line)
            if len(text)==6:
                shift_x=float(text[1])
                shift_y=float(text[2])
        print shift_x,shift_y
        f.close()
        f=open(filename)
        lines=f.readlines()
        i=0        
        for line in lines:
            if i >3:
                word=string.split(line)
                if word[0]=='L' and len(word[0])==1:
                    record_1=i
                    record=int(word[1])
                if word[0]=='A' and len(word[0])==1:
                    record_2=i
            i=i+1
        data=lines[record_1+1:record_2]
        rec=0
        
        for i in range(record):
            header=string.split(data[rec])
            point_id=int(header[0])
            f1.write(str(point_id)+'\n')
            point_count=int(header[1])
            rec=rec+1
            coor=string.split(data[rec])
            count=0
            while len(coor)<2*point_count:
                rec=rec+1
                coor=coor+string.split(data[rec])                
            
            for k in range(point_count):                
                point_x=float(coor[2*k])
                point_y=float(coor[2*k+1])
                f1.write(str(shift_x+point_x)+','+str(shift_y+point_y)+'\n')
           
            
            rec=rec+1
            f1.write('end\n')
            
        f.close()
            
        f1.write('end\n')
        f1.close()        
print 'end'

                
