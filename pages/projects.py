from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel

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

		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		page_layout.addWidget(ProjectsItem())
		
		# Projects listprojects_list = QTableWidget()
		# projects_list.setObjectName("projects")
		# projects_list.setContentsMargins(0, 0, 0, 0)
		# projects_list.setColumnCount(3)
		# projects_list.setRowCount(10)
		# projects_list.verticalHeader().setVisible(False)
		# projects_list.horizontalHeader().setSectionResizeMode(0, 1)
		# projects_list.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
		
		# for row, (col1, col2, col3) in enumerate(projects):
		# 	projects_list.setItem(row, 0, QTableWidgetItem("{}\n{}".format(col1, col2)))
		# 	projects_list.setItem(row, 1, QTableWidgetItem(col3))
		# 	#projects_list.setItem(row, 2, QTableWidgetItem(col3))
		# projects_list = QTableWidget()
		# projects_list.setObjectName("projects")
		# projects_list.setContentsMargins(0, 0, 0, 0)
		# projects_list.setColumnCount(3)
		# projects_list.setRowCount(10)
		# projects_list.verticalHeader().setVisible(False)
		# projects_list.horizontalHeader().setSectionResizeMode(0, 1)
		# projects_list.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
		
		# for row, (col1, col2, col3) in enumerate(projects):
		# 	projects_list.setItem(row, 0, QTableWidgetItem("{}\n{}".format(col1, col2)))
		# 	projects_list.setItem(row, 1, QTableWidgetItem(col3))
		# 	#projects_list.setItem(row, 2, QTableWidgetItem(col3))

		# page_layout.addWidget(projects_list)
		
		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
		