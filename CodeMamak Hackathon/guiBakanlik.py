# -*- coding: utf-8 -*-

# HoldMyRover takımı tarafından CodeMamak Hackathon'u için oluşturuldu!
# 17.05.2020

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Ui_hastaSorgu(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, hastaSorgu):
        hastaSorgu.setObjectName("hastaSorgu")
        hastaSorgu.resize(903, 847)
        hastaSorgu.setStyleSheet("background:#492fb8;")
        self.label = QtWidgets.QLabel(hastaSorgu)
        self.label.setGeometry(QtCore.QRect(30, 20, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(hastaSorgu)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 811, 51))
        self.lineEdit.setStyleSheet("background:white;\n"
"border-radius:20px;")
        self.lineEdit.setObjectName("lineEdit")
        self.sorgulaBut = QtWidgets.QPushButton(hastaSorgu)
        self.sorgulaBut.setGeometry(QtCore.QRect(730, 70, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.sorgulaBut.setFont(font)
        self.sorgulaBut.setStyleSheet("background:#32cf3c;\n"
"color:white;\n"
"border-radius:20px;")
        self.sorgulaBut.setObjectName("sorgulaBut")
        self.frame = QtWidgets.QFrame(hastaSorgu)
        self.frame.setGeometry(QtCore.QRect(20, 140, 871, 191))
        self.frame.setStyleSheet("border-radius:20px;\n"
"background:#c9aa6f;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.hastalikDurumu = QtWidgets.QLabel(self.frame)
        self.hastalikDurumu.setGeometry(QtCore.QRect(200, 140, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.hastalikDurumu.setFont(font)
        self.hastalikDurumu.setText("")
        self.hastalikDurumu.setObjectName("hastalikDurumu")
        self.yas = QtWidgets.QLabel(self.frame)
        self.yas.setGeometry(QtCore.QRect(200, 110, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.yas.setFont(font)
        self.yas.setText("")
        self.yas.setObjectName("yas")
        self.cinsiyet = QtWidgets.QLabel(self.frame)
        self.cinsiyet.setGeometry(QtCore.QRect(200, 80, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.cinsiyet.setFont(font)
        self.cinsiyet.setText("")
        self.cinsiyet.setObjectName("cinsiyet")
        self.isimSoyisim = QtWidgets.QLabel(self.frame)
        self.isimSoyisim.setGeometry(QtCore.QRect(200, 50, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.isimSoyisim.setFont(font)
        self.isimSoyisim.setText("")
        self.isimSoyisim.setObjectName("isimSoyisim")
        self.tablo = QtWidgets.QTableWidget(hastaSorgu)
        self.tablo.setGeometry(QtCore.QRect(20, 350, 871, 481))
        self.tablo.setStyleSheet("background:white;")
        self.tablo.setObjectName("tablo")
        self.tablo.setColumnCount(4)
        self.tablo.setHorizontalHeaderLabels(["Mekan","Masa","Hareket","Tarih"])
        header = self.tablo.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)



        self.retranslateUi(hastaSorgu)
        QtCore.QMetaObject.connectSlotsByName(hastaSorgu)

    def retranslateUi(self, hastaSorgu):
        _translate = QtCore.QCoreApplication.translate
        hastaSorgu.setWindowTitle(_translate("hastaSorgu", "Hasta Hareketi Sorgu Sistemi"))
        self.label.setText(_translate("hastaSorgu", "Hastanın T.C. kimlik numarasını giriniz"))
        self.sorgulaBut.setText(_translate("hastaSorgu", "Sorgula"))
        self.label_2.setText(_translate("hastaSorgu", "Hasta Bilgileri"))
        self.label_3.setText(_translate("hastaSorgu", "İsim Soyisim:"))
        self.label_4.setText(_translate("hastaSorgu", "Cinsiyet:"))
        self.label_5.setText(_translate("hastaSorgu", "Yaş:"))
        self.label_6.setText(_translate("hastaSorgu", "Hastalık Durumu:"))