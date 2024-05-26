from time import ctime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog

from pages.dialogs.new_project import NewProject

from components.file_dialog import FileDialog
from components.header_page import HeaderPage
from components.projects.buttons import OptionsButtonsHeader
from components.projects.header import Header
from components.scroll_list import ScrollList
from components.projects.item import Item

from utils.blender.run import new_project

from globals import projects, versions

class ProjectsPage(QWidget):
	def __init__(self, title, parent=None, name="projects_page"):
		super().__init__()

		# Init UI
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		page = QWidget()
		page.setObjectName(name)
		page_layout = QVBoxLayout()
		page_layout.setContentsMargins(0, 0, 0, 0)
		page_layout.setSpacing(0)


		# Header Page
		header_page = HeaderPage(title)
		header_page.addWidget(OptionsButtonsHeader(self.createProject, self.importProject))
		header_page.parent(page_layout)
		# page_layout.addWidget(header_page)
		

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
		new_project_dialog = NewProject(self)
		if new_project_dialog.open() == QDialog.Accepted:
			# Getting data from the dialog
			file_name, blender_version = new_project_dialog.getProjectData()
			
			# Creating a new project
			new_project(file_name, versions.paths[blender_version])

			# Adding the project to "Projects List"
			data, index = projects.addProject(file_name, ctime(), blender_version)
			item = Item(data, index, lambda _index, delete: self.removeProject(_index, delete))
			self.list.addItem(item)

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

				# Skip the current loop if the project is on the list
				if is_on_list: continue
				
				# Add project if is not on the list
				data, index = projects.addProject(file_name)

				item = Item(data, index, lambda _index, delete: self.removeProject(_index, delete))
				self.list.addItem(item)

				print(f"Project imported: {file_name}")

	def removeProject(self, index, delete=False):
		# print(index)
		
		# Remove data from "projects.txt" file
		projects.removeProject(index, delete)

		# Add new items
		self.list.populate(projects.items, lambda data, index : Item(data, index, lambda _index, delete: self.removeProject(_index, delete)))

