from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from components.custom.frame import Frame

class ScrollArea(Frame):
	def __init__(self, name="scroll-area", layout=QVBoxLayout):
		super().__init__(name)

		self.loadStyle(__file__)

		self.content = Frame(f"{name}-items", layout)
		self.content.layout.setAlignment(Qt.AlignTop)

		self.scroll = QScrollArea()
		self.scroll.setWidgetResizable(True)
		self.scroll.setWidget(self.content)

		self.addWidget(self.scroll)

	def hideHorizontalScroll(self, hide=True):
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff if hide else None)

	def hideVerticalScroll(self, hide=True):
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff if hide else None)
	
	def setSpacing(self, spacing):
		self.content.setSpacing(spacing)

	def addItem(self, item):
		self.content.addWidget(item)

	'''def clear(self):
		pass

	def populate(self, items):
		pass
		self.clear()

		for item in items:
			self.addWidget(item)

		self.update()

	def update(self):
		pass
		#self.content.update()'''