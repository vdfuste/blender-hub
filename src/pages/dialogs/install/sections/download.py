import urllib.request
from os import path
from subprocess import run
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QLabel

from components.custom.dialog import Section, TextInput
from components.custom.frame import Frame

class InstallThread(QThread):
	stateChanged = pyqtSignal(str)
	downloadPercentageChanged = pyqtSignal(int)

	def __init__(self, url):
		super().__init__()
		self._stop = False
		self.url = url
		
	def run(self):
		try:
			# DOWNLOADING
			self.stateChanged.emit("Downloading")

			# Download Blender file
			tempDir = "/tmp/blenderhub"
			blenderOpt = "/opt/blender"

			extension = ".tar.xz"
			blenderFile = path.split(self.url)[-1]
			blenderDir = blenderFile.replace(extension, "")
			
			tempBlenderDir = path.join(tempDir, blenderDir)
			tempBlenderFile = path.join(tempDir, blenderFile)
			
			def report(count, blockSize, total):
				if self._stop:
					raise Exception("Download manually stopped")
				
				percent = int(count * blockSize * 100 / total)
				self.downloadPercentageChanged.emit(percent)
			
			opener = urllib.request.build_opener()
			opener.addheaders = [("User-agent", "Mozilla/5.0")]
			urllib.request.install_opener(opener)
			urllib.request.urlretrieve(self.url, tempBlenderFile, reporthook=report)
			
			# INSTALLING
			self.stateChanged.emit("Installing")

			# Create Blender directory if not exists
			if not path.isdir(blenderOpt):
				run(["sudo", "mkdir", blenderOpt], check=True)
			
			# Extract file content and move it to Blender directory
			run(["tar", "-xf", tempBlenderFile, "-C", tempDir], check=True)
			run(["sudo", "mv", tempBlenderDir, blenderOpt], check=True)
			
			# FINISHED
			self.stateChanged.emit("Finished")
			run(["sudo", "rm", "-r", tempDir])
			
		except Exception as e:
			self.stateChanged.emit("Stopped" if self._stop else "Error")
			run(["sudo", "rm", "-r", tempDir])
			print(e)

	def stop(self):
		self._stop = True

class DownloadSection(Section):
	def __init__(self, version, url):
		super().__init__()

		self.version = version

		self.install = InstallThread(url)
		self.install.stateChanged.connect(self.stateChanged)
		self.install.downloadPercentageChanged.connect(self.percentageChanged)
		
		title = QLabel(f"Installing Blender v{self.version}", objectName="input-title")
		self.addWidget2(title)
		
		self.processText = QLabel("", objectName="input-label")
		self.addWidget2(self.processText)
	
		self.setDefaultButtons(prevLabel="Cancel download", nextLabel="Installing...")
		self.primaryBtn.setDisabled(True)
		#self.primaryBtn.hide()

	def initAction(self):
		self.install.start()

	def primaryAction(self):
		self.accept()
	
	def secondAction(self):
		self.install.stop()
		self.cancel()

	def stateChanged(self, state):
		if state == "Installing":
			self.processText.setText("Installing...")
		elif state == "Finished":
			self.processText.setText(f"Blender v{self.version} successfully installed!")
			self.primaryBtn.setLabel("Accept")
			self.primaryBtn.setDisabled(False)
			self.secondBtn.hide()
		elif state == "Error":
			self.processText.setText(f"An error ocurred installing Blender v{self.version}")
			self.primaryBtn.setLabel("Close")
			self.primaryBtn.setDisabled(False)
			self.secondBtn.hide()

	def percentageChanged(self, percent):
		self.processText.setText(f"Downloading...{percent}%")
	