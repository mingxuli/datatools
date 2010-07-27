# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import crawler
import os

class FileTreeView(QTreeView):
    def __init__(self,fileList,parent=None):
        super(FileTreeView,self).__init__(parent)
        self.fileList = fileList

    def mouseDoubleClickEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():            
            path = self.getAbsolutPath(index)
            Crawler = crawler.Crawler(path)
            self.fileList.clear()
            for file in Crawler.files:
                item = QListWidgetItem(file)
                item.setSizeHint(QSize(-1, 22))
                self.fileList.addItem(item)

    def getAbsolutPath(self,index):
        paths = []
        self.getParentPath(index,paths)
        return self.join(paths)
        

    def getParentPath(self,index,paths):
        path = index.data().toString();
        if path.isEmpty(): return;
        paths.append(path)
        self.getParentPath(index.parent(), paths)

    def join(self,paths):
        newPaths=[unicode(path) for path in reversed(paths)]
        return os.path.sep.join(newPaths)
