from os import path
from PyQt5.QtWidgets import QFrame, QHBoxLayout

class Frame(QFrame):
	def __init__(self, name="", layout=QHBoxLayout):
		super().__init__()

		self.setObjectName(name)

		self.layout = layout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)
		
		self.setLayout(self.layout)
	
	def loadStyle(self, file):
		_path = path.dirname(path.abspath(file))
		with open(f"{_path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def addWidget(self, widget, first=False):
		#index = 0 if first else len(self.layout)
		#self.layout.insertWidget(index, widget)
		self.layout.addWidget(widget)

	def setSpacing(self, spacing):
		self.layout.setSpacing(spacing)
