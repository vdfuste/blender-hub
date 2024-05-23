from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from components.custom.widget import Widget
from utils.read import loadStyle

class HeaderPage(Widget):
	def __init__(self, title, name="header-page"):
		super().__init__(QWidget, QHBoxLayout, name)

		self.loadStyle("src/qss/components/header_page.qss")
		self.widget.setFixedHeight(150)

		self.layout.setContentsMargins(24, 0, 16, 0)
		self.layout.setAlignment(Qt.AlignBottom)
		
		_title = QLabel(title, objectName=f"{name}-title")
		_title.setFixedHeight(50)
		self.addWidget(_title)

		self.layout.addStretch(0)
