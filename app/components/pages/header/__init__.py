from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel

from app.components.custom.frame import Frame

class HeaderPage(Frame):
	def __init__(self, title, name="header-page"):
		super().__init__(name)

		self.loadStyle(__file__)
		self.setFixedHeight(150)

		self.layout.setContentsMargins(24, 0, 16, 0)
		self.layout.setAlignment(Qt.AlignBottom)
		
		title_label = QLabel(title)
		title_label.setObjectName("title")
		title_label.setFixedHeight(64)
		self.addWidget(title_label)

		self.layout.addStretch()
