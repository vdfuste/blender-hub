from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget

class ConfigPage(QWidget):
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		page = QWidget()
		page.setContentsMargins(0, 0, 0, 0)
		page.setObjectName("config_page")
		page_layout = QVBoxLayout()

		label = QLabel("Config!")
		page_layout.addWidget(label)

		page.setLayout(page_layout)
		layout.addWidget(page)
		
		self.setLayout(layout)
