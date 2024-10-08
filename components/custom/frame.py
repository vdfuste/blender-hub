from os import path
from PyQt5.QtWidgets import QFrame, QHBoxLayout

class Frame(QFrame):
	def __init__(self, name="", layout=QHBoxLayout):
		super().__init__()

		self.layout = layout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)
		
		self.setObjectName(name)
		self.setLayout(self.layout)
	
	def loadStyle(self, file):
		_path = path.dirname(path.abspath(file))
		with open(f"{_path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def addWidget(self, widget):
		self.layout.addWidget(widget)
