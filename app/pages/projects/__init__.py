from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QDialog

from app.components.custom.frame import Frame
from app.components.file_dialog import FileDialog

from app.components.pages.header import HeaderPage
from app.components.pages.projects.header.buttons import OptionsButtonsHeader
from app.components.pages.projects.list import ProjectsList

from app.pages.dialogs.new_project import NewProject

class ProjectsPage(Frame):
	def __init__(self, title, name="projects-page"):
		super().__init__(name, QVBoxLayout)

		self.initUI(title)

	def initUI(self, title):
		self.loadStyle(__file__)

		header_buttons = OptionsButtonsHeader()
		header_buttons.onCreateProject.connect(self.createProject)
		header_buttons.onImportProject.connect(self.importProjects)
		
		header = HeaderPage(title)
		header.addWidget(header_buttons)
		self.addWidget(header)
		
		self.projects = ProjectsList()
		self.projects.populate()
		self.addWidget(self.projects)
	
	def createProject(self):
		new_project_dialog = NewProject(self)
		if new_project_dialog.open() == QDialog.Accepted:
			file_name, version = new_project_dialog.getProjectData()
			self.projects.createProject(file_name, version)

	def importProjects(self):
		# Getting the full path of the projects
		file_names = FileDialog.findBlendFile(self)
		self.projects.importProjects(file_names)
