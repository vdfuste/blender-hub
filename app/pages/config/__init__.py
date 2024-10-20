from os import listdir, path
from shutil import copy, SameFileError

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QCheckBox, QMessageBox

from app.components.custom.frame import Frame
from app.components.pages.header import HeaderPage

from app.globals import config, CONFIG_USER_FOLDER

class ConfigPage(Frame):
	def __init__(self, title, name="config-page"):
		super().__init__(name)

		self.initUI(title)

	def initUI(self, title):
		self.layout.setAlignment(Qt.AlignTop)

		# Header Page
		header_page = HeaderPage(title)
		self.addWidget(header_page)

		'''if path.isdir(CONFIG_USER_FOLDER):
			# Content
			content = Widget(QWidget, QHBoxLayout)
			content.widget.setMaximumWidth(720)
			content.widget.setContentsMargins(24, 24, 24, 24)
			content.layout.setSpacing(24)
			content.parent(page_layout)
			
			# Left section
			left_section = Widget(QWidget, QVBoxLayout)
			left_section.layout.setAlignment(Qt.AlignTop)
			left_section.layout.setSpacing(12)
			left_section.parent(content)

			from_label = QLabel("Copy from:", objectName="copy-label")
			left_section.addWidget(from_label)
			
			self.from_combo = QComboBox()
			self.from_combo.addItems(config.versions)
			self.from_combo.currentTextChanged.connect(lambda version: self.versionChanged(version))
			left_section.addWidget(self.from_combo)

			# All available config files
			self.checkboxes_list = []
			self.checkboxes = Widget(QWidget, QVBoxLayout)
			self.checkboxes.parent(left_section)
			self.checkboxes.layout.setSpacing(12)
			
			# Adding the current files
			self.versionChanged(self.from_combo.currentText())
			
			# Center section
			center_section = Widget(QWidget, QVBoxLayout)
			center_section.layout.setAlignment(Qt.AlignTop)
			center_section.layout.setSpacing(12)
			center_section.parent(content)

			to_label = QLabel("Copy to:", objectName="copy-label")
			center_section.addWidget(to_label)
			
			self.to_combo = QComboBox()
			self.to_combo.addItems(config.versions)
			center_section.addWidget(self.to_combo)

			# Right section
			right_section = Widget(QWidget, QVBoxLayout)
			right_section.layout.setAlignment(Qt.AlignTop)
			right_section.layout.setContentsMargins(0, 32, 0, 0)
			right_section.parent(content)
			
			# Copy button
			copy_btn = QPushButton("Copy config files", objectName="primary-border-button")
			copy_btn.clicked.connect(lambda: self.copyFiles())
			right_section.addWidget(copy_btn)'''

	def versionChanged(self, version):
		# Flush checkboxes
		self.checkboxes_list = []
		while self.checkboxes.layout.count():
			item = self.checkboxes.layout.takeAt(0)
			if item.widget():
				item.widget().deleteLater()
		
		for file in listdir(path.join(CONFIG_USER_FOLDER, version, "config")):
			if ".blend" in file:
				checkbox = QCheckBox(file)
				self.checkboxes_list.append(checkbox)
				self.checkboxes.addWidget(self.checkboxes_list[-1])

	def copyFiles(self):
		from_version = self.from_combo.currentText()
		to_version = self.to_combo.currentText()
		
		files = []
		for check in self.checkboxes_list:
			if check.checkState():
				files.append(path.join(CONFIG_USER_FOLDER, from_version, "config", check.text()))

		# Do nothing if no files are selected
		if len(files) == 0:
			return
		
		try:
			for file in files:
				copy(file, path.join(CONFIG_USER_FOLDER, to_version, "config"))
			message = "Files copied succesfully!"
		except SameFileError: message = "Same version detected. Files not copied."
		except FileNotFoundError as e: message = e
		except PermissionError as e: message = e
		except Exception as e: message = e

		# Show a message to improve the feedback with the user
		feedback_message = QMessageBox()
		feedback_message.setIcon(QMessageBox.Warning)
		feedback_message.setWindowTitle("Blender Hub")
		feedback_message.setText(message)
		feedback_message.addButton(QPushButton("Close"), QMessageBox.AcceptRole)
		feedback_message.exec_()
