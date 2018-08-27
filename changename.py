import os

document = '/media/gzd/本地磁盘L/PHOTO/美帝生活/越野马拉松向日葵/New folder'
os.chdir(document)
for pic in os.listdir(document):
    num = int(pic[4:8])
    new_num = num + 160
    new_name = pic[0:4] + str(new_num) + pic[8:]
    path_old = os.path.relpath(pic, start=document)
    path_new = os.path.relpath(new_name, start=document)
    os.rename(path_old, path_new)