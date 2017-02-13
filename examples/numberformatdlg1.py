from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout, \
						    QSpinBox, QCheckBox, QDialogButtonBox, \
						    QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
class NumberFormatDlg(QDialog):

	def __init__(self, format, parent=None):
		super(NumberFormatDlg, self).__init__(parent)

		thousandsLabel = QLabel("&Thousands separator")
		self.thousandsEdit = QLineEdit(format["thousandsseparator"])
		thousandsLabel.setBuddy(self.thousandsEdit)
		decimalMarkerLabel = QLabel("Decimal &marker")
		self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
		decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
		decimalPlacesLabel = QLabel("&Decimal places")
		self.decimalPlacesSpinBox = QSpinBox()
		decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
		self.decimalPlacesSpinBox.setRange(0, 6)
		self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
		self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
		self.redNegativesCheckBox.setChecked(format["rednegatives"])

		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)

		self.format = format.copy()

		grid = QGridLayout()
		grid.addWidget(thousandsLabel, 0, 0)
		grid.addWidget(self.thousandsEdit, 0, 1)
		grid.addWidget(decimalMarkerLabel, 1, 0)
		grid.addWidget(self.decimalMarkerEdit, 1, 1)
		grid.addWidget(decimalPlacesLabel, 2, 0)
		grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
		grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
		grid.addWidget(buttonBox, 4, 0, 1, 2)
		self.setLayout(grid)

		buttonBox.accepted.connect(self.accept)
		buttonBox.rejected.connect(self.reject)

		self.setWindowTitle("Set Number Format (Modal)")

	def numberFormat(self):
		return self.format

	def accept(self):
		class ThousandsError(Exception):
			def __init__(self, args):
				self.__str__ = args

		class DecimalError(Exception):
			def __init__(self, args):
				self.__str__ = args

		Punctuation = frozenset(" ,;:.")

		thousands = str(self.thousandsEdit.text())
		decimal = str(self.decimalMarkerEdit.text())
		try:
			if len(decimal) == 0:
				raise DecimalError("The decimal marker may not be empty.")

			if len(thousands) > 1:
				raise ThousandsError("The thousands separator may only be empty or one character.")

			if len(decimal) > 1:
				raise DecimalError("The decimal marker must be one character.")

			if thousands == decimal:
				raise ThousandsError("The thousands separator and the decimal marker must be different.")

			if thousands and thousands not in Punctuation:
				raise ThousandsError("The thousands separator must be a punctuation symbol.")

			if decimal not in Punctuation:
				raise DecimalError("The decimal marker must be a punctuation symbol.")

		except ThousandsError as e:
			QMessageBox.warning(self, "Thousands Separator Error", str(e))
			self.thousandsEdit.selectAll()
			self.thousandsEdit.setFocus()
			return

		except DecimalError as e:
			QMessageBox.warning(self, "Decimal Marker Error", str(e))
			self.decimalMarkerEdit.selectAll()
			self.decimalMarkerEdit.setFocus()
			return

		self.format["thousandsseparator"] = thousands
		self.format["decimalmarker"] = decimal
		self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
		self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
		QDialog.accept(self)