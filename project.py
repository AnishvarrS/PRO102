import os
import shutil
from_dir= "E:/Whitehatjunior/Module3/C102/NSA"
to_dir= "E:\Whitehatjunior\Module3\C102\NSA"
ListofFiles= os.listdir(from_dir)
for file_name in ListofFiles:
    name, extension = os.path.splitext(file_name)
    if extension == '': 
        continue 
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name
        if os.path.exists(path2):
             print("Moving " + file_name + ".....")
             shutil.move(path1, path3)
        else: 
            os.makedir(path2) 
            print("Moving " + file_name + ".....") 
            shutil.move(path1, path3)
