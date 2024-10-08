from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QStackedWidget

from pages.config import ConfigPage
from pages.projects import ProjectsPage
from pages.installs import InstallsPage

pages_data = [
	{
		"title": "My Projects",
		"icon": "folder.svg",
		"page": ProjectsPage
	},
	{
		"title": "Installs",
		"icon": "download.svg",
		"page": InstallsPage
	},
	{
		"title": "Config Files",
		"icon": "settings.svg",
		"page": ConfigPage
	}
]

class Pages(QFrame):
	def __init__(self):
		super().__init__()

		self.initUI()
		self.changePage("Projects")

	def initUI(self):
		self.setObjectName("pages")

		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignTop)
		layout.setContentsMargins(0, 0, 0, 0)
		
		# Pages stack
		self.stack = QStackedWidget()
		self.stack.setObjectName("stack")
		
		for data in pages_data:
			self.stack.addWidget(data["page"](data["title"]))
		
		layout.addWidget(self.stack)
		self.setLayout(layout)
	
	def changePage(self, title):
		for index, page in enumerate(pages_data):
			if title == page["title"]:
				self.stack.setCurrentIndex(index)
				break
		