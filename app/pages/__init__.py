from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QStackedWidget

from app.components.custom.frame import Frame

from app.pages.config import ConfigPage
from app.pages.projects import ProjectsPage
from app.pages.installs import InstallsPage

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

class Pages(Frame):
	def __init__(self):
		super().__init__("pages", QVBoxLayout)

		self.initUI()
		self.changePage("Projects")

	def initUI(self):
		self.layout.setAlignment(Qt.AlignTop)
		
		self.stack = QStackedWidget()
		self.stack.setObjectName("stack")
		
		for data in pages_data:
			page = data["page"]
			title = data["title"]

			self.stack.addWidget(page(title))
		
		self.addWidget(self.stack)
	
	def changePage(self, title):
		for index, page in enumerate(pages_data):
			if title == page["title"]:
				self.stack.setCurrentIndex(index)
				break
		