from os import path
from subprocess import Popen, CalledProcessError

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from utils.read import loadStyle

from components.file_dialog import FileDialog

from globals import versions, DOCUMENTS_FOLDER, SCREEN_GEOMETRY

'''
TO-DO list:
 - Close application when a project is created.
'''

class NewProject(QDialog):
	def __init__(self, parent=None):
		super().__init__()
		
		width = 640
		height = 300
		pos_x = int(SCREEN_GEOMETRY.width()/2 - width/2)
		pos_y = int(SCREEN_GEOMETRY.height()/2 - height/2)
		
		loadStyle("src/qss/pages/dialogs/new_project.qss", self)

		# Init UI
		self.setParent(parent)
		self.setObjectName("new-project-page")
		self.setGeometry(pos_x, pos_y, width, height)
		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.Tool)

		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignTop)
		
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
		
		project_path_btn = QPushButton("...", objectName="border-btn")
		project_path_btn.clicked.connect(self.changePath)
		path_layout.addWidget(project_path_btn)
		
		wrap_path.setLayout(path_layout)
		layout.addWidget(wrap_path)

		# Blender version
		version_label = QLabel("Project version:", objectName="label")
		layout.addWidget(version_label)

		self.versions_combo = QComboBox()
		self.versions_combo.addItems(versions.installed)
		layout.addWidget(self.versions_combo)

		# Buttons
		wrap_buttons = QWidget()
		buttons_layout = QHBoxLayout()
		buttons_layout.setContentsMargins(0, 10, 0, 0)
		buttons_layout.addSpacing(0)
		
		close_btn = QPushButton("Cancel", objectName="border-btn")
		close_btn.clicked.connect(lambda: self.hide())
		buttons_layout.addWidget(close_btn)
		
		self.create_btn = QPushButton("Create new project", objectName="primary-border-btn")
		self.create_btn.setDisabled(True)
		# self.create_btn.clicked.connect(self.createNewProject)
		self.create_btn.clicked.connect(self.accept)
		buttons_layout.addWidget(self.create_btn)
		
		wrap_buttons.setLayout(buttons_layout)
		layout.addWidget(wrap_buttons)

		self.setLayout(layout)

	def open(self):
		self.reset()
		return self.exec_()
	
	def reset(self):
		self.project_name.setText("My Project")
		self.project_name.setFocus(Qt.FocusReason.ActiveWindowFocusReason)
	
	def nameTextChanged(self):
		self.create_btn.setDisabled(self.project_name.text() == "")

	def changePath(self):
		file_path = FileDialog.newBlenderFile(self)
		
		if file_path:
			self.project_path.setText(file_path)

	def getProjectData(self):
		_file_name = path.join(self.project_path.text(), f"{self.project_name.text()}.blend")
		_blender_version = self.versions_combo.currentText()

		return [_file_name, _blender_version]
	
	'''def createNewProject(self):
		_file_name = path.join(self.project_path.text(), f"{self.project_name.text()}.blend")
		_blender_version = versions.paths[self.versions_combo.currentText()]

		new_project(_file_name, _blender_version)
		
		self.hide()'''
