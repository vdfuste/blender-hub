from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from utils.data import ProjectsList

from components.projects_item import ProjectsItem

class ProjectsPage(QWidget):
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		page = QWidget()
		page.setObjectName("projects_page")
		page_layout = QVBoxLayout()
		page_layout.setContentsMargins(0, 0, 0, 0)
		page_layout.setSpacing(0)

		# Loading projects
		projects = ProjectsList()
		#print(projects.items)
		
		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
		