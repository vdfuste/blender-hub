from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget

from pages.config import ConfigPage
from pages.projects import ProjectsPage

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

		# Header
		header = QWidget()
		header.setObjectName("header")
		header_layout = QHBoxLayout()
		header_layout.setContentsMargins(16, 256, 16, 16)

		self.title = QLabel("")
		header_layout.addWidget(self.title)
		
		header.setLayout(header_layout)
		pages_layout.addWidget(header)
		
		# Pages stack
		self.stack = QStackedWidget()
		self.stack.setObjectName("stack")
		
		self.addPage("Projects", "My Projects", ProjectsPage())
		self.addPage("Config", "Configuration File", ConfigPage())
		
		pages_layout.addWidget(self.stack)

		pages.setLayout(pages_layout)
		layout.addWidget(pages)

		self.changePage("Projects")
		
		self.setLayout(layout)
	
	def addPage(self, name, title, page):
		self.pagesIndex[name] = {
			"index": len(self.pagesIndex),
			"title": title
		}
		self.stack.addWidget(page)
	
	def changePage(self, name):
		self.stack.setCurrentIndex(self.pagesIndex[name]["index"])
		self.title.setText(self.pagesIndex[name]["title"])
		