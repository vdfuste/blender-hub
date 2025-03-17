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

	def setMargins(self, left, top=None, right=None, bottom=None):
		top = top or left
		right = right or left
		bottom = bottom or top
		self.layout.setContentsMargins(left, top, right, bottom)
	
	def setSpacing(self, spacing):
		self.layout.setSpacing(spacing)
