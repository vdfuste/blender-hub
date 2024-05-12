from sys import platform
from subprocess import run, CalledProcessError
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget

from utils.scrapping import getAvailableVersions

from globals import BLENDER_DOWNLOADS_URL

'''
TO-DO list:
 - Scrap the web to see all available versions.
 - Check if the selected version is already installed.
 - Add blender to PATH?
'''

class InstallsPage(QWidget):
	def __init__(self):
		super().__init__()

		getAvailableVersions()
		
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		page = QWidget()
		page.setContentsMargins(0, 0, 0, 0)
		page.setObjectName("installs_page")
		page_layout = QVBoxLayout()

		#install_stable_button = QPushButton("Install last stable version (4.1.1)")
		#install_stable_button.clicked.connect(lambda: self.install_stable("4.1", "1"))
		#page_layout.addWidget(install_stable_button)

		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)

	def install_stable(self, mayor, minor):
		blender_url = "{BLENDER_DOWNLOADS_URL}{0}/".format(mayor)
		file_name = "blender-{0}.{1}-".format(mayor, minor)
		
		# Getting the extension and user based on the OS
		if platform == "linux" or platform == "linux2":
			os = "linux-x64"
			extension = ".tar.xz"
			commands = [
				"mkdir -p temp",
				"wget {0} -P temp".format(blender_url + file_name + os + extension),
				"tar -xf {0}".format("temp/" + file_name + os + extension),
				"sudo mv {0} /opt/blender".format(file_name + os),
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
			print("Failed to install Blender {0}.{1}".format(mayor, minor))
