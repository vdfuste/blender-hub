from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QSizePolicy
from utils.data import ProjectsList

from components.projects.header import Header
from components.projects.item import Item

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

		# Projects list
		# Header
		header = Header()
		page_layout.addWidget(header)

		# Items
		scroll_area = QScrollArea()
		scroll_area.setWidgetResizable(True)
		scroll_area.setContentsMargins(0, 0, 0, 0)
		scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		projects_list = QWidget()
		projects_list.setObjectName("list")
		projects_list_layout = QVBoxLayout()
		projects_list_layout.setAlignment(Qt.AlignTop)
		projects_list_layout.setContentsMargins(0, 0, 0, 0)
		projects_list_layout.setSpacing(0)
		#projects_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		# Populate list with data
		for row, project in enumerate(projects.items):
			print(project)
			projects_list_layout.addWidget(Item(project))

		projects_list.setLayout(projects_list_layout)
		scroll_area.setWidget(projects_list)
		page_layout.addWidget(scroll_area)
		
		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
		