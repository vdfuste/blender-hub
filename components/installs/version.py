from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from components.button import Button
from components.dropdown import Dropdown
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
		self.setFixedHeight(int(width * 0.35))

		# Image
		pixmap = QPixmap(self.data["image"])
		pixmap = pixmap.scaledToWidth(int(width * 0.7), mode=Qt.SmoothTransformation)

		image = QLabel()
		image.setPixmap(pixmap)
		self.addWidget(image)

		# Version content
		content = Frame("content", QVBoxLayout)
		content.setContentsMargins(12, 12, 12, 12)
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
		if self.is_installed: open(versions.paths[self.selected_version])
		else:
			for data in self.data["subversions"]:
				if self.selected_version != data["subversion"]: continue

				installBlender(self.selected_version, data["url"], self)
				
				break	

'''class SubVersionItem(Widget):
	def __init__(self, version, installed, url, name="sub-version-item"):
		super().__init__(QWidget, QHBoxLayout, name)

		self.layout.setContentsMargins(16, 20, 16, 16)
		self.layout.setSpacing(8)
		
		# Version
		self.addWidget(QLabel(f"Blender {version}", objectName=f"{name}-version"))
		
		# Show a message if is already installed
		if installed:
			self.addWidget(QLabel("Already installed", objectName=f"{name}-installed"))

		self.layout.addStretch(0)

		# Action Button
		action_btn = QPushButton("Install" if not installed else "Uninstall")
		action_btn.setObjectName("primary-btn" if not installed else "btn")
		action_btn.clicked.connect(lambda: self.handleClick(version, url, installed, parent=self.widget))
		self.addWidget(action_btn)

	def handleClick(self, version, url, installed, parent=None):
		if not installed: installBlender(version, url, parent)
		else: uninstallBlender(version, versions.paths[version], parent)

class VersionItem(QWidget):
	def __init__(self, width, data, name="version-item"):
		super().__init__()
		
		loadStyle("src/qss/pages/installs/version.qss", self)

		# Width hardcoded adjust. Still don't know why 32.
		width -= 32
		
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)

		title = QLabel(f'Blender {data["version"]}', objectName="version-title")
		layout.addWidget(title)

		image = QPixmap(data["image"])
		self.header_image = QLabel(objectName="version-image")
		self.header_image.setPixmap(image.scaledToWidth(width, mode=QtCore.Qt.SmoothTransformation))
		self.header_image.setFixedSize(width, int(width/3))
		self.header_image.setAlignment(Qt.AlignTop)
		layout.addWidget(self.header_image)

		# Sub-versions
		for subdata in data["subversions"]:
			layout.addWidget(SubVersionItem(
				subdata["subversion"],
				subdata["subversion"] in versions.installed,
				subdata["url"]
			).widget)
			
		self.setLayout(layout)'''
