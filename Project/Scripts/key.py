# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyCreated(object):
    def setupUi(self, KeyCreated):
        KeyCreated.setObjectName("KeyCreated")
        KeyCreated.resize(345, 127)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KeyCreated.setWindowIcon(icon)
        KeyCreated.setStyleSheet("background-color: #929294;")
        self.label = QtWidgets.QLabel(KeyCreated)
        self.label.setGeometry(QtCore.QRect(100, 20, 141, 41))
        self.label.setStyleSheet("QLabel {\n"
"color: #fff;\n"
"font: 17pt \"Mongolian Baiti\";\n"
"}")
        self.label.setObjectName("label")
        self.CloseKey = QtWidgets.QPushButton(KeyCreated)
        self.CloseKey.setEnabled(True)
        self.CloseKey.setGeometry(QtCore.QRect(130, 80, 75, 23))
        self.CloseKey.setAutoFillBackground(False)
        self.CloseKey.setStyleSheet("QPushButton {\n"
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
        self.CloseKey.setObjectName("CloseKey")

        self.retranslateUi(KeyCreated)
        QtCore.QMetaObject.connectSlotsByName(KeyCreated)

    def retranslateUi(self, KeyCreated):
        _translate = QtCore.QCoreApplication.translate
        KeyCreated.setWindowTitle(_translate("KeyCreated", "Created"))
        self.label.setText(_translate("KeyCreated", "Ключ создан"))
        self.CloseKey.setText(_translate("KeyCreated", "OK"))



