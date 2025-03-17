from subprocess import run
from PyQt5.QtWidgets import QLabel

from components.custom.dialog import Section, TextInput

class PasswordSection(Section):
	def __init__(self):
		super().__init__()
		
		title = QLabel("Enter the password to install", objectName="input-title")
		self.addWidget2(title)
		
		self.password = TextInput("Password", isPassword=True)
		self.password.returnPressed.connect(self.primaryAction)
		self.password.textChanged.connect(self.onTextChanged)
		self.addWidget2(self.password)

		self.setDefaultButtons(prevLabel="Cancel", nextLabel="Download and install")
		self.primaryBtn.setDisabled(True)

	def onTextChanged(self):
		self.primaryBtn.setDisabled(self.password.isEmpty())

	def primaryAction(self):
		try:
			passw = self.password.getText()

			run(["sudo", "-k"])
			run(["sudo", "-S", "mkdir", "-pm", "777", "/tmp/blenderhub"], input=passw.encode(), check=True)
			
			self.next()
		
		except Exception:
			self.password.setText("")
	