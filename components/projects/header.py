from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy

class Header(QWidget):
	def __init__(self):
		super(QWidget, self).__init__()

		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		
		header = QWidget()
		header.setObjectName("list-header")
		header_layout = QHBoxLayout()
		header_layout.setContentsMargins(24, 0, 32, 0)

		# Buttons
		'''star_btn = QPushButton("*")
		star_btn.clicked.connect(lambda: self.sortBy("star"))
		header_layout.addWidget(star_btn)'''

		name_btn = QPushButton("NAME")
		name_btn.clicked.connect(lambda: self.sortBy("name"))
		name_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		header_layout.addWidget(name_btn)
	
		modified_btn = QPushButton("MODIFIED")
		modified_btn.clicked.connect(lambda: self.sortBy("modified"))
		header_layout.addWidget(modified_btn)
	
		version_btn = QPushButton("VERSION")
		version_btn.setObjectName("last")
		version_btn.clicked.connect(lambda: self.sortBy("version"))
		header_layout.addWidget(version_btn)
		
		header.setLayout(header_layout)
		layout.addWidget(header)
		self.setLayout(layout)

	def sortBy(self, type):
		print(f"{type} button pressed!")
