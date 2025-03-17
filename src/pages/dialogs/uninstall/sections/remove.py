import urllib.request
from os import path
from subprocess import run
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QLabel

from components.custom.dialog import Section, TextInput
from components.custom.frame import Frame

from globals import versions

class RemoveSection(Section):
	def __init__(self, version):
		super().__init__()

		self.version = version
		
		title = QLabel(f"Uninstalling Blender v{self.version}", objectName="input-title")
		self.addWidget2(title)
		
		self.processText = QLabel("", objectName="input-label")
		self.addWidget2(self.processText)
	
		self.setDefaultButtons(nextLabel="Uninstalling...")
		self.primaryBtn.setDisabled(True)
		self.secondBtn.hide()

	def initAction(self):
		try:
			# Remove blender directory from /opt/blender
			blenderPath = versions.paths[self.version]
			if path.isdir(blenderPath):
				run(["sudo", "rm", "-rf", blenderPath], check=True)
			
			self.processText.setText(f"Blender v{self.version} successfully uninstalled!")
			self.primaryBtn.setLabel("Accept")
			self.primaryBtn.setDisabled(False)
			
		except Exception as e:
			self.processText.setText(f"An error ocurred uninstalling Blender v{self.version}")
			self.primaryBtn.setLabel("Close")
			self.primaryBtn.setDisabled(False)
			print(e)

	def primaryAction(self):
		self.accept()
	