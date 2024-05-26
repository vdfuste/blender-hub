from os import mkdir, path
from sys import platform
from subprocess import run, CalledProcessError

from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy

from components.custom.widget import Widget
from utils.read import loadStyle

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
		action_btn.clicked.connect(lambda: self.install_stable(url, installed))
		self.addWidget(action_btn)

	def install_stable(self, url, installed):
		if installed:
			return

		
		if platform == "linux" or platform == "linux2":
			extension = ".tar.xz"
			blender_file = path.split(url)[-1].replace(extension, "")
			
			commands = [
				"mkdir -p temp",
				f"wget {url} -P temp",
				f"tar -xf temp/{blender_file + extension}",
				f"sudo mv {blender_file} /opt/blender",
				#"sudo ln -s /opt/blender/blender /usr/local/bin/blender",
				"rm -rf temp"
			]
		
		elif platform == "win32":
			# extension = ".msi"
			# blender_file = path.split(url)[-1].replace(extension)

			commands = []
		
		elif platform == "darwin":
			# extension = ".dmg"
			# blender_file = path.split(url)[-1].replace(extension)

			commands = []
		
		try:
			for command in commands:
				run(command.split(), check=True)
		
		except CalledProcessError:
			print(f"Failed to install Blender {mayor}.{minor}")

class VersionItem(QWidget):
	def __init__(self, width, data, name="version-item"):
		super().__init__()
		
		loadStyle("src/qss/pages/installs/version.qss",self)

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
