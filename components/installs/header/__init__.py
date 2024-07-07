from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

# from components.custom.widget import Widget
from utils.read import loadStyle

class VersionButtonsHeader(QWidget):
	def __init__(self, series, selectVersion):
		super().__init__()

		loadStyle("components/installs/header/style.qss", self)
		
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 16, 0)
		layout.setSpacing(0)
		layout.setAlignment(Qt.AlignBottom)
		
		for index, version in enumerate(series):		
			button = QPushButton(f"Version {version} {index}")
			button.setObjectName("version-btn")
			button.clicked.connect(lambda _, index = index: selectVersion(index))
			layout.addWidget(button)

		self.setLayout(layout)
