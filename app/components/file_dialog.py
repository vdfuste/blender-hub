from PyQt5.QtWidgets import QFileDialog

from app.globals import DOCUMENTS_FOLDER

class FileDialog():
	def findBlendFile(self):
		title = "Open Blender File"
		format_options = "Blender Files (*.blend);;All Files (*)"

		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_name, _ = QFileDialog.getOpenFileNames(self, title, DOCUMENTS_FOLDER, format_options, options=options)

		return file_name

	def newBlenderFile(self):
		title = "New Blender File"

		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_path = QFileDialog.getExistingDirectory(self, title, DOCUMENTS_FOLDER, options=options)

		return file_path