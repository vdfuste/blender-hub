from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

from app.components.custom.frame import Frame
from app.components.custom.button import Button

class OptionsButtonsHeader(Frame):
	onCreateProject = pyqtSignal()
	onImportProject = pyqtSignal()
	
	def __init__(self):
		super().__init__()
		
		# self.loadStyle(__file__)
		
		self.layout.setContentsMargins(0, 0, 0, 8)
		self.layout.setSpacing(8)
		self.layout.setAlignment(Qt.AlignBottom)
		
		import_button = Button("Import existing project")
		import_button.setObjectName("border-button")
		import_button.clicked.connect(self.onImportProject.emit)
		self.addWidget(import_button)
		
		new_button = Button("Create new project")
		new_button.setObjectName("primary-button")
		new_button.clicked.connect(self.onCreateProject.emit)
		self.addWidget(new_button)
