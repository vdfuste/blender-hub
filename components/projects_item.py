from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

class ProjectsItem(QWidget):
	def __init__(self):
		super().__init__()

		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		item = QWidget()
		item.setObjectName("projects_item")
		item_layout = QHBoxLayout()
		item_layout.setContentsMargins(0, 0, 0, 0)
		
		# Title and path
		left_section = QWidget()
		left_section.setObjectName("projects_item_left")
		left_section_layout = QVBoxLayout()
		left_section_layout.setContentsMargins(0, 0, 0, 0)

		# Left section content
		file_name = QLabel("Nuriasaurio")
		left_section_layout.addWidget(file_name)

		file_path = QLabel("~/Documents/BlenderHub/")
		left_section_layout.addWidget(file_path)

		left_section.setLayout(left_section_layout)
		item_layout.addWidget(left_section)

		# Last modification date
		center_section = QWidget()
		center_section.setObjectName("projects_item_center")
		center_section_layout = QVBoxLayout()
		center_section_layout.setContentsMargins(0, 0, 0, 0)

		# Center section content
		file_last = QLabel("a week ago")
		center_section_layout.addWidget(file_last)

		center_section.setLayout(center_section_layout)
		item_layout.addWidget(center_section)

		# Version and options
		right_section = QWidget()
		right_section.setObjectName("projects_item_right")
		right_section_layout = QVBoxLayout()
		right_section_layout.setContentsMargins(0, 0, 0, 0)

		# Right section content
		file_version = QLabel("4.0.2")
		right_section_layout.addWidget(file_version)

		right_section.setLayout(right_section_layout)
		item_layout.addWidget(right_section)

		item.setLayout(item_layout)
		layout.addWidget(item)
		self.setLayout(layout)
