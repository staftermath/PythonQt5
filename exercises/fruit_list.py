#!/home/weiwen/anaconda3/bin/python

import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout, \
						    QDialogButtonBox, QMessageBox, \
						    QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget
from PyQt5.QtCore import Qt

class StringListDlg(QDialog):
	def __init__(self, fruit, parent=None):
		super(StringListDlg, self).__init__(parent)

		self.stringlist = fruit

		self.fruitList = QListWidget()
		self.fruitList.addItems(self.stringlist)
		button_Add = QPushButton("&Add...")
		button_Edit = QPushButton("&Edit...")
		button_Remove = QPushButton("&Remove...")
		button_Up = QPushButton("&Up")
		button_Down = QPushButton("&Down")
		button_Sort = QPushButton("&Sort")
		button_Close = QPushButton("&Close")

		layout = QGridLayout()
		layout.addWidget(self.fruitList, 0, 0, 7, 1)
		layout.addWidget(button_Add, 0, 1)
		layout.addWidget(button_Edit, 1, 1)
		layout.addWidget(button_Remove, 2, 1)
		layout.addWidget(button_Up, 3, 1)
		layout.addWidget(button_Down, 4, 1)
		layout.addWidget(button_Sort, 5, 1)
		layout.addWidget(button_Close, 6, 1)
		self.setLayout(layout)
		self.setWindowTitle("Edit Fruit List")

		button_Add.clicked.connect(self.Add_Win)
		button_Sort.clicked.connect(self.Sort)
		button_Remove.clicked.connect(self.Remove_Win)


	def Add_Win(self):
		dialog = Edit(label="Add Fruit", parent=self)
		dialog.buttons.accepted.connect(dialog.accept)
		if dialog.exec_():
			if len(self.fruitList.findItems(dialog.edit.text(), Qt.MatchExactly)) == 0:
				self.fruitList.addItem(str(dialog.edit.text()))
			else:
				QMessageBox.warning(self, "Warning", "{} already in list".format(dialog.edit.text()))

	def Remove_Win(self):
		for item in self.fruitList.selectedItems():
			self.fruitList.takeItem(self.fruitList.row(item))

	def Sort(self):
		self.fruitList.sortItems()





class Edit(QDialog):
	def __init__(self, label, parent=None):
		super(Edit, self).__init__(parent)
		
		self.toLabel = QLabel(label)
		self.edit = QLineEdit()

		self.buttons = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)

		layout = QVBoxLayout()
		layout.addWidget(self.toLabel)
		layout.addWidget(self.edit)
		layout.addWidget(self.buttons)
		self.setLayout(layout)


if __name__ == "__main__":
	fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
			"Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
			"Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
			"Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry",
			"Orange"]
	app = QApplication(sys.argv)
	form = StringListDlg(fruit)
	form.exec_()
	print("\n".join([str(x) for x in form.stringlist]))