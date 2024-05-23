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
