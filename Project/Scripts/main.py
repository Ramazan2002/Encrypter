import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from first import Ui_MainWindow
from key import Ui_KeyCreated
from encrypt_page import Ui_EncryptedFile
from browse_file import Ui_Browser
from browse_file_2 import Ui_Browser2


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# logic...


def OpenOtherWindow():
	import create_key
	global KeyCreated
	KeyCreated = QtWidgets.QWidget() 
	ui = Ui_KeyCreated()
	ui.setupUi(KeyCreated)
	KeyCreated.show()

	def close_window():
		KeyCreated.close()	
	ui.CloseKey.clicked.connect(close_window)


def OpenBrowseFile():
	global Browser
	Browser = QtWidgets.QDialog()
	ui = Ui_Browser()
	ui.setupUi(Browser)
	Browser.show()

	
	def BrowseFile(self):
		global fname 
		fname = QFileDialog.getOpenFileName(None, 'Open file', '')[0]
		from encrypt import encrypt
		key = open('crypto.key', 'rb').read() 
		encrypt(fname,key)
		Browser.close()
	ui.browsefile.clicked.connect(BrowseFile)


def OpenBrowseFile_2():
	global Browser2
	Browser2 = QtWidgets.QDialog()
	ui = Ui_Browser2()
	ui.setupUi(Browser2)
	Browser2.show() 


	def BrowseFile_2(self):
		global fname 
		fname = QFileDialog.getOpenFileName(None, 'Open file', '')[0]
		from decrypt import decrypt
		key = open('crypto.key', 'rb').read() 
		decrypt(fname,key)
		Browser2.close()
	ui.browse_file_2.clicked.connect(BrowseFile_2)



ui.Encrypt.clicked.connect(OpenBrowseFile)
ui.pushButton.clicked.connect(OpenBrowseFile_2)
ui.Key.clicked.connect(OpenOtherWindow)

sys.exit(app.exec_())