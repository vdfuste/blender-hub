from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QSizePolicy

from components.custom.widget import Widget

class ScrollList(Widget):
	def __init__(self, name="scroll-list"):
		super().__init__(QScrollArea, QVBoxLayout, name)

		# self.loadStyle("src/qss/components/scroll_list.qss")
		self.layout.setAlignment(Qt.AlignTop)

		self.items = QWidget(objectName=f"{name}-items")
		self.items.setLayout(self.layout)

		self.widget.setWidgetResizable(True)
		self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.widget.setWidget(self.items)

	def addItem(self, item):
		self.layout.addWidget(item.widget)

	def clear(self):
		while self.layout.count():
			item = self.layout.takeAt(0)
			if item.widget():
				item.widget().deleteLater()
	
	def populate(self, items, callback):
		# Remove all items before populate
		self.clear()
		
		# Populate list using an external item as template
		for index, data in enumerate(items):
			self.addItem(callback(data, index))

		self.layout.update()

'''class ScrollList(QWidget):
	def __init__(self, name="scroll-list"):
		super().__init__()

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)
		self.layout.setAlignment(Qt.AlignTop)

		self.items = QWidget(objectName=f"{name}-items")
		self.items.setLayout(self.layout)

		scroll_area = QScrollArea(objectName=name)
		scroll_area.setWidgetResizable(True)
		scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		scroll_area.setWidget(self.items)

		wrap_layout = QVBoxLayout()
		wrap_layout.setContentsMargins(0, 0, 0, 0)
		wrap_layout.setSpacing(0)
		wrap_layout.addWidget(scroll_area)
		self.setLayout(wrap_layout)

	def addItem(self, item):
		self.layout.addWidget(item)

	def clear(self):
		while self.layout.count():
			item = self.layout.takeAt(0)
			if item.widget():
				item.widget().deleteLater()
	
	def populate(self, items, callback):
		# Remove all items before populate
		self.clear()
		
		# Populate list using an external item as template
		for index, data in enumerate(items):
			self.addItem(callback(data, index))

		self.layout.update()'''
