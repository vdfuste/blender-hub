from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from utils.data import loadProjects

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

		# Items list
		projects = [
			("mera_mera_no_mi", "~/Documents/Projects/3D/", "4.1.0"),
			("Nuriasaurio", "~/Documents/BlenderHub/", "4.0.2"),
			("Suzanne", "~/Desktop/MonkeyHead/", "3.6.1"),
		]

		loadProjects()
		
		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
		