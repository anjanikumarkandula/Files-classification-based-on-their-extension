import os
import shutil
print("------------welcome to the file classifier-----------------------------")
print("----------our expert system needs the raw files that you need to classify----------")
path=os.getcwd()
names=os.listdir(path)
folder=['image','python','shell','java','c','pdf','docu','os']
for x in range(0,8):
    if not os.path.exists(path+folder[x]):
           os.makedirs(path+folder[x])
for files in names:
    if ".png" in files and not os.path.exists(path+'image/'+files):
         shutil.move(path+files,path+'image/'+files)
    if ".py" in files and not os.path.exists(path+'python/'+files):
         shutil.move(path+files,path+'python/'+files)
    if ".cpp" in files and not os.path.exists(path+'shell/'+files):
         shutil.move(path+files,path+'shell/'+files)
    if ".java" in files and not os.path.exists(path+'java/'+files):
         shutil.move(path+files,path+'java/'+files)
    if ".c" in files and not os.path.exists(path+'c/'+files):
         shutil.move(path+files,path+'c/'+files)
    if ".pdf" in files and not os.path.exists(path+'pdf/'+files):
         shutil.move(path+files,path+'pdf/'+files)
    if ".docx" in files and not os.path.exists(path+'docu/'+files):
         shutil.move(path+files,path+'docu/'+files)
    if ".pptx" in files and not os.path.exists(path+'os/'+files):
         shutil.move(path+files,path+'os/'+files)
print("please check your specified directory")
print("------------------------------------")
print("------ ARE YOU SATISFIED FOR THE CLASSIFICATION ----------------------")
