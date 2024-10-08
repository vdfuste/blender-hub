from os import path

from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QFrame, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

from components.button import Button
from components.pages import pages_data

class Sidebar(QFrame):
	pageChanged = pyqtSignal(str)

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.loadStyle()

		self.setObjectName("sidebar")
		self.setFixedWidth(220)

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)

		# Header
		header = QWidget()
		header.setObjectName("header")
		header_layout = QHBoxLayout()
		header_layout.setContentsMargins(0, 24, 0, 0)

		header_layout.addStretch()

		icon = QLabel()
		icon.setObjectName("icon")
		icon.setFixedWidth(20)
		icon.setPixmap(QPixmap("src/images/icons/logo.svg"))
		header_layout.addWidget(icon)
		
		title = QLabel("Blender Hub")
		title.setObjectName("title")
		header_layout.addWidget(title)
		
		header_layout.addStretch()

		header.setLayout(header_layout)
		layout.addWidget(header)
		
		layout.addStretch()
		
		# Buttons
		buttons = QWidget()
		buttons.setObjectName("buttons")
		buttons_layout = QVBoxLayout()
		buttons_layout.setContentsMargins(0, 0, 0, 0)
		buttons_layout.setSpacing(0)
		
		for data in pages_data:
			self.addButton(data, buttons_layout)

		buttons.setLayout(buttons_layout)
		layout.addWidget(buttons)

		layout.addStretch()
		
		self.setLayout(layout)

	def loadStyle(self):
		_path = path.dirname(path.abspath(__file__))

		with open(f"{_path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def addButton(self, data, layout):
		label = data["title"]
		icon = data["icon"]
		
		button = Button(label, f"src/images/icons/{icon}", "sidebar-button", Qt.AlignRight)
		button.clicked.connect(lambda id=label: self.pageChanged.emit(id))
		
		layout.addWidget(button)
