from os import path
from subprocess import Popen, CalledProcessError
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from utils.read import loadStyle

from components.fileDialog import FileDialog

from globals import DOCUMENTS_FOLDER

'''
TO-DO list:
 - Handle names with spaces.
 - Close application when a project is created.
'''
class NewProject(QWidget):
	def __init__(self):
		super().__init__()

		self.setObjectName("new-project-page")
		self.setGeometry(100, 100, 640, 20)
		loadStyle("src/qss/pages/floating/new_project.qss", self)

		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignTop)
		# layout.setContentsMargins(0, 0, 0, 0)
		# layout.setSpacing(0)
		
		# Page Content
		title_label = QLabel("Create new project", objectName="title")
		layout.addWidget(title_label)
		
		# Project name
		name_label = QLabel("Project name:", objectName="label")
		layout.addWidget(name_label)

		self.project_name = QLineEdit(objectName="input-text")
		self.project_name.textChanged.connect(self.nameTextChanged)
		layout.addWidget(self.project_name)

		# Project path
		path_label = QLabel("Save project on:", objectName="label")
		layout.addWidget(path_label)

		wrap_path = QWidget()
		path_layout = QHBoxLayout()
		path_layout.setContentsMargins(0, 0, 0, 0)

		self.project_path = QLineEdit(DOCUMENTS_FOLDER, objectName="input-text")
		path_layout.addWidget(self.project_path)
		
		project_path_btn = QPushButton("...", objectName="btn")
		project_path_btn.clicked.connect(self.changePath)
		path_layout.addWidget(project_path_btn)
		
		wrap_path.setLayout(path_layout)
		layout.addWidget(wrap_path)

		# Buttons
		wrap_buttons = QWidget()
		buttons_layout = QHBoxLayout()
		
		buttons_layout.addSpacing(0)
		
		close_btn = QPushButton("Cancel", objectName="btn")
		close_btn.clicked.connect(lambda: self.hide())
		buttons_layout.addWidget(close_btn)
		
		self.create_btn = QPushButton("Create new project", objectName="primary-btn")
		self.create_btn.setDisabled(True)
		self.create_btn.clicked.connect(self.createNewProject)
		buttons_layout.addWidget(self.create_btn)
		
		wrap_buttons.setLayout(buttons_layout)
		layout.addWidget(wrap_buttons)

		self.setLayout(layout)

	def reset(self):
		self.project_name.setText("My Project")
		self.project_name.setFocus(Qt.FocusReason.ActiveWindowFocusReason)
	
	def nameTextChanged(self):
		self.create_btn.setDisabled(self.project_name.text() == "")

	def changePath(self):
		file_path = FileDialog.newBlenderFile(self)
		
		if file_path:
			self.project_path.setText(file_path)

	def createNewProject(self):
		self.hide()
		
		try:
			blender_path = f"/opt/blender/blender-4.1.1-linux-x64/blender"
			file_name = path.join(self.project_path.text(), f"{self.project_name.text()}.blend")

			Popen(f"{blender_path} -P utils/new.py {file_name}".split(' '))
		
		except CalledProcessError:
			print(f"Error opening {self.project_name} project.")
