import glob
from shutil import copy2
#Instructions:
# 1- Input Files Folder Name Should be Input
# 2- Output Files Folder Name Should be Output

#Balsam, Fraser, Canaan
path =r'/tempdata3/fasket/Xmas/usearch90_cluster_dir/*' #copyPaste inputFolder Address HERE
files=glob.glob(path)
fwSingle=open(r"/tempdata3/adeel/SingleSeparateFile",'a') #Enter Output Folder Name with address Single File Name (File that have all combined data)

for file in files:
    flag, flag1,flag2=0,0,0
    data=[]
    fileName=file.split("\\")[-1]
    for line in open(file):
        if line.startswith(">Balsam"):
            data.append(line.replace("\n", "")+" "+fileName+"\n")
            flag=1
        elif line.startswith(">Fraser"):
            data.append(line.replace("\n", "")+" "+fileName+"\n")
            flag1=1
        elif line.startswith(">Canaan"):
            data.append(line.replace("\n", "")+" "+fileName+"\n")
            flag2=1
        else:
            data.append(line)
    
    if flag==1 and flag1==1 and flag2==1:
        open("/tempdata3/adeel/"+fileName."a")
        for line in data:
            if line.startswith(">"):
                fw.write(line.split()[0]+"\n")
            else:
                fw.write(line)
            fwSingle.write(line)
        fw.close()
  
fwSingle.close()       
    
