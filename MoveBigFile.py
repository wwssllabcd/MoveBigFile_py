#-*- coding: utf-8 -*-　
import os
import shutil



def move_big_files(fpath):
    """Docstring"""
    # dirPath: 目前走訪的目錄
    # dirs: 該path所包含的所有的目錄
    # files: 該path 所包含的檔案
    # os.walk: 會從起始位置往下走訪每個dirPath
    for dirPath, dirs, files in os.walk(fpath):
        if dirPath == fpath:
            continue
        for f in files:
            fp = dirPath + "/" + f
            fsizeMb = os.path.getsize(fp) / 1024 / 1024
            if fsizeMb > 80:
                shutil.move(fp, fpath)
                print "move " + fp

    


FOLDER_PATH = './'
move_big_files(FOLDER_PATH)
print "Finish"