from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QComboBox

class Item(QWidget):
	'''
	TO-DO list:
	 * Versions
	  - Check what versions are installed
	  - Highlight the current version
	  - Mark the current version as uninstalled if is not installed
	'''
	def __init__(self, data):
		super(QWidget, self).__init__()

		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)

		item = QWidget()
		item.setObjectName("item")
		item_layout = QHBoxLayout()
		item_layout.setContentsMargins(24, 0, 48, 0)
		item_layout.setSpacing(0)

		
		# Left section content
		left_section = QWidget()
		left_section.setObjectName("item_left")
		left_section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		left_section_layout = QVBoxLayout()
		left_section_layout.setContentsMargins(0, 0, 0, 0)
		left_section_layout.setSpacing(0)

		# Title and path
		file_name = QLabel(data["name"])
		file_name.setObjectName("file_name")
		left_section_layout.addWidget(file_name)

		file_path = QLabel(data["path"])
		file_path.setObjectName("file_path")
		left_section_layout.addWidget(file_path)

		left_section.setLayout(left_section_layout)
		item_layout.addWidget(left_section)


		# Center section content
		center_section = QWidget()
		center_section.setObjectName("item_center")
		center_section_layout = QVBoxLayout()
		center_section_layout.setContentsMargins(0, 0, 0, 0)

		# Last modification date
		file_last = QLabel("a week ago")
		center_section_layout.addWidget(file_last)

		center_section.setLayout(center_section_layout)
		item_layout.addWidget(center_section)


		# Right section content
		right_section = QWidget()
		right_section.setObjectName("item_right")
		right_section_layout = QVBoxLayout()
		right_section_layout.setContentsMargins(0, 0, 0, 0)

		# Version and options
		versions = QComboBox()
		versions.setObjectName("versions")
		versions.addItems([data["version"], "v4.1.1", "v4.0.2"])
		right_section_layout.addWidget(versions)

		right_section.setLayout(right_section_layout)
		item_layout.addWidget(right_section)

		
		item.setLayout(item_layout)
		layout.addWidget(item)
		self.setLayout(layout)

	def onClick(self, callback):
		self.clicked.connect(callback)
