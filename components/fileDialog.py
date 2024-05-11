from PyQt5.QtWidgets import QFileDialog

from globals import INIT_FILE_DIALOG_FOLDER

class FileDialog():
	def findBlendFile(self):
		title = "Open Blender File"
		format_options = "Blender Files (*.blend);;All Files (*)"

		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_name, _ = QFileDialog.getOpenFileNames(self, title, INIT_FILE_DIALOG_FOLDER, format_options, options=options)

		return file_name

	def newBlenderFile(self):
		title = "New Blender File"

		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_name, _ = QFileDialog.getExistingDirectory(self, title, INIT_FILE_DIALOG_FOLDER, format_options, options=options)

		return file_name