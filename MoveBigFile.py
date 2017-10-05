# -*- coding: UTF-8 -*-
#coding=utf-8

import os
import shutil

def move_big_files(src, dst):
    fsizeMb = os.path.getsize(src)/1024/1024
    if fsizeMb > 80:
        shutil.move(src,  dst)
        print ("move " + src)

def move_big_files(fpath, execFun):
    for root, dirs, files in os.walk(fpath):
        if root == fpath:
            continue
        for f in files:
            fp = os.path.join(root, f)
            execFun(fp, fpath)
            



FOLDER_PATH = './'
move_big_files(FOLDER_PATH, move_big_files)
print ("Finish")