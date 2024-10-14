from time import ctime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QDialog

from components.custom.frame import Frame
from components.file_dialog import FileDialog

from components.pages.header import HeaderPage
from components.pages.projects.header.buttons import OptionsButtonsHeader
from components.pages.projects.list import ProjectsList

from pages.dialogs.new_project import NewProject
from utils.blender.run import new_project
from utils.projects import ProjectsData

from globals import versions, PROJECTS_FILE_PATH

class ProjectsPage(Frame):
	def __init__(self, title, name="projects-page"):
		super().__init__(name, QVBoxLayout)

		self.projects_data = ProjectsData(PROJECTS_FILE_PATH)
		self.initUI(title)
		self.projects.populate()

	def initUI(self, title):
		self.loadStyle(__file__)

		header_buttons = OptionsButtonsHeader()
		header_buttons.onCreateProject.connect(self.createProject)
		header_buttons.onImportProject.connect(self.importProject)
		
		header = HeaderPage(title)
		header.addWidget(header_buttons)
		self.addWidget(header)
		
		self.projects = ProjectsList()
		self.addWidget(self.projects)
	
	def createProject(self):
		new_project_dialog = NewProject(self)
		if new_project_dialog.open() == QDialog.Accepted:
			# Getting data from the dialog
			file_name, blender_version = new_project_dialog.getProjectData()
			
			# Creating a new project
			new_project(file_name, versions.paths[blender_version])

			# Adding the project to "Projects List"
			data, index = self.projects_data.addProject(file_name, ctime(), blender_version)
			self.projects.addItem(self.newItem(data, index))

		#self.projects.populate()

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

				self.projects.addItem(self.newItem(data, index))

				print(f"Project imported: {file_name}")

		#self.projects.populate()
