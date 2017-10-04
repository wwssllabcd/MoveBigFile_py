# -*- coding: UTF-8 -*-

import os
import shutil

def move_big_files(fpath):
    for root, dirs, files in os.walk(fpath):
        if root == fpath:
            continue
        for f in files:
            fp = os.path.join(root, f)
            fsizeMb = os.path.getsize(fp) /1024/1024
            if fsizeMb > 80:
                shutil.move(fp, fpath)
                print ("move " + fp)



FOLDER_PATH = './'
move_big_files(FOLDER_PATH)
print ("Finish")