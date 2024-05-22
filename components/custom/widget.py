from utils.read import loadStyle

class Widget():
	def __init__(self, widget, layout, name=""):
		
		self.layout = layout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)

		self.widget = widget(objectName=name)
		self.widget.setLayout(self.layout)

	def parent(self, parent):
		parent.addWidget(self.widget)
	
	def addWidget(self, widget):
		self.layout.addWidget(widget)

	def count(self):
		return self.layout.count()
	
	def takeAt(self, index):
		return self.layout.takeAt(index)

	def loadStyle(self, style_path):
		loadStyle(style_path, self.widget)

'''class Widget(QWidget):
	def __init__(self):
		super().__init__()

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)
		self.setLayout(self.layout)
		# self.setStyleSheet("background-color: transparent")

	def count(self):
		return self.layout.count()

	def takeAt(self, index):
		return self.layout.takeAt(index)
	
	def setWidget(self, widget):
		self.layout.addWidget(widget)
'''
'''class StyleWidget(Widget):
	def __init__(self, layout, parent, name=""):
		super().__init__(layout, parent, name)

		self.content = layout()
		self.content.setContentsMargins(0, 0, 0, 0)
		self.content.setSpacing(0)

		widget = QWidget(objectName=name)
		widget.setLayout(self.content)
		self.setWidget(widget)

		# self.setStyleSheet("background-color: transparent")

	def addWidget(self, widget):
		self.content.addWidget(widget)

	def count(self):
		return self.content.count()
	
	def takeAt(self, index):
		return self.content.takeAt(index)
	
	def setAlignment(self, alignment):
		self.content.setAlignment(alignment)

	def loadStyle(self, style_path):
		loadStyle(style_path, self.widget)'''