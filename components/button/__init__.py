from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

class Button(QFrame):
	clicked = pyqtSignal()
	
	def __init__(self, label="", icon=None, name="button"):
		super().__init__()
		
		self.initUI(label, icon, name)

	def initUI(self, label, icon, name):
		self.loadStyle("components/button")

		self.setObjectName(name)
		self.setFrameShape(QFrame.Panel)
		
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		label = QLabel(label)
		label.setObjectName("label")
		layout.addWidget(label)

		#layout.addStretch()

		self.icon = QLabel()
		self.icon.setObjectName("icon")
		self.icon.hide()
		
		if icon is not None:
			self.icon.setPixmap(QPixmap(icon))
			self.icon.show()
		
		layout.addWidget(self.icon)
		
		self.setLayout(layout)

	def loadStyle(self, path):
		with open(f"{path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def mousePressEvent(self, event):
		self.clicked.emit()
