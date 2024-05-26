from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QScrollArea, QMenu, QComboBox, QMessageBox, QSizePolicy

from components.custom.widget import Widget

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
	def __init__(self, data, index, callback, name="item"):
		super().__init__()

		self.splitData(data)

		#Init UI
		self.setFixedHeight(96)

		wrap_layout = QHBoxLayout()
		wrap_layout.setContentsMargins(0, 0, 0, 0)
		wrap_layout.setSpacing(0)
		
		item = QWidget(objectName=name)
		item.setFixedHeight(96)
		layout = QHBoxLayout()
		layout.setContentsMargins(24, 0, 56, 0)
		layout.setSpacing(0)
		
		# Left section content
		left_section_scroll = QScrollArea()
		left_section_scroll.setFixedHeight(45)
		left_section_scroll.setContentsMargins(0, 0, 0, 0)
		left_section_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		left_section_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		left_section_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		
		left_section = QWidget()
		left_section.setObjectName(f"{name}-left")
		left_section.setFixedHeight(40)
		left_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		left_section_layout = QVBoxLayout()
		left_section_layout.setContentsMargins(24, 0, 24, 0)
		left_section_layout.setSpacing(0)

		# Title and path
		file_name_label = QLabel(
			self.project_name
			.replace(".blend", "")
			.replace("_", " ")
			.capitalize()
		)
		file_name_label.setObjectName("file_name")
		left_section_layout.addWidget(file_name_label)

		file_path_label = QLabel(self.project_path)
		file_path_label.setObjectName("file_path")
		left_section_layout.addWidget(file_path_label)

		left_section.setLayout(left_section_layout)
		left_section_scroll.setWidget(left_section)
		layout.addWidget(left_section_scroll)


		# Center section content
		center_section = QWidget()
		center_section.setFixedWidth(136)
		center_section.setObjectName(f"{name}-center")
		center_section_layout = QVBoxLayout()
		center_section_layout.setContentsMargins(24, 0, 24, 0)

		# Last modification date
		file_last = QLabel(calculateTimeAgo(self.project_date))
		center_section_layout.addWidget(file_last)

		center_section.setLayout(center_section_layout)
		layout.addWidget(center_section)


		# Right section content
		right_section = QWidget()
		right_section.setFixedWidth(136)
		right_section.setObjectName(f"{name}-right")
		right_section_layout = QHBoxLayout()
		right_section_layout.setContentsMargins(24, 0, 0, 0)

		# Version and options
		self.versions_combo = QComboBox()
		self.versions_combo.setObjectName("versions")
		self.versions_combo.addItems(self.getVersions())
		right_section_layout.addWidget(self.versions_combo)

		options = QPushButton("⋮")
		options.setObjectName("options")
		options_menu = QMenu()
		remove_action = options_menu.addAction("Remove from Blender Hub")
		remove_action.triggered.connect(lambda: callback(index, False))
		delete_action = options_menu.addAction("Delete file from disk")
		delete_action.triggered.connect(lambda: self.openWarningMessage(index, callback))
		options.setMenu(options_menu)
		options.clicked.connect(options_menu.popup)
		right_section_layout.addWidget(options)

		right_section.setLayout(right_section_layout)
		layout.addWidget(right_section)

		item.setLayout(layout)
		wrap_layout.addWidget(item)

		self.setLayout(wrap_layout)
	
	def splitData(self, data):
		# Gets the full path, last modified date and current version from data
		_path_name, self.project_date, self.project_version = data.split(';')
		
		# Split to path and name from the full path
		self.project_path, self.project_name = path.split(_path_name)
	
	def getVersions(self):
		_versions = []

		for version in versions.installed:
			if version != self.project_version:
				_versions.append(version)

		_versions.append(self.project_version)
		_versions.reverse()

		return _versions

	def mousePressEvent(self, event):
		_file_name = path.join(self.project_path, self.project_name)
		_version = versions.paths[self.versions_combo.currentText()]

		print("BLENDER HUB: " + _version)

		open_project(_file_name, _version)

	def openWarningMessage(self, index, callback):
		warningMessage = QMessageBox()
		warningMessage.setIcon(QMessageBox.Warning)
		warningMessage.setText("Are you sure you want to delete the file from your disk?")
		warningMessage.setWindowTitle("Blender Hub says:")

		delete_btn = QPushButton("Delete it")
		delete_btn.clicked.connect(lambda: callback(index, True))
		warningMessage.addButton(delete_btn, QMessageBox.AcceptRole)
		
		remove_btn = QPushButton("Just remove it from list")
		remove_btn.clicked.connect(lambda: callback(index, False))
		warningMessage.addButton(remove_btn, QMessageBox.ActionRole)
		
		cancel_btn = QPushButton("Cancel")
		warningMessage.addButton(cancel_btn, QMessageBox.RejectRole)

		warningMessage.setDefaultButton(cancel_btn)
		warningMessage.exec_()
