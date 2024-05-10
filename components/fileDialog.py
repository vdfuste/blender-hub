from PyQt5.QtWidgets import QFileDialog

class FileDialog():
	def findBlendFile(self):
		title = "Open Blender File"
		format_options = "Blender Files (*.blend);;All Files (*)"

		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		file_name, _ = QFileDialog.getOpenFileNames(self, title, "", format_options, options=options)

		return file_name