from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QIcon

class SideBarButton(QPushButton):
	def __init__(self, label, name, icon):
		super().__init__(label)
		self.setObjectName(name)
		#self.setLayoutDirection(Qt.RightToLeft)
		self.setIcon(QIcon("src/images/{0}".format(icon)))
		self.setIconSize(QSize(20, 20))
		self.setContentsMargins(0, 0, 0, 0)

	def addToLayout(self, parent_layout):
		parent_layout.addWidget(self)

	def onClick(self, callback):
		self.clicked.connect(callback)


class Sidebar(QWidget):
	def __init__(self, changePage):
		super().__init__()

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

		icon = QLabel("")
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

		button1 = SideBarButton("Projects", "projects_btn", "folder.svg")
		button1.onClick(lambda: changePage("Projects"))
		button1.addToLayout(buttons_layout)
		
		button2 = SideBarButton("Config File", "config_btn", "settings.svg")
		button2.onClick(lambda: changePage("Config"))
		button2.addToLayout(buttons_layout)

		buttons.setLayout(buttons_layout)
		sidebar_layout.addWidget(buttons)

		# Vertical space
		sidebar_layout.addStretch(1)

		sidebar.setLayout(sidebar_layout)
		layout.addWidget(sidebar)
		
		self.setLayout(layout)
