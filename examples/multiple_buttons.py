#!/home/weiwen/anaconda3/bin/python

import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QHBoxLayout

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		button1 = QPushButton("One")
		button2 = QPushButton("Two")
		button3 = QPushButton("Three")
		button4 = QPushButton("Four")
		button5 = QPushButton("Five")
		self.toLabel = QLabel("Click Something")

		button1.clicked.connect(partial(self.anyButton, "One"))
		button2.clicked.connect(partial(self.anyButton, "Two"))
		button3.clicked.connect(partial(self.anyButton, "Three"))
		button4.clicked.connect(partial(self.anyButton, "Four"))
		button5.clicked.connect(partial(self.anyButton, "Five"))

		layout = QHBoxLayout()
		layout.addWidget(button1)
		layout.addWidget(button2)
		layout.addWidget(button3)
		layout.addWidget(button4)
		layout.addWidget(button5)
		layout.addWidget(self.toLabel)
		self.setLayout(layout)

		button1.setFocus()


	def anyButton(self, who):
		self.toLabel.setText("You clicked button '{}'".format(who))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()