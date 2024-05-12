class Widget(QWidget):
	def __init__(self, name):
		super().__init__()

		self.setObjectName(name)
		loadStyle("src/qss/Style.qss", self)

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		
		# Widget Content
		label = QLabel("My Label here")
		layout.addWidget(label)

		self.setLayout(layout)