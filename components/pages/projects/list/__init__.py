from PyQt5.QtWidgets import QVBoxLayout

from components.custom.frame import Frame
from components.custom.scroll import ScrollArea

from components.pages.projects.list.header import HeaderList
from components.pages.projects.list.item import Item

class ProjectsList(Frame):
	def __init__(self, name="projects-list"):
		super().__init__(name, QVBoxLayout)
		
		header = HeaderList()
		self.addWidget(header)

		self.list = ScrollArea()
		self.addWidget(self.list)

	def newItem(self, data, index):
		item = Item(data, index)
		item.projectOpened.connect(lambda file, ind, ver: self.openProject(file, ind, ver))
		item.projectRemoved.connect(lambda file, delete: self.removeProject(index, file))
		
		return item
	
	def populate(self):
		pass

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
