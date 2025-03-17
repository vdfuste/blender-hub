from PyQt5.QtWidgets import QVBoxLayout

from components.custom.dialog import Dialog
from pages.dialogs.install.sections.download import DownloadSection
from pages.dialogs.install.sections.password import PasswordSection

class InstallDialog(Dialog):
	def __init__(self, version, url, *, parent=None):
		super().__init__(parent, name="install-dialog")

		self.initWindow(title=f"Install Blender v{version}", width=640, height=20)

		self.addSection(PasswordSection())
		self.addSection(DownloadSection(version, url))
