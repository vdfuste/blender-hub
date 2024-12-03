from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from app.components.custom.frame import Frame
from app.components.custom.scroll import ScrollArea

from app.components.pages.page import Page
from app.components.pages.installs.header import VersionButtonsHeader
from app.components.pages.installs.version import VersionItem

from app.globals import downloads

class InstallsPage(Page):
	def __init__(self, title, name="installs-page"):
		super().__init__(title, name)
		
		self.called = False
		self.selected_serie = 0
		
		self.initUI(title)
		
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
	
	def setSerie(self, serie):
		pass
	
	def callOnce(self):
		if self.called: pass
		
		print("MEH: Meeeheuhbeujbfbefgeuieu")
	
	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.setSerie(self.selected_serie)

'''class InstallsPage(Frame):
	def __init__(self, title, name="installs-page"):
		super().__init__(name, QVBoxLayout)
		
		self.selected_serie = 0
		self.initUI(title)
		self.loadData()
		
	def initUI(self, title):
		self.loadStyle(__file__)
		
		# Header Page
		buttons_header = VersionButtonsHeader(downloads.series)
		buttons_header.versionSelected.connect(lambda index: self.setSerie(index))

		header_page = HeaderPage(title)
		header_page.addWidget(buttons_header)
		self.addWidget(header_page)
		
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
	
	def setSerie(self, serie):
		pass
		'' 'self.selected_serie = serie
		self.versions_list.clear()

		for data in downloads.versions[serie]["cards"]:
			card = VersionItem(self.width(), data)
			self.versions_list.addItem(card)

		self.versions_list.update()'' '
	
	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.setSerie(self.selected_serie)'''
