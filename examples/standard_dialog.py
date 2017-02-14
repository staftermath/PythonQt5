#!/home/weiwen/anaconda3/bin/python

import sys
import numberformatdlg1, numberformatdlg2, numberformatdlg3
import random, string, math
from functools import partial
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout, \
						    QSpinBox, QCheckBox, QDialogButtonBox, \
						    QVBoxLayout, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class Form(QDialog):
	
	X_MAX = 26
	Y_MAX = 60
	
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		
		self.numberFormatDlg = None
		self.format = dict(thousandsseparator=",", \
						   decimalmarker=".", decimalplaces=2, \
						   rednegatives=False)
		self.numbers = {}
		for x in range(self.X_MAX):
			for y in range(self.Y_MAX):
				self.numbers[(x,y)] = (10000*random.random())-5000


		self.table = QTableWidget()
		self.toLabel = QLabel("")
		formatButton1 = QPushButton("Formating Number 1")
		formatButton2 = QPushButton("Formating Number 2")
		formatButton3 = QPushButton("Formating Number 3")

		layout = QVBoxLayout()
		layout.addWidget(self.table)
		layout.addWidget(formatButton1)
		layout.addWidget(formatButton2)
		layout.addWidget(formatButton3)

		self.setLayout(layout)
		self.setWindowTitle("Change Format")
		


		formatButton1.clicked.connect(self.setNumberFormat1)
		formatButton2.clicked.connect(self.setNumberFormat2)
		formatButton3.clicked.connect(self.setNumberFormat3)
		self.refreshTable()

	def setNumberFormat1(self):
		dialog = numberformatdlg1.NumberFormatDlg(format=self.format, parent=self)
		# dialog.show()

		if dialog.exec_():
			self.format = dialog.numberFormat()
			self.refreshTable()
			# self.toLabel.setText("Thousands separator = {}<br>"
			# 					 "Decimal Marker = {}<br>"
			# 					 "Decimal Places = {}<br>"
			# 					 "Red Negative Numbers: {}".format(*list(dialog.format.values())))
								 								   
	def setNumberFormat2(self):
		dialog = numberformatdlg2.NumberFormatDlg(format=self.format, parent=self)
		dialog.changed.connect(self.refreshTable)
		dialog.show()

	def setNumberFormat3(self):
		if self.numberFormatDlg is None:
			self.numberFormatDlg = numberformatdlg3.NumberFormatDlg(self.format, self.refreshTable, self)
		self.numberFormatDlg.show()
		self.numberFormatDlg.raise_()
		self.numberFormatDlg.activateWindow()

	def refreshTable(self):
		self.table.clear()
		self.table.setColumnCount(self.X_MAX)
		self.table.setRowCount(self.Y_MAX)
		self.table.setHorizontalHeaderLabels(list(string.ascii_uppercase))
		for x in range(self.X_MAX):
			for y in range(self.Y_MAX):
				fraction, whole = math.modf(self.numbers[(x,y)])
				sign = "-" if whole < 0 else ""
				whole = "{}".format(math.floor(abs(whole)))
				digits = []
				for i, digit in enumerate(reversed(whole)):
					if i and i % 3 == 0:
						digits.insert(0, self.format["thousandsseparator"])
					digits.insert(0, digit)
				if self.format["decimalplaces"]:
					fraction = "{}".format(abs(fraction))
					fraction = (self.format["decimalmarker"] + fraction[2:(self.format["decimalplaces"]+2)])
				else:
					fraction = ""
				text = "{0}{1}{2}".format(sign, "".join(digits), fraction)
				item = QTableWidgetItem(text)
				item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
				if sign and self.format["rednegatives"]:
					item.setBackground(Qt.red)
				self.table.setItem(y, x, item)
		# self.toLabel.setText("Thousands separator = {}<br>"
		# 						 "Decimal Marker = {}<br>"
		# 						 "Decimal Places = {}<br>"
		# 						 "Red Negative Numbers: {}".format(*list(self.format.values())))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
