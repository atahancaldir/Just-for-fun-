# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'masaSecimEkrani.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_masaSecimEkrani(object):
    def setupUi(self, masaSecimEkrani):
        masaSecimEkrani.setObjectName("masaSecimEkrani")
        masaSecimEkrani.resize(760, 815)
        masaSecimEkrani.setMinimumSize(QtCore.QSize(760, 815))
        masaSecimEkrani.setMaximumSize(QtCore.QSize(760, 815))
        masaSecimEkrani.setStyleSheet("background:#492fb8;")
        self.lineEdit = QtWidgets.QLineEdit(masaSecimEkrani)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 421, 41))
        self.lineEdit.setStyleSheet("background:white;\n"
"border-radius:20px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(masaSecimEkrani)
        self.label.setGeometry(QtCore.QRect(50, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(masaSecimEkrani)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:#32cf3c;\n"
"color:white;\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.cafeFrame = QtWidgets.QFrame(masaSecimEkrani)
        self.cafeFrame.setGeometry(QtCore.QRect(30, 260, 701, 541))
        self.cafeFrame.setStyleSheet("background:white;")
        self.cafeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cafeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cafeFrame.setObjectName("cafeFrame")
        self.masa1 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa1.setGeometry(QtCore.QRect(40, 50, 131, 71))
        self.masa1.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa1.setObjectName("masa1")
        self.label_3 = QtWidgets.QLabel(self.cafeFrame)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 21, 131))
        self.label_3.setStyleSheet("background:#67baea;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.cafeFrame)
        self.label_4.setGeometry(QtCore.QRect(50, 340, 31, 17))
        self.label_4.setObjectName("label_4")
        self.masa5 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa5.setGeometry(QtCore.QRect(40, 160, 131, 71))
        self.masa5.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa5.setObjectName("masa5")
        self.masa2 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa2.setGeometry(QtCore.QRect(210, 50, 131, 71))
        self.masa2.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa2.setObjectName("masa2")
        self.masa6 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa6.setGeometry(QtCore.QRect(210, 160, 131, 71))
        self.masa6.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa6.setObjectName("masa6")
        self.masa4 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa4.setGeometry(QtCore.QRect(540, 50, 131, 71))
        self.masa4.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa4.setObjectName("masa4")
        self.masa9 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa9.setGeometry(QtCore.QRect(390, 370, 131, 71))
        self.masa9.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa9.setObjectName("masa9")
        self.masa11 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa11.setGeometry(QtCore.QRect(390, 460, 131, 71))
        self.masa11.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa11.setObjectName("masa11")
        self.label_5 = QtWidgets.QLabel(self.cafeFrame)
        self.label_5.setGeometry(QtCore.QRect(70, 430, 281, 91))
        self.label_5.setStyleSheet("background:#67baea;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.masa3 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa3.setGeometry(QtCore.QRect(390, 50, 131, 71))
        self.masa3.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa3.setObjectName("masa3")
        self.masa7 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa7.setGeometry(QtCore.QRect(390, 160, 131, 71))
        self.masa7.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa7.setObjectName("masa7")
        self.masa10 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa10.setGeometry(QtCore.QRect(540, 370, 131, 71))
        self.masa10.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa10.setObjectName("masa10")
        self.masa12 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa12.setGeometry(QtCore.QRect(540, 460, 131, 71))
        self.masa12.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa12.setObjectName("masa12")
        self.label_6 = QtWidgets.QLabel(self.cafeFrame)
        self.label_6.setGeometry(QtCore.QRect(651, 250, 20, 91))
        self.label_6.setStyleSheet("background:#67baea;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.cafeFrame)
        self.label_2.setGeometry(QtCore.QRect(590, 280, 51, 17))
        self.label_2.setObjectName("label_2")
        self.masa8 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa8.setGeometry(QtCore.QRect(540, 160, 131, 71))
        self.masa8.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa8.setObjectName("masa8")
        self.label_8 = QtWidgets.QLabel(self.cafeFrame)
        self.label_8.setGeometry(QtCore.QRect(196, 410, 41, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(masaSecimEkrani)
        self.label_7.setGeometry(QtCore.QRect(550, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(masaSecimEkrani)
        self.label_9.setGeometry(QtCore.QRect(190, 210, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Lohit Punjabi")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:black;")
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(masaSecimEkrani)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 70, 125, 125))
        self.pushButton_2.setStyleSheet("background:white;\n"
"border-radius:60px;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("temassizresim.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(207, 207))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(masaSecimEkrani)
        QtCore.QMetaObject.connectSlotsByName(masaSecimEkrani)

    def retranslateUi(self, masaSecimEkrani):
        _translate = QtCore.QCoreApplication.translate
        masaSecimEkrani.setWindowTitle(_translate("masaSecimEkrani", "Masa Seçim Ekranı"))
        self.label.setText(_translate("masaSecimEkrani", "Lütfen T.C. Kimlik Numaranızı giriniz"))
        self.pushButton.setText(_translate("masaSecimEkrani", "Giriş yap!"))
        self.masa1.setText(_translate("masaSecimEkrani", "Masa 1"))
        self.label_4.setText(_translate("masaSecimEkrani", "Giriş"))
        self.masa5.setText(_translate("masaSecimEkrani", "Masa 5"))
        self.masa2.setText(_translate("masaSecimEkrani", "Masa 2"))
        self.masa6.setText(_translate("masaSecimEkrani", "Masa 6"))
        self.masa4.setText(_translate("masaSecimEkrani", "Masa 4"))
        self.masa9.setText(_translate("masaSecimEkrani", "Masa 9"))
        self.masa11.setText(_translate("masaSecimEkrani", "Masa 11"))
        self.masa3.setText(_translate("masaSecimEkrani", "Masa 3"))
        self.masa7.setText(_translate("masaSecimEkrani", "Masa 7"))
        self.masa10.setText(_translate("masaSecimEkrani", "Masa 10"))
        self.masa12.setText(_translate("masaSecimEkrani", "Masa 12"))
        self.label_2.setText(_translate("masaSecimEkrani", "Lavabo"))
        self.masa8.setText(_translate("masaSecimEkrani", "Masa 8"))
        self.label_8.setText(_translate("masaSecimEkrani", "Kasa"))
        self.label_7.setText(_translate("masaSecimEkrani", "Temassız giriş"))
        self.label_9.setText(_translate("masaSecimEkrani", "Lütfen oturmak istediğiniz masayı seçiniz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    masaSecimEkrani = QtWidgets.QWidget()
    ui = Ui_masaSecimEkrani()
    ui.setupUi(masaSecimEkrani)
    masaSecimEkrani.show()
    sys.exit(app.exec_())

