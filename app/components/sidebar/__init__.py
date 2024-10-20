from os import path

from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

from app.components.custom.frame import Frame
from app.components.custom.button import Button

from app.pages import pages_data

class Sidebar(Frame):
	pageChanged = pyqtSignal(str)

	def __init__(self):
		super().__init__("sidebar", QVBoxLayout)
		self.initUI()

	def initUI(self):
		self.loadStyle()
		self.setFixedWidth(220)

		# Header
		header = Frame("header")
		header.layout.addStretch()

		icon = QLabel("icon")
		icon.setFixedWidth(20)
		icon.setPixmap(QPixmap("app/src/images/icons/logo.svg"))
		header.addWidget(icon)
		
		title = QLabel("Blender Hub")
		title.setObjectName("title")
		header.addWidget(title)
		
		header.layout.addStretch()
		self.addWidget(header)
		
		self.layout.addStretch()
		
		# Buttons
		buttons = Frame("buttons", QVBoxLayout)
		
		for data in pages_data:
			self.addButton(data, buttons.layout)
		
		self.addWidget(buttons)

		self.layout.addStretch()
		
	def loadStyle(self):
		_path = path.dirname(path.abspath(__file__))

		with open(f"{_path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def addButton(self, data, layout):
		label = data["title"]
		icon = data["icon"]
		
		button = Button(label, f"app/src/images/icons/{icon}", "sidebar-button", Qt.AlignRight)
		button.clicked.connect(lambda id=label: self.pageChanged.emit(id))
		
		layout.addWidget(button)
