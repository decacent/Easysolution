# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:07:33 2017

@author: wnight
"""

from main_ui import *
import  sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class Solulation(QMainWindow,Ui_mainWindow):
    def __init__(self, parent=None):
        super(Solulation, self).__init__(parent)
        self.setupUi(self)
        self.co=[1,1e-3,1e-6,1e-9]


        self.pushButton.clicked.connect(self.cacl1)


    def re_init(self):
        self.m=self.doubleSpinBox.value()*self.co[self.comboBox.currentIndex()]
        self.v=self.doubleSpinBox_2.value()*self.co[self.comboBox_2.currentIndex()]
        self.c=self.doubleSpinBox_3.value()*self.co[self.comboBox_3.currentIndex()]
        self.mr=self.doubleSpinBox_4.value()

    def cacl1(self):
        try:
            self.re_init()
            s=[self.m,self.v,self.c,self.mr]
            r=s.index(0.0)
            if r == 0:
                self.m = self.c * self.v * self.mr
                self.doubleSpinBox.setValue(self.m/self.co[self.comboBox.currentIndex()])
            elif r == 1:
                self.v = self.m / self.mr / self.c
                self.doubleSpinBox_2.setValue(self.v/self.co[self.comboBox_2.currentIndex()])
            elif r == 2:
                self.c = self.m / self.mr / self.v
                self.doubleSpinBox_3.setValue(self.c/self.co[self.comboBox_3.currentIndex()])
            else:
                pass
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Solulation()
    mainWindow.show()
    sys.exit(app.exec_())
