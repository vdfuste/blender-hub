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
		
		# TO-DO: Fix this!
		#for index, version in enumerate(series):
		#	button = QPushButton(f"Version {version}")
		#	button.setObjectName("version-btn")
		#	button.clicked.connect(lambda: selectVersion(index))

		#	layout.addWidget(button)

		# DELETE THIS LATER
		button4X = QPushButton(f"Serie 4.X")
		button4X.setObjectName("version-btn")
		button4X.clicked.connect(lambda: selectVersion(0))
		layout.addWidget(button4X)

		button3X = QPushButton(f"Serie 3.X")
		button3X.setObjectName("version-btn")
		button3X.clicked.connect(lambda: selectVersion(1))
		layout.addWidget(button3X)

		#button2X = QPushButton(f"Serie 4.X")
		#button2X.setObjectName("version-btn")
		#button2X.clicked.connect(lambda: selectVersion(0))
		#layout.addWidget(button2X)
		# DELETE THIS LATER

		self.setLayout(layout)
