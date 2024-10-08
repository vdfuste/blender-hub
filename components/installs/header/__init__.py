from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

from components.custom.frame import Frame

class VersionButtonsHeader(Frame):
	versionSelected = pyqtSignal(int)
	
	def __init__(self, series):
		super().__init__()

		self.loadStyle(__file__)
		
		self.layout.setContentsMargins(0, 0, 16, 0)
		self.layout.setAlignment(Qt.AlignBottom)

		for index, version in enumerate(series):		
			button = QPushButton(f"Version {version} {index}")
			button.setObjectName("version-btn")
			button.clicked.connect(lambda _, index=index: self.versionSelected.emit(index))
			
			self.addWidget(button)
