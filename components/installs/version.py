from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy

from components.custom.widget import Widget
from utils.read import loadStyle

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

class VersionItem(QWidget):
	def __init__(self, width, data="", index="", name="version-item"):
		super().__init__()
		
		loadStyle("src/qss/pages/installs/version.qss",self)

		width -= 32
		
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)

		title = QLabel("Blender 4.1", objectName="version-title")
		layout.addWidget(title)

		image = QPixmap("src/images/blender_4_1_splash.jpg")
		self.header_image = QLabel(objectName="version-image")
		self.header_image.setPixmap(image.scaledToWidth(width, mode=QtCore.Qt.SmoothTransformation))
		self.header_image.setFixedSize(width, int(width/3))
		self.header_image.setAlignment(Qt.AlignTop)
		layout.addWidget(self.header_image)

		# Sub-versions
		layout.addWidget(SubVersionItem("4.1", "1", installed=True).widget)
		layout.addWidget(SubVersionItem("4.1", "0").widget)

		self.setLayout(layout)
