from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QStackedWidget, QDialog
from PyQt5.QtGui import QFont, QFontDatabase

from app.components.custom.frame import Frame

from app.components.sidebar import Sidebar
from app.pages import Pages

from app.globals import SCREEN_GEOMETRY

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		width = 1024
		height = 720
		pos_x = int(SCREEN_GEOMETRY.width()/2 - width/2)
		pos_y = int(SCREEN_GEOMETRY.height()/2 - height/2)

		with open("app/style.qss") as style:
			self.setStyleSheet(style.read())
		
		self.setWindowTitle("Blender Hub v0.1.0")
		self.setGeometry(pos_x, pos_y, width, height)
		
		central_widget = Frame()
		
		pages = Pages()
		sidebar = Sidebar()
		sidebar.pageChanged.connect(lambda page: pages.changePage(page))
		
		central_widget.addWidget(sidebar)
		central_widget.addWidget(pages)

		self.setCentralWidget(central_widget)
		self.show()
