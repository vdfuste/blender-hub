from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget

class Sidebar(QWidget):
	def __init__(self, changePage):
		super(Sidebar, self).__init__()

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		sidebar = QWidget()
		sidebar.setObjectName("sidebar")
		sidebar_layout = QVBoxLayout()
		sidebar_layout.setContentsMargins(0, 0, 0, 0)
		sidebar_layout.setSpacing(0)

		# Header
		header = QWidget()
		header.setObjectName("header")
		header_layout = QHBoxLayout()
		header_layout.setContentsMargins(0, 0, 0, 0)

		icon = QLabel("BH")
		icon.setContentsMargins(0, 0, 0, 0)
		icon.setAlignment(Qt.AlignRight)
		title = QLabel("Blender Hub")
		title.setContentsMargins(0, 0, 0, 0)
		header_layout.addWidget(icon)
		header_layout.addWidget(title)
		
		header.setLayout(header_layout)
		sidebar_layout.addWidget(header)
		
		# Vertical space
		sidebar_layout.addStretch(1)
		
		# Buttons
		buttons = QWidget()
		buttons.setObjectName("buttons")
		buttons_layout = QVBoxLayout()
		buttons_layout.setContentsMargins(0, 0, 0, 0)
		buttons_layout.setSpacing(0)

		button1 = QPushButton("Projects")
		button1.setObjectName("button1")
		button1.clicked.connect(lambda: changePage("Projects"))
		button1.setContentsMargins(0, 0, 0, 0)
		buttons_layout.addWidget(button1)
		
		button2 = QPushButton("Config File")
		button2.setObjectName("button2")
		button2.clicked.connect(lambda: changePage("Config"))
		button2.setContentsMargins(0, 0, 0, 0)
		buttons_layout.addWidget(button2)

		buttons.setLayout(buttons_layout)
		sidebar_layout.addWidget(buttons)

		sidebar.setLayout(sidebar_layout)
		layout.addWidget(sidebar)
		
		self.setLayout(layout)
		
