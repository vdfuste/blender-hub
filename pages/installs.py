from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from components.custom.widget import Widget
from components.header_page import HeaderPage
from components.installs.header import VersionButtonsHeader
from components.scroll_list import ScrollList
from components.installs.version import VersionItem

from utils.read import loadStyle

from globals import downloads

'''
TO-DO list:
 - Scrap the web to see all available versions.
 - Check if the selected version is already installed.
 - Add blender to PATH?
'''

class InstallsPage(QWidget):
	def __init__(self, title, name="installs-page"):
		super().__init__()
		
		loadStyle("src/qss/pages/installs/style.qss", self)

		self.selected_serie = 0
		
		page_layout = QVBoxLayout()
		page_layout.setContentsMargins(0, 0, 0, 0)
		page_layout.setSpacing(0)
		
		# Header Page
		buttons_header = VersionButtonsHeader(downloads.series)
		buttons_header.versionSelected.connect(lambda index: self.setSerie(index))

		header_page = HeaderPage(title)
		header_page.addWidget(buttons_header)
		header_page.parent(page_layout)

		#Scroll List
		self.versions_list = ScrollList()
		self.versions_list.layout.setContentsMargins(12, 8, 24, 8)
		self.versions_list.layout.setSpacing(12)
		# self.setSerie(self.selected_serie)
		self.versions_list.parent(page_layout)
		
		self.setLayout(page_layout)

	def setSerie(self, serie):
		self.selected_serie = serie
		self.versions_list.populate(
			downloads.versions[serie]["cards"],
			lambda data, index: VersionItem(self.width(), data)
		)
	
	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.setSerie(self.selected_serie)
