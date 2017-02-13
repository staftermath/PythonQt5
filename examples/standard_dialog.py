#!/home/weiwen/anaconda3/bin/python

import sys
import numberformatdlg1
import numberformatdlg2
from functools import partial
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout, \
						    QSpinBox, QCheckBox, QDialogButtonBox, \
						    QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		self.format = dict(thousandsseparator=",", \
						   decimalmarker=".", decimalplaces=2, \
						   rednegatives=False)

		self.toLabel = QLabel("")
		formatButton1 = QPushButton("Formating Number 1")
		formatButton2 = QPushButton("Formating Number 2")

		layout = QVBoxLayout()
		layout.addWidget(self.toLabel)
		layout.addWidget(formatButton1)
		layout.addWidget(formatButton2)

		self.setLayout(layout)
		self.setWindowTitle("Change Format")

		formatButton1.clicked.connect(self.setNumberFormat1)
		formatButton2.clicked.connect(self.setNumberFormat2)

	def setNumberFormat1(self):
		dialog = numberformatdlg1.NumberFormatDlg(format=self.format, parent=self)
		dialog.show()

		if dialog.exec_():
			self.toLabel.setText("Thousands separator = {}<br>"
								 "Decimal Marker = {}<br>"
								 "Decimal Places = {}<br>"
								 "Red Negative Numbers: {}".format(*list(dialog.format.values())))
								 								   # self.format["thousandsseparator"], \
								 								   # self.format.decimalmarker, \
								 								   # self.format.decimalplaces, \
								 								   # self.format.rednegatives
								 								   # ))
	def setNumberFormat2(self):
		dialog = numberformatdlg2.NumberFormatDlg(format=self.format, parent=self)
		dialog.changed.connect(self.refreshTable)
		dialog.show()

	def refreshTable(self):
		self.toLabel.setText("Thousands separator = {}<br>"
								 "Decimal Marker = {}<br>"
								 "Decimal Places = {}<br>"
								 "Red Negative Numbers: {}".format(*list(self.format.values())))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
