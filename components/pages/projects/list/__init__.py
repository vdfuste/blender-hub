from time import ctime

from PyQt5.QtWidgets import QVBoxLayout

from components.custom.frame import Frame
from components.custom.scroll import ScrollArea

from components.pages.projects.list.header import HeaderList
from components.pages.projects.list.item import Item

from utils.blender.run import new_project
from utils.projects import ProjectsData

from globals import versions, PROJECTS_FILE_PATH

class ProjectsList(Frame):
	def __init__(self, name="projects-list"):
		super().__init__(name, QVBoxLayout)

		self.projects_data = ProjectsData(PROJECTS_FILE_PATH)
		self.initUI()

		print(self.projects_data.items)

	def initUI(self):
		header = HeaderList()
		self.addWidget(header)

		self.list = ScrollArea()
		self.addWidget(self.list)

	def addItem(self, data, index):
		item = Item(data, index)
		item.projectOpened.connect(lambda file, ind, ver: self.openProject(file, ind, ver))
		item.projectRemoved.connect(lambda file, delete: self.removeProject(index, file))
		
		self.list.addItem(item)
	
	def populate(self):
		self.list.clear()
		for index, data in enumerate(self.projects_data.items):
			self.addItem(data, index)

	def createProject(self, file_name, version):
		new_project(file_name, versions.paths[version])
		data, index = self.projects_data.addProject(file_name, ctime(), version)
		self.addItem(data, index)

	def importProjects(self, file_names):
		# Getting any Blender version to check the project version
		check_path = versions.paths[versions.installed[0]]

		for file_name in file_names:
			if file_name:
				# Check if the project is already on the list                                      
				is_on_list = False 

				for project in self.projects_data.items:
					if project["file_name"] == file_name:
						print("The project already exists.")
						is_on_list = True
						break

				if is_on_list: continue
				
				data, index = self.projects_data.addProject(file_name, check_path=check_path)
				self.addItem(data, index)

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
