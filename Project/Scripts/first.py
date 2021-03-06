# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 307)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #929294;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color:#fff;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"color: #fff;\n"
"font: 17pt \"Mongolian Baiti\";\n"
"}")
        self.label.setObjectName("label")
        self.Key = QtWidgets.QPushButton(self.centralwidget)
        self.Key.setGeometry(QtCore.QRect(10, 140, 91, 31))
        self.Key.setAccessibleDescription("")
        self.Key.setAutoFillBackground(False)
        self.Key.setStyleSheet("QPushButton {\n"
"    background-color: #ceced9;\n"
"    font: 8pt \"Poor Richard\";\n"
"    border: 1px solid gray;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #acadb0;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #d4d4d6;\n"
"} \n"
"")
        self.Key.setFlat(False)
        self.Key.setObjectName("Key")
        self.Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.Encrypt.setGeometry(QtCore.QRect(10, 190, 131, 31))
        self.Encrypt.setMouseTracking(False)
        self.Encrypt.setStyleSheet("QPushButton {\n"
"    background-color: #ceced9;\n"
"    font: 8pt \"Poor Richard\";\n"
"    border: 1px solid gray;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #acadb0;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #d4d4d6;\n"
"} \n"
"")
        self.Encrypt.setCheckable(False)
        self.Encrypt.setObjectName("Encrypt")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 131, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #ceced9;\n"
"    font: 8pt \"Poor Richard\";\n"
"    border: 1px solid gray;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #acadb0;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #d4d4d6;\n"
"} \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 260, 161, 31))
        self.label_2.setStyleSheet("QLabel {\n"
"color: #fff;\n"
"font: 10pt \"Mongolian Baiti\";\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encrypter"))
        self.label.setText(_translate("MainWindow", "Encrypter v. 2.4.8"))
        self.Key.setText(_translate("MainWindow", "Создать ключ"))
        self.Encrypt.setText(_translate("MainWindow", "Зашифровать файл"))
        self.pushButton.setText(_translate("MainWindow", "Расшифровать файл"))
        self.label_2.setText(_translate("MainWindow", "Prod. by Ramazan Muslimov"))



