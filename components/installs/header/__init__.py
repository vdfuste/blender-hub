from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

# from components.custom.widget import Widget
from utils.read import loadStyle

class VersionButtonsHeader(QWidget):
	def __init__(self):
		super().__init__()

		versions = [4, 3, 2]
		
		loadStyle("components/installs/header/style.qss", self)
		
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 16, 0)
		layout.setSpacing(0)
		layout.setAlignment(Qt.AlignBottom)
		
		# layout.addStretch(0)

		for index, version in enumerate(versions):
			_button = QPushButton(f"Version {version}")
			_button.setObjectName("version-btn")
			layout.addWidget(_button)

		self.setLayout(layout)
