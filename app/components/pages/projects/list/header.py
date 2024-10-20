from PyQt5.QtWidgets import QPushButton, QSizePolicy

from app.components.custom.frame import Frame

class HeaderList(Frame):
	def __init__(self, name="list-header"):
		super().__init__(name)
		
		self.setFixedHeight(58)
		self.layout.setContentsMargins(24, 0, 32, 0)

		'''star_button = QPushButton("*")
		star_button.clicked.connect(lambda _, label="star": self.sortBy(label))
		self.addWidget(star_button)'''

		name_button = QPushButton("NAME")
		name_button.clicked.connect(lambda _, label="name": self.sortBy(label))
		name_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		self.addWidget(name_button)
	
		modified_button = QPushButton("MODIFIED")
		modified_button.setFixedWidth(150)
		modified_button.clicked.connect(lambda _, label="modified": self.sortBy(label))
		self.addWidget(modified_button)
	
		version_button = QPushButton("VERSION")
		version_button.setObjectName("last")
		version_button.setFixedWidth(150)
		version_button.clicked.connect(lambda _, label="version": self.sortBy(label))
		self.addWidget(version_button)
		
	def sortBy(self, label):
		print(f"[Blender Hub] {label} button pressed!")
