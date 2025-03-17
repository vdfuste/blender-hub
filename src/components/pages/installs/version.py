from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel

from components.custom.button import Button, OptionsButton
from components.custom.dropdown import Dropdown
from components.custom.frame import Frame

from pages.dialogs.install import InstallDialog
from pages.dialogs.uninstall import UninstallDialog

from utils.install import uninstallBlender
from utils.blender.run import open_blender

from globals import versions

class VersionItem(Frame):
	def __init__(self, width, data, name="version-item"):
		super().__init__(name)

		self.data = data
		self.subversions = []

		self.selected_version = None
		self.is_installed = None

		self.initUI(width)

	def initUI(self, width):
		self.loadStyle(__file__)
		self.setFixedHeight(int(width * 0.33))

		# Image
		pixmap = QPixmap(self.data["image"])
		pixmap = pixmap.scaledToWidth(int(width * 0.67), mode=Qt.SmoothTransformation)

		image = QLabel()
		image.setPixmap(pixmap)
		self.addWidget(image)

		# Version content
		content = Frame("content", QVBoxLayout)
		content.layout.setSpacing(12)
		self.addWidget(content)

		header = Frame("header", QHBoxLayout)
		
		title = QLabel(f"Blender {self.data["version"]}")
		title.setObjectName("title")
		header.addWidget(title)

		header.layout.addStretch()

		self._options = OptionsButton()
		self._options.addAction("Delete this version", self.deleteSelectedVersion)
		header.addWidget(self._options)

		content.addWidget(header)
		content.layout.addStretch()

		self.splitSubversions()
		
		dropdown = Dropdown()
		dropdown.setOptions(self.subversions)
		dropdown.optionSelected.connect(lambda option: self.updateState(option))
		content.addWidget(dropdown)

		self.action_button = Button()
		self.action_button.setObjectName("primary-button")
		self.action_button.clicked.connect(self.actionButtonClicked)
		content.addWidget(self.action_button)

		self.updateState(dropdown.getOption())

	def splitSubversions(self):
		versions.check()

		self.subversions = [
			{ "title": "INSTALLED", "items": [] },
			{ "title": "AVAILABLE", "items": [] }
		]

		for data in self.data["subversions"]:
			sub = data["subversion"]
			index = 0 if sub in versions.installed else 1 # 0=INSTALLED, 1=AVAILABLE

			self.subversions[index]["items"].append(sub)
	
	def updateState(self, version):
		self.selected_version = version
		self.is_installed = version in versions.installed
		
		action_label = "Open" if self.is_installed else "Install"
		self.action_button.setLabel(f"{action_label} Blender {version}")

		self._options.setEnabled(self.is_installed)

	def actionButtonClicked(self):
		if self.is_installed:
			open_blender(versions.paths[self.selected_version])
		else:
			for data in self.data["subversions"]:
				if self.selected_version != data["subversion"]:
					continue
				
				install = InstallDialog(self.selected_version, data["url"], parent=self)
				install.exec_()

				self.splitSubversions()
				self.updateState(self.selected_version)
				
				break

	def deleteSelectedVersion(self):
		if self.is_installed:
			uninstall = UninstallDialog(self.selected_version, parent=self)
			uninstall.exec_()

			self.splitSubversions()
			self.updateState(self.selected_version)
