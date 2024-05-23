from sys import platform
from subprocess import run, CalledProcessError
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from components.custom.widget import Widget
from components.header_page import HeaderPage
from components.installs.header import VersionButtonsHeader
from components.scroll_list import ScrollList
from components.installs.version import VersionItem

from utils.read import loadStyle
from utils.scrapping import getAvailableVersions

from globals import BLENDER_ALL_VERSIONS_URL

'''
TO-DO list:
 - Scrap the web to see all available versions.
 - Check if the selected version is already installed.
 - Add blender to PATH?
'''

class ConfigPage(QWidget):
	def __init__(self, title, name="installs-page"):
		super().__init__()

		# loadStyle("src/qss/pages/installs/style.qss", self)

		page_layout = QVBoxLayout()
		page_layout.setContentsMargins(0, 0, 0, 0)
		page_layout.setSpacing(0)

		# Header Page
		header_page = HeaderPage(title)
		# header_page.addWidget(VersionButtonsHeader())
		header_page.parent(page_layout)
		# page_layout.addWidget(header_page)

		#Scroll List
		self.content = ScrollList()
		self.content.parent(page_layout)
		
		self.setLayout(page_layout)
