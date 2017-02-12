#!/home/weiwen/anaconda3/bin/python

import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout, \
						    QDoubleSpinBox, QComboBox

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		self.principal = QDoubleSpinBox()
		self.principal.setRange(0.01, 10000000.00)
		self.principal.setValue(1000.00)
		self.principal.setPrefix("$ ")
		self.rate = QDoubleSpinBox()
		self.rate.setRange(0.01, 100.00)
		self.rate.setValue(5.00)
		self.rate.setSuffix(" %")
		self.years = QComboBox()
		self.yearsDict = {"1 year": 1,
				 "2 years": 2,
				 "3 years": 3,
				 "4 years": 4}
		self.years.addItems(self.yearsDict)

		self.principal.valueChanged.connect(self.CalculateInterest)
		self.rate.valueChanged.connect(self.CalculateInterest)
		self.years.currentIndexChanged.connect(self.CalculateInterest)
		self.toLabel = QLabel("")
		label_principal = QLabel("Principle:")
		label_rate = QLabel("Rate:")
		label_years = QLabel("Years:")
		label_amount = QLabel("Amount")
		self.CalculateInterest()

		layout = QGridLayout()
		layout.addWidget(label_principal, 0, 0)
		layout.addWidget(label_rate, 1, 0)
		layout.addWidget(label_years, 2, 0)
		layout.addWidget(label_amount, 3, 0)
		layout.addWidget(self.principal, 0, 1)
		layout.addWidget(self.rate, 1, 1)
		layout.addWidget(self.years, 2, 1)
		layout.addWidget(self.toLabel, 3, 1)
		self.setLayout(layout)
		self.setWindowTitle("Interest")

	def CalculateInterest(self):
		Principal = float(self.principal.value())
		Rate = float(self.rate.value())/100
		Years = float(self.yearsDict[self.years.currentText()])
		InterestPlusPrincipal = Principal*((1+Rate)**Years)
		self.toLabel.setText("$ {:0.2f}".format(InterestPlusPrincipal))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()