import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QStackedWidget, QDialog
from PyQt5.QtGui import QFont, QFontDatabase
from utils.read import loadStyle

from components.pages import Pages
from components.sidebar import Sidebar

from globals import app, SCREEN_GEOMETRY

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# Window config
		width = 1024
		height = 720
		pos_x = int(SCREEN_GEOMETRY.width()/2 - width/2)
		pos_y = int(SCREEN_GEOMETRY.height()/2 - height/2)
		
		self.setWindowTitle("Blender Hub v0.1.0")
		self.setGeometry(pos_x, pos_y, width, height)
		
		# Style
		loadStyle("src/qss/style.qss", self)
		
		# Layout
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		
		# Widgets
		pages = Pages(self)
		sidebar = Sidebar(pages.changePage)
		
		layout.addWidget(sidebar)
		layout.addWidget(pages)

		central_widget = QWidget()
		central_widget.setLayout(layout)

		self.setCentralWidget(central_widget)
		self.show()

if __name__ == "__main__":
	window = MainWindow()
	sys.exit(app.exec_())
