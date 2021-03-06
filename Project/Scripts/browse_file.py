# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Browser(object):
	def setupUi(self, Browser):
		Browser.setObjectName("Browser")
		Browser.resize(272, 135)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Browser.setWindowIcon(icon)
		Browser.setStyleSheet("background-color: #929294;")
		self.browsefile = QtWidgets.QPushButton(Browser)
		self.browsefile.setGeometry(QtCore.QRect(170, 70, 91, 21))
		self.browsefile.setStyleSheet("QPushButton {\n"
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
		self.browsefile.setObjectName("browsefile")
		self.lineEdit = QtWidgets.QLineEdit(Browser)
		self.lineEdit.setGeometry(QtCore.QRect(20, 69, 141, 21))
		self.lineEdit.setStyleSheet("background-color:#fff;")
		self.lineEdit.setObjectName("lineEdit")

		self.retranslateUi(Browser)
		QtCore.QMetaObject.connectSlotsByName(Browser)

	def retranslateUi(self, Browser):
		_translate = QtCore.QCoreApplication.translate
		Browser.setWindowTitle(_translate("Browser", "Browse"))
		self.browsefile.setText(_translate("Browser", "Обзор"))
		

	
