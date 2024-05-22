from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget

from pages.config import ConfigPage
from pages.projects import ProjectsPage
from pages.installs import InstallsPage

class Pages(QWidget):
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		self.pagesIndex = {}
		
		pages = QWidget()
		pages.setObjectName("pages")
		pages_layout = QVBoxLayout()
		pages_layout.setContentsMargins(0, 0, 0, 0)
		pages_layout.setAlignment(Qt.AlignTop)
		
		# Pages stack
		self.stack = QStackedWidget()
		self.stack.setObjectName("stack")
		
		self.addPage("Projects", "My Projects", ProjectsPage("My Projects"))
		self.addPage("Config", "Configuration File", ConfigPage("Configuration File"))
		self.addPage("Installs", "Installs", InstallsPage("Installs"))
		
		pages_layout.addWidget(self.stack)

		pages.setLayout(pages_layout)
		layout.addWidget(pages)

		self.changePage("Projects")
		# self.changePage("Installs")
		
		self.setLayout(layout)
	
	def addPage(self, name_id, title, page):
		self.pagesIndex[name_id] = {
			"index": len(self.pagesIndex),
			"title": title
		}
		self.stack.addWidget(page)
	
	def changePage(self, name_id):
		self.stack.setCurrentIndex(self.pagesIndex[name_id]["index"])
		#self.title.setText(self.pagesIndex[name_id]["title"])
		