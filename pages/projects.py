from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy, QFileDialog

from globals import projects
from components.fileDialog import FileDialog

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


		# Header
		header = QWidget()
		header.setObjectName("header")
		header_layout = QHBoxLayout()
		header_layout.setContentsMargins(24, 96, 12, 12)
		
		title = QLabel("Projects")
		title.setObjectName("title")
		header_layout.addWidget(title)
		
		header_layout.addStretch(0)

		import_btn = QPushButton("Import existing project")
		import_btn.clicked.connect(lambda: self.importProject())
		header_layout.addWidget(import_btn)

		# new_btn = QPushButton("Create new project")
		new_btn = QPushButton("See projects")
		new_btn.setObjectName("new_btn")
		new_btn.clicked.connect(lambda: self.createProject())
		header_layout.addWidget(new_btn)

		header.setLayout(header_layout)
		page_layout.addWidget(header)


		# Projects list
		# List Header
		header = Header()
		page_layout.addWidget(header)

		# Items
		scroll_area = QScrollArea()
		scroll_area.setWidgetResizable(True)
		scroll_area.setContentsMargins(0, 0, 0, 0)
		scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.projects_list = QWidget()
		self.projects_list.setObjectName("list")
		self.projects_list_layout = QVBoxLayout()
		self.projects_list_layout.setAlignment(Qt.AlignTop)
		self.projects_list_layout.setContentsMargins(0, 0, 0, 0)
		self.projects_list_layout.setSpacing(0)

		self.populateList()

		self.projects_list.setLayout(self.projects_list_layout)
		scroll_area.setWidget(self.projects_list)
		page_layout.addWidget(scroll_area)
		
		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
	
	def populateList(self):
		# Populate list with all the items in "projects"
		for index, project in enumerate(projects.items):
			item = Item(project, index, lambda _index, delete: self.removeProject(_index, delete))
			self.projects_list_layout.addWidget(item)
		
		self.projects_list.update()
	
	def createProject(self):
		print(projects.items)

	def importProject(self):
		# Get the full path of the projects
		file_names = FileDialog.findBlendFile(self)

		for file_name in file_names:
			if file_name:
				is_on_list = False 
				
				# Check if the project is already on the list
				for project in projects.items:
					data = project.split(';')
					if data[0] == file_name:
						print("The project already exists.")
						is_on_list = True
						break

				# Skip the current loop if the prject is on the list
				if is_on_list: continue
				
				# Add project if is not on the list
				data, index = projects.addProject(file_name)

				item = Item(data, index, lambda _index, delete: self.removeProject(_index, delete))
				self.projects_list_layout.addWidget(item)

				print(f"Project imported: {file_name}")

	def removeProject(self, index, delete=False):
		print(index)
		
		# Remove data from "projects.txt" file
		projects.removeProject(index, delete)

		# Remove all items
		while self.projects_list_layout.count():
			item = self.projects_list_layout.takeAt(0)
			if item.widget():
				item.widget().deleteLater()

		# Add new items
		self.populateList()
