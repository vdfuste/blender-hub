from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from components.custom.button import Button
from components.custom.dropdown import Dropdown
from components.custom.frame import Frame

from utils.install import installBlender, uninstallBlender
from utils.blender.run import open

from globals import versions

class VersionItem(Frame):
	def __init__(self, width, data, name="version-item"):
		super().__init__(name)

		self.data = data

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

		title = QLabel(f"Blender {self.data["version"]}")
		title.setObjectName("title")
		content.addWidget(title)

		content.layout.addStretch()

		# Split all versions in Installed and Available
		subversions = [
			{ "title": "INSTALLED", "items": [] },
			{ "title": "AVAILABLE", "items": [] }
		]
		for data in self.data["subversions"]:
			sub = data["subversion"]
			index = 0 if sub in versions.installed else 1 # 0=INSTALLED, 1=AVAILABLE

			subversions[index]["items"].append(sub)

		dropdown = Dropdown()
		dropdown.setOptions(subversions)
		dropdown.optionSelected.connect(lambda option: self.updateData(option))
		content.addWidget(dropdown)

		self.action_button = Button()
		self.action_button.setObjectName("primary-button")
		self.action_button.clicked.connect(self.actionButtonClicked)
		content.addWidget(self.action_button)

		self.updateData(dropdown.getOption())

	def updateData(self, version):
		self.selected_version = version
		self.is_installed = version in versions.installed
		
		action_label = "Open" if self.is_installed else "Install"
		
		self.action_button.setLabel(f"{action_label} Blender {version}")

	def actionButtonClicked(self):
		if self.is_installed:
			open(versions.paths[self.selected_version])
		else:
			for data in self.data["subversions"]:
				if self.selected_version != data["subversion"]: continue

				installBlender(self.selected_version, data["url"], self)
				
				break
