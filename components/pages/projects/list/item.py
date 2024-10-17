from os import path
from time import ctime

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QMenu, QMessageBox

from components.custom.frame import Frame
from components.custom.dropdown import Dropdown
from components.custom.scroll import ScrollArea

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

class Item(Frame):
	projectOpened = pyqtSignal(str, int, str)
	projectRemoved = pyqtSignal(int, bool)
	
	def __init__(self, data, index, name="item"):
		super().__init__(name)

		# Split to path and name from the full path
		self.project_path, self.project_name = path.split(data["file_name"])
		
		self.index = index
		self.project_date = data["date"]
		self.project_version = data["version"]

		self.initUI()

	def initUI(self):
		self.setFixedHeight(96)
		
		# LEFT CONTENT
		left_section = ScrollArea("left-section")
		left_section.hideHorizontalScroll()
		left_section.hideVerticalScroll()

		# Title and path
		file_name_label = QLabel(
			self.project_name
			.replace(".blend", "")
			.replace("_", " ")
			.capitalize()
		)
		file_name_label.setObjectName("file_name")
		file_name_label.setFixedHeight(32)
		left_section.addItem(file_name_label)

		file_path_label = QLabel(self.project_path)
		file_path_label.setObjectName("file_path")
		left_section.addItem(file_path_label)

		self.addWidget(left_section)


		# CENTER CONTENT
		center_section = Frame("center-section")
		center_section.setFixedWidth(150)

		# Last modification date
		file_last = QLabel(calculateTimeAgo(self.project_date))
		center_section.addWidget(file_last)

		self.addWidget(center_section)


		# RIGHT CONTENT
		right_section = Frame("right-section")
		right_section.setFixedWidth(150)

		# Versions Dropdown		
		self.dropdown = Dropdown()
		self.dropdown.setOptions([
			{ "title": "Current", "items": [self.project_version] },
			{ "title": "Installed", "items": self.getInstalledVersions(self.project_version) },
		])
		right_section.addWidget(self.dropdown)

		# Options Button and Menu
		options_menu = QMenu()
		remove_action = options_menu.addAction("Remove from Blender Hub")
		remove_action.triggered.connect(lambda: self.projectRemoved.emit(self.index, False))
		delete_action = options_menu.addAction("Delete file from disk")
		delete_action.triggered.connect(self.openWarningMessage)
		
		options = QPushButton("⋮")
		options.setObjectName("options")
		options.setMenu(options_menu)
		options.clicked.connect(options_menu.popup)
		right_section.addWidget(options)

		self.addWidget(right_section)
	
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
