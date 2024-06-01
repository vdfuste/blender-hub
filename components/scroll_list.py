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

	def addItem(self, item, on_top=False):
		self.layout.insertWidget(0 if on_top else len(self.layout), item)

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

	# def iterate(self, callback):
	# 	for i in range(self.layout.count()):
			
	# 		item = self.layout.takeAt(i)
	# 		print(item)
			
	# 		if item != None:
	# 			callback(item.widget())
