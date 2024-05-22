from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy

from components.custom.widget import Widget

class SubVersionItem(Widget):
	def __init__(self, version, subversion, installed=False, name="sub-version-item"):
		super().__init__(QWidget, QHBoxLayout, name)

		self.layout.setContentsMargins(16, 20, 16, 16)
		self.layout.setSpacing(8)
		
		# Version
		self.addWidget(QLabel(f"Blender {version}.{subversion}", objectName=f"{name}-version"))
		
		# Show a message if is already installed
		if installed:
			self.addWidget(QLabel("Already installed", objectName=f"{name}-installed"))

		self.layout.addStretch(0)

		# Action Button
		action_btn = QPushButton("Install" if not installed else "Uninstall")
		action_btn.setObjectName("primary-btn" if not installed else "btn")
		self.addWidget(action_btn)
		

class VersionItem(Widget):
	def __init__(self, data, index):
		super().__init__(QWidget, QVBoxLayout, "version-item")

		self.loadStyle("src/qss/pages/installs/version.qss")
		
		title = QLabel("Blender 4.1", objectName="version-title")
		self.addWidget(title)

		image = QPixmap("src/images/blender_4_1_splash.jpg")
		self.header_image = QLabel(objectName="version-image")
		self.header_image.setPixmap(image.scaledToWidth(750, mode=QtCore.Qt.SmoothTransformation))
		self.header_image.setFixedSize(750, 200)
		self.header_image.setAlignment(Qt.AlignTop)
		self.addWidget(self.header_image)

		# Sub-versions
		self.addWidget(SubVersionItem("4.1", "1", installed=True).widget)
		self.addWidget(SubVersionItem("4.1", "0").widget)