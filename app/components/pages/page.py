from PyQt5.QtWidgets import QVBoxLayout

from app.components.custom.frame import Frame
from app.components.pages.header import HeaderPage

class Page(Frame):
	def __init__(self, title, name="page", layout=QVBoxLayout):
		super().__init__(name, layout)
		
		self.header_page = HeaderPage(title)
		self.addWidget(self.header_page)

	def setHeaderButtons(self, buttons):
		self.header_page.addWidget(buttons)
