from os import path
from time import ctime
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QScrollArea, QMenu, QComboBox, QMessageBox, QSizePolicy

from components.custom.widget import Widget
from components.dropdown import Dropdown

from utils.time import calculateTimeAgo
from utils.blender.run import open_project

from globals import versions

'''
TO-DO list:
 * Versions
  - Highlight the current version
  - Mark the current version as uninstalled if is not installed
 
 * Open project:
  - Check if the file exists before open it
  - Close Blender Hub when a file is open
'''

class Item(QWidget):
	projectOpened = pyqtSignal(str, int, str)
	projectRemoved = pyqtSignal(int, bool)
	
	def __init__(self, data, index, name="item"):
		super().__init__()

		self.index = index

		self.initUI(data, name)

	def initUI(self, data, name):
		self.setFixedHeight(96)
		
		# Gets the full path, last modified date and current version from data
		self.project_date = data["date"]
		path_name = data["file_name"]
		project_version = data["version"]

		# Split to path and name from the full path
		self.project_path, self.project_name = path.split(path_name)

		wrap_layout = QHBoxLayout()
		wrap_layout.setContentsMargins(0, 0, 0, 0)
		wrap_layout.setSpacing(0)
		
		item = QWidget(objectName=name)
		layout = QHBoxLayout()
		layout.setContentsMargins(24, 0, 32, 0)
		layout.setSpacing(0)
		
		# Left section content
		left_section_scroll = QScrollArea()
		left_section_scroll.setObjectName(f"{name}-left")
		left_section_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		left_section_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		left_section_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		
		left_section = QWidget()
		left_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		left_section_layout = QVBoxLayout()
		left_section_layout.setContentsMargins(0, 0, 0, 0)
		left_section_layout.setSpacing(0)

		# Title and path
		file_name_label = QLabel(
			self.project_name
			.replace(".blend", "")
			.replace("_", " ")
			.capitalize()
		)
		file_name_label.setObjectName("file_name")
		file_name_label.setFixedHeight(32)
		left_section_layout.addWidget(file_name_label)

		file_path_label = QLabel(self.project_path)
		file_path_label.setObjectName("file_path")
		left_section_layout.addWidget(file_path_label)

		left_section.setLayout(left_section_layout)
		left_section_scroll.setWidget(left_section)
		layout.addWidget(left_section_scroll)


		# Center section content
		center_section = QWidget()
		center_section.setObjectName(f"{name}-center")
		center_section.setFixedWidth(156)
		center_section_layout = QHBoxLayout()
		center_section_layout.setContentsMargins(24, 0, 0, 0)

		# Last modification date
		file_last = QLabel(calculateTimeAgo(self.project_date))
		center_section_layout.addWidget(file_last)

		center_section.setLayout(center_section_layout)
		layout.addWidget(center_section)


		# Right section content
		right_section = QWidget()
		right_section.setObjectName(f"{name}-right")
		right_section.setFixedWidth(150)
		right_section_layout = QHBoxLayout()
		right_section_layout.setContentsMargins(8, 0, 0, 0)

		# Version and options		
		self.dropdown = Dropdown()
		self.dropdown.setOptions([
			{ "title": "Current", "items": [project_version] },
			{ "title": "Installed", "items": self.getInstalledVersions(project_version) },
		])
		right_section_layout.addWidget(self.dropdown)

		# Options button
		options = QPushButton("⋮")
		options.setObjectName("options")
		options_menu = QMenu()
		remove_action = options_menu.addAction("Remove from Blender Hub")
		remove_action.triggered.connect(lambda: self.projectRemoved.emit(self.index, False))
		delete_action = options_menu.addAction("Delete file from disk")
		delete_action.triggered.connect(self.openWarningMessage)
		options.setMenu(options_menu)
		options.clicked.connect(options_menu.popup)
		right_section_layout.addWidget(options)

		right_section.setLayout(right_section_layout)
		layout.addWidget(right_section)

		item.setLayout(layout)
		wrap_layout.addWidget(item)

		self.setLayout(wrap_layout)
	
	def mousePressEvent(self, event):
		file_name = path.join(self.project_path, self.project_name)
		version = versions.paths[self.dropdown.getOption()]
		
		self.projectOpened.emit(file_name, self.index, self.dropdown.getOption())

		open_project(file_name, version)
	
	def getInstalledVersions(self, currentVersion):
		installed = []

		for version in versions.installed:
			if version != currentVersion:
				installed.append(version)

		return installed

	def openWarningMessage(self):
		warning_message = QMessageBox()
		warning_message.setIcon(QMessageBox.Warning)
		warning_message.setText("Are you sure you want to delete the file from your disk?")
		warning_message.setWindowTitle("Blender Hub says:")

		delete_btn = QPushButton("Delete it")
		delete_btn.clicked.connect(lambda: self.projectRemoved.emit(self.index, True))
		warning_message.addButton(delete_btn, QMessageBox.AcceptRole)
		
		remove_btn = QPushButton("Just remove it from list")
		remove_btn.clicked.connect(lambda: self.projectRemoved.emit(self.index, False))
		warning_message.addButton(remove_btn, QMessageBox.ActionRole)
		
		cancel_btn = QPushButton("Cancel")
		warning_message.addButton(cancel_btn, QMessageBox.RejectRole)

		warning_message.setDefaultButton(cancel_btn)
		warning_message.exec_()
