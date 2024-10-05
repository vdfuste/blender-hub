from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

from components.button import Button

class OptionsButtonsHeader(QWidget):
	def __init__(self, createProject, importProject):
		super().__init__()
		
		# loadStyle("components/projects/header/style.qss", self)
		
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 8)
		layout.setSpacing(8)
		layout.setAlignment(Qt.AlignBottom)
		
		'''import_btn = QPushButton("Import existing project")
		import_btn.setObjectName("border-btn")
		import_btn.clicked.connect(lambda: importProject())
		layout.addWidget(import_btn)

		new_btn = QPushButton("Create new project")
		new_btn.setObjectName("primary-border-btn")
		new_btn.clicked.connect(lambda: createProject())
		layout.addWidget(new_btn)'''
		
		import_button = Button("Import existing project")
		import_button.setObjectName("border-button")
		import_button.clicked.connect(lambda: importProject())
		layout.addWidget(import_button)
		
		new_button = Button("Create new project")
		new_button.setObjectName("primary-button")
		new_button.clicked.connect(lambda: createProject())
		layout.addWidget(new_button)

		self.setLayout(layout)
