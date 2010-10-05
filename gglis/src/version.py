#! /usr/bin/env python
#coding=utf-8
import sys
import os

def  homeDir():
    path = sys.path[0]
    if os.path.isdir(path):        
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def detectHDem():
    drivers = ('c:\\','d:\\','e:\\','f:\\','g:\\','h:\\','i:\\','g:\\','k:\\','l:\\','m:\\')
    for d in drivers:
        file=os.path.join(d,'hkh','background_h.tif')
        if os.path.isfile(file):
            return file
        else:
            return None

DEFAULT_DATABASE=homeDir()+"\\data"+"\\db.sqlite"
DEFAULT_IMAGE=homeDir()+"\\data"+"\\background.tif"
DEFAULT_LAYERS=('glacial_lake','major_river','study_area','basin_boundary')
LAYERS=('glacial_lake','major_river','study_area','basin_boundary','background')
resolution = 6000000

if __name__=='__main__':
    print detectDem()
