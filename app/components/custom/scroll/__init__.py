from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QSizePolicy

from app.components.custom.frame import Frame

class ScrollArea(Frame):
	def __init__(self, name="scroll-area", layout=QVBoxLayout):
		super().__init__(name, QVBoxLayout)

		self.loadStyle(__file__)

		self.items = []
		
		self.content = Frame(f"items", layout)
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
		self.items.append(item)
		self.content.addWidget(self.items[-1])

	def clear(self):
		for item in self.items:
			item.deleteLater()
		self.items.clear()
