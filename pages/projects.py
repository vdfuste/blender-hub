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

from utils.projects import ProjectsList
from utils.blender.run import new_project

from globals import versions, PROJECTS_FILE_PATH

class ProjectsPage(QWidget):
	def __init__(self, title, name="projects_page"):
		super().__init__()

		self.projects_data = ProjectsList(PROJECTS_FILE_PATH)

		self.initUI(title, name)

	def initUI(self, title, name):
		self.loadStyle("components/projects")

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
		
		# Projects List
		header_list = Header()
		page_layout.addWidget(header_list)

		self.list = ScrollList("list")
		self.list.parent(page_layout)
		self.populate()

		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)

	def loadStyle(self, path):
		with open(f"{path}/style.qss") as style:
			self.setStyleSheet(style.read())
	
	def newItem(self, data, index):
		item = Item(data, index)
		item.projectOpened.connect(lambda file, ind, ver: self.openProject(file, ind, ver))
		item.projectRemoved.connect(lambda file, delete: self.removeProject(index, file))
		
		return item
	
	def populate(self):
		self.list.populate(
			self.projects_data.items,
			lambda data, index : self.newItem(data, index)
		)
	
	def createProject(self):
		new_project_dialog = NewProject(self)
		if new_project_dialog.open() == QDialog.Accepted:
			# Getting data from the dialog
			file_name, blender_version = new_project_dialog.getProjectData()
			
			# Creating a new project
			new_project(file_name, versions.paths[blender_version])

			# Adding the project to "Projects List"
			data, index = self.projects_data.addProject(file_name, ctime(), blender_version)
			self.list.addItem(self.newItem(data, index))

	def importProject(self):
		# Getting the full path of the projects
		file_names = FileDialog.findBlendFile(self)

		# Getting any Blender version to check the project version
		check_path = versions.paths[versions.installed[0]]

		for file_name in file_names:
			if file_name:
				is_on_list = False 
				
				# Check if the project is already on the list                                      
				for project in self.projects_data.items:
					if project["file_name"] == file_name:
						print("The project already exists.")
						is_on_list = True
						break

				# Skip the current loop if the project is on the list
				if is_on_list: continue
				
				# Add project if is not on the list
				data, index = self.projects_data.addProject(file_name, check_path=check_path)

				self.list.addItem(self.newItem(data, index))

				print(f"Project imported: {file_name}")

	def openProject(self, file_name, index, selected_version):
		# When a project is opened it's also moved to first place.
		# To achive this behaviour instead of move the clicked item
		# it will be removed and inserted at the beginning of the list
		# and then the widget list is populated with the new items
		# causing a re-rendering.
		self.projects_data.removeProject(index)
		self.projects_data.addProject(file_name, ctime(), selected_version, index=0)
		self.populate()
	
	def removeProject(self, index, delete=False):
		# Remove data from "projects.txt" file
		self.projects_data.removeProject(index, delete)

		# Add new items
		self.populate()

