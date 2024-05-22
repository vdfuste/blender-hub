from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from components.custom.widget import Widget
from utils.read import loadStyle

class HeaderPage(Widget):
	def __init__(self, title, name="header-page"):
		super().__init__(QWidget, QHBoxLayout, name)

		self.loadStyle("src/qss/components/header_page.qss")
		self.layout.setContentsMargins(24, 0, 16, 16)
		self.layout.setSpacing(8)
		self.layout.setAlignment(Qt.AlignBottom)
		
		_title = QLabel(title, objectName=f"{name}-title")
		self.addWidget(_title)

		self.layout.addStretch(0)

'''class HeaderPage(StyleWidget):
	def __init__(self, parent, name="header-page"):
		super().__init__(QHBoxLayout, parent, name)

		self.setStyleSheet("src/qss/components/header_page.qss")
		
		title = QLabel("Projects", objectName=f"{name}-title")
		self.addWidget(title)

		self.layout.addStretch(0)
		self.setObjectName("header")
		loadStyle("src/qss/components/header.qss", self)

		layout = QHBoxLayout()
		layout.setContentsMargins(24, 96, 12, 12)
		
		title = QLabel("Projects")
		title.setObjectName("header-title")
		layout.addWidget(title)
		
		layout.addStretch(0)

		# import_btn = QPushButton("Import existing project")
		# import_btn.clicked.connect(lambda: self.importProject())
		# layout.addWidget(import_btn)

		# new_btn = QPushButton("Create new project")
		# new_btn.setObjectName("new_btn")
		# new_btn.clicked.connect(lambda: self.createProject())
		# layout.addWidget(new_btn)

		self.setLayout(layout)'''