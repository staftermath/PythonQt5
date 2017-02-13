#!/home/weiwen/anaconda3/bin/python

import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout, \
						    QDoubleSpinBox, QComboBox, QSpinBox, QCheckBox, QHBoxLayout, \
						    QVBoxLayout
from PyQt5.QtCore import Qt

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		self.width = 1
		self.beveled = False
		self.style = "Solid"
		self.label = QLabel("The Pen has not been set")
		self.label.setTextFormat(Qt.RichText)

		invoke = QPushButton("Invoke Pen")
		invoke.clicked.connect(self.setPenProperties)

		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(invoke)

		self.setLayout(layout)
		self.setWindowTitle("Test Invoke PenProp")

	def setPenProperties(self):
		dialog = PenPropertiesDlg(self)
		dialog.widthSpinBox.setValue(self.width)
		dialog.beveledCheckBox.setChecked(self.beveled)
		dialog.styleComboBox.setCurrentIndex(\
							dialog.styleComboBox.findText(self.style))

		if dialog.exec_():
			self.width = dialog.widthSpinBox.value()
			self.beveled = dialog.beveledCheckBox.isChecked()
			self.style = str(dialog.styleComboBox.currentText())
			self.updateData()

	def updateData(self):
		bevel = ""
		if self.beveled:
			bevel = "<br>Beveled"
		self.label.setText("<font color=red>Width</font> = {}<br>Style = {}{}".format(self.width, self.style, bevel))

class PenPropertiesDlg(QDialog):

	def __init__(self, parent=None):
		super(PenPropertiesDlg, self).__init__(parent)
		widthLabel = QLabel("&Width")
		self.widthSpinBox = QSpinBox()
		widthLabel.setBuddy(self.widthSpinBox)
		self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
		self.widthSpinBox.setRange(0, 24)
		self.beveledCheckBox = QCheckBox("&Beveled edges")
		styleLabel = QLabel("&Style:")
		self.styleComboBox = QComboBox()
		styleLabel.setBuddy(self.styleComboBox)
		self.styleComboBox.addItems(["Solid", "Dashed", "Dotted", \
									 "DashDotted", "DashDotDotted"])
		okButton = QPushButton("&OK")
		cancelButton = QPushButton("Cancel")

		buttonLayout = QHBoxLayout()
		buttonLayout.addStretch()
		buttonLayout.addWidget(okButton)
		buttonLayout.addWidget(cancelButton)
		layout = QGridLayout()
		layout.addWidget(widthLabel, 0, 0)
		layout.addWidget(self.widthSpinBox, 0, 1)
		layout.addWidget(self.beveledCheckBox, 0, 2)
		layout.addWidget(styleLabel, 1, 0)
		layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
		layout.addLayout(buttonLayout, 2, 0, 1, 3)
		self.setLayout(layout)

		okButton.clicked.connect(self.accept) # accept is a build-in function to run exec_()?
		cancelButton.clicked.connect(self.reject)

		self.setWindowTitle("Pen Properties")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

