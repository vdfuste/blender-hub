from PyQt5.QtWidgets import QVBoxLayout, QLabel

from app.components.custom.frame import Frame
from app.components.custom.scroll import ScrollArea

from app.components.pages.header import HeaderPage
from app.components.pages.installs.header import VersionButtonsHeader
from app.components.pages.installs.version import VersionItem

from app.globals import downloads

class InstallsPage(Frame):
	def __init__(self, title, name="installs-page"):
		super().__init__(name, QVBoxLayout)
		
		self.selected_serie = 0
		self.initUI(title)
		
	def initUI(self, title):
		self.loadStyle(__file__)
		
		# Header Page
		buttons_header = VersionButtonsHeader(downloads.series)
		buttons_header.versionSelected.connect(lambda index: self.setSerie(index))

		header_page = HeaderPage(title)
		header_page.addWidget(buttons_header)
		self.addWidget(header_page)

		#Scroll List
		self.versions_list = ScrollArea()
		self.versions_list.hideHorizontalScroll()
		self.versions_list.hideVerticalScroll()
		self.versions_list.setSpacing(24)
		self.addWidget(self.versions_list)

	def setSerie(self, serie):
		self.selected_serie = serie
		self.versions_list.clear()

		for data in downloads.versions[serie]["cards"]:
			card = VersionItem(self.width(), data)
			self.versions_list.addItem(card)

		self.versions_list.update()
	
	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.setSerie(self.selected_serie)
