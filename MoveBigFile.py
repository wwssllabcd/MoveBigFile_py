# -*- coding: UTF-8 -*-
#coding=utf-8

import os
import shutil
import sys

def move_big_files(src, dst):
    fsizeMb = os.path.getsize(src)/1024/1024
    if fsizeMb > 100:
        print(src.encode("utf-8"))
        try:
            shutil.move(src,  dst)
        except:
            msg = sys.exc_info()
            print("!! Unexpected error:",msg[0], msg[1])
        print ("move " + src)

def get_file_in_fir(fpath, execFun):
    for root, dirs, files in os.walk(fpath):
        if root == fpath:
            continue
        for f in files:
           
            fp = os.path.join(root, f)
            execFun(fp, fpath)
            



FOLDER_PATH = './'
get_file_in_fir(FOLDER_PATH, move_big_files)
print("Finish")
os.system("pause")
