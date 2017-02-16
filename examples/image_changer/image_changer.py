import os
import platform
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDockWidget, QListWidget, QFrame, \
							QAction
from PyQt5.QtGui import QImage, QIcon, QKeySequence
from PyQt5.QtCore import Qt
# import helpform
# import newimagedlg
# import qrc_resources

__version__ = "1.0.0"

class MainWindow(QMainWindow):

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)

		self.image = QImage()
		self.dirty = False
		self.filename = None
		self.mirroredvertically = False
		self.mirroredhorizontally = False

		self.imageLabel = QLabel()
		self.imageLabel.setMinimumSize(200,200)
		self.imageLabel.setAlignment(Qt.AlignCenter)
		self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.setCentralWidget(self.imageLabel)

		logDockWidget = QDockWidget("Log", self)
		logDockWidget.setObjectName("logDockWidget")
		logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)

		self.listWidget = QListWidget()
		logDockWidget.setWidget(self.listWidget)
		self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

		self.printer = None
		self.sizeLabel = QLabel()
		self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
		status = self.statusBar()
		status.setSizeGripEnabled(False)
		status.addPermanentWidget(self.sizeLabel)
		status.showMessage("Ready", 5000)

		fileNewAction = QAction(QIcon("images/filenew.png"), "&New", self)
		fileNewAction.setShortcut(QKeySequence.New)
		helpText = "Create a new image"
		fileNewAction.setToolTip(helpText)
		fileNewAction.setStatusTip(helpText)
		fileNewAction.triggered.connect(self.fileNew)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(fileNewAction)
		self.toolbar = self.addToolBar('New')
		self.toolbar.addAction(fileNewAction)
		
		self.setWindowTitle("Image Changer")

	def fileNew(self):
		pass

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()