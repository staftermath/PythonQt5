#!/home/weiwen/anaconda3/bin/python

import sys
from math import *
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QTextBrowser, QLineEdit, QVBoxLayout
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

class Form(QDialog):
	def __init__(self, parent = None):
		super(Form, self).__init__(parent)
		self.browser = QTextBrowser()
		self.lineedit = QLineEdit("Type an expression and press Enter")
		self.lineedit.selectAll()
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		self.setLayout(layout)
		self.lineedit.setFocus()
		self.lineedit.returnPressed.connect(self.updateUi)
		self.setWindowTitle("Calculate")

	def updateUi(self):
		try:
			text = str(self.lineedit.text())
			self.browser.append("{} = <b>{}</b>".format(text,eval(text)))
		except:
			self.browser.append("<font color=red>{} is invalid!</font>".format(text))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
