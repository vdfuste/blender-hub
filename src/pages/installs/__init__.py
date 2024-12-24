from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from components.custom.frame import Frame
from components.custom.scroll import ScrollArea

from components.pages.page import Page
from components.pages.installs.header import VersionButtonsHeader
from components.pages.installs.version import VersionItem

from globals import downloads

class InstallsPage(Page):
	def __init__(self, title, name="installs-page"):
		super().__init__(title, name)
		
		self.up_to_date = False
		self.selected_serie = 0
		
		self.initUI(title)
		self.loadData()
		
	def initUI(self, title):
		self.loadStyle(__file__)
		
		# Header Buttons
		header_buttons = VersionButtonsHeader(downloads.series)
		header_buttons.versionSelected.connect(lambda index: self.setSerie(index))
		self.setHeaderButtons(header_buttons)
		
		# Scroll List
		self.versions_list = ScrollArea()
		self.versions_list.hideHorizontalScroll()
		self.versions_list.hideVerticalScroll()
		self.versions_list.setSpacing(24)
		self.addWidget(self.versions_list)
	
	def loadData(self):
		message = QLabel("Loading all versions...")
		message.setObjectName("loading-label")
		message.setAlignment(Qt.AlignCenter)
		self.versions_list.addItem(message)

		# Fetch new data here
		
		self.up_to_date = True
		self.setSerie(self.selected_serie)
	
	def setSerie(self, serie):
		if not self.up_to_date: pass

		self.selected_serie = serie
		self.versions_list.clear()

		for data in downloads.versions[serie]["cards"]:
			card = VersionItem(self.width(), data)
			self.versions_list.addItem(card)

		self.versions_list.update()
	
	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.setSerie(self.selected_serie)
