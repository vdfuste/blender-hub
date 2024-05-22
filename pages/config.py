from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget

from components.header_page import HeaderPage

class ConfigPage(QWidget):
	def __init__(self, title):
		super().__init__()

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		page = QWidget()
		page.setContentsMargins(0, 0, 0, 0)
		page.setObjectName("config_page")
		page_layout = QVBoxLayout()

		# Header Page
		header_page = HeaderPage(title)
		header_page.parent(page_layout)

		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
