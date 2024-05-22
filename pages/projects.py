from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy, QFileDialog

from pages.floating.new_project import NewProject

from components.file_dialog import FileDialog
from components.scroll_list import ScrollList
from components.header_page import HeaderPage
from components.projects.header import Header
from components.projects.item import Item

from globals import projects

class ProjectsPage(QWidget):
	def __init__(self, title, name="projects_page"):
		super().__init__()

		self.floating_window = NewProject()

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		page = QWidget()
		page.setObjectName(name)
		page_layout = QVBoxLayout()
		page_layout.setContentsMargins(0, 0, 0, 0)
		page_layout.setSpacing(0)


		# Header Page
		header_page = HeaderPage(title)
		header_page.parent(page_layout)
		
		import_btn = QPushButton("Import existing project")
		import_btn.setObjectName("border-btn")
		import_btn.clicked.connect(lambda: self.importProject())
		header_page.addWidget(import_btn)

		new_btn = QPushButton("Create new project")
		new_btn.setObjectName("primary-border-btn")
		new_btn.clicked.connect(lambda: self.createProject())
		header_page.addWidget(new_btn)

		# Projects List
		header_list = Header()
		page_layout.addWidget(header_list)

		self.list = ScrollList("list")
		self.list.parent(page_layout)
		self.list.populate(
			projects.items,
			lambda data, index : self.newItem(data, index)
		)

		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
	
	def newItem(self, data, index):
		return Item(data, index, lambda _index, delete: self.removeProject(_index, delete))
	
	def createProject(self):
		self.floating_window.reset()
		self.floating_window.show()

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
				# self.projects_list_layout.addWidget(item)
				self.list.addItem(item)

				print(f"Project imported: {file_name}")

	def removeProject(self, index, delete=False):
		# print(index)
		
		# Remove data from "projects.txt" file
		projects.removeProject(index, delete)

		# Add new items
		self.list.populate(projects.items, lambda data, index : Item(data, index, lambda _index, delete: self.removeProject(_index, delete)))

