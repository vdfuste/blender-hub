from sys import platform
from subprocess import run, CalledProcessError
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from components.custom.widget import Widget
from components.header_page import HeaderPage
from components.installs.header import VersionButtonsHeader
from components.scroll_list import ScrollList
from components.installs.version import VersionItem

from utils.read import loadStyle

from globals import downloads

'''
TO-DO list:
 - Scrap the web to see all available versions.
 - Check if the selected version is already installed.
 - Add blender to PATH?
'''

class InstallsPage(QWidget):
	def __init__(self, title, name="installs-page"):
		super().__init__()
		
		loadStyle("src/qss/pages/installs/style.qss", self)

		page_layout = QVBoxLayout()
		page_layout.setContentsMargins(0, 0, 0, 0)
		page_layout.setSpacing(0)

		# Header Page
		header_page = HeaderPage(title)
		header_page.addWidget(VersionButtonsHeader())
		header_page.parent(page_layout)
		# page_layout.addWidget(header_page)

		#Scroll List
		self.versions_list = ScrollList()
		self.versions_list.layout.setContentsMargins(12, 8, 24, 8)
		self.versions_list.layout.setSpacing(12)
		self.versions_list.populate(downloads.versions[0]["cards"], lambda data, index: VersionItem(self.width(), data))
		self.versions_list.parent(page_layout)
		
		# install_stable_button = QPushButton("Install last stable version (4.1.1)")
		# install_stable_button.clicked.connect(lambda: self.install_stable("4.1", "1"))
		# self.addWidget(install_stable_button)
		
		self.setLayout(page_layout)
	
	def install_stable(self, mayor, minor):
		blender_url = f"{BLENDER_ALL_VERSIONS_URL}/Blender{mayor}/"
		file_name = f"blender-{mayor}.{minor}-"
		
		# Getting the extension and user based on the OS
		if platform == "linux" or platform == "linux2":
			os = "linux-x64"
			extension = ".tar.xz"
			commands = [
				"mkdir -p temp",
				f"wget {blender_url + file_name + os + extension} -P temp",
				f"tar -xf temp/{file_name + os + extension}",
				f"sudo mv {file_name + os} /opt/blender",
				#"sudo ln -s /opt/blender/blender /usr/local/bin/blender",
				"rm -rf temp"
			]
		elif platform == "win32":
			extension = "windows-x64.zip/"
			url = blender_url + file_name + extension
			commands = []
		elif platform == "darwin":
			extension = "macos-x64.dmg/"
			url = blender_url + file_name + extension
			commands = []
		
		try:
			for command in commands:
				run(command.split(), check=True)
		
		except CalledProcessError:
			print(f"Failed to install Blender {mayor}.{minor}")

	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.versions_list.populate(downloads.versions[0]["cards"], lambda data, index: VersionItem(self.width(), data))
