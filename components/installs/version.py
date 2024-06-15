from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy

from components.custom.widget import Widget

from utils.read import loadStyle
from utils.install import installBlender, uninstallBlender

from globals import versions

class SubVersionItem(Widget):
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
			
		self.setLayout(layout)
