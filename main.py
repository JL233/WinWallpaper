user='jei88'
wall_dir=r'C:\Users\%s\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'%user
import os
import shutil
new_dir=r'C:\Users\%s\Desktop\wallpaper\\'%user
if __name__ =='__main__':
    print(wall_dir)
    # root 本次walk的根目录绝对路径，str
    # dirs 本次walk的根目录下的文件夹名称集合，是个str的list
    # files 本次walk的根目录下的文件名称集合，是个str的list
    # root本身是文件夹，要循环一次。root下有n个文件夹，则总共循环n+1次。
    # os.path.join(root,dirs[index])获取完整文件夹路径
    # os.path.join(root,files[index])获取完整文件路径
    # os.path.basename(root) 目录的名称
    for root, dirs, files in os.walk(wall_dir):
        for file in files:
            abpath=os.path.join(root,file)
            new_abpath=new_dir+'\\'+file+'.jpg'
            size=os.path.getsize(abpath)
            if size>150*1024:
                print(new_abpath+'大小为：'+str(size/1024))
                shutil.copyfile(abpath,new_abpath)