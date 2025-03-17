from PyQt5.QtWidgets import QVBoxLayout

from components.custom.dialog import Dialog
from pages.dialogs.uninstall.sections.password import PasswordSection
from pages.dialogs.uninstall.sections.remove import RemoveSection

class UninstallDialog(Dialog):
	def __init__(self, version, *, parent=None):
		super().__init__(parent, name="uninstall-dialog")

		self.initWindow(title=f"Uninstall Blender v{version}", width=640, height=20)

		self.addSection(PasswordSection())
		self.addSection(RemoveSection(version))
