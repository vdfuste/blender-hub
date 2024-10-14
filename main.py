import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QStackedWidget, QDialog
from PyQt5.QtGui import QFont, QFontDatabase

from components.sidebar import Sidebar
from pages import Pages

from globals import app, SCREEN_GEOMETRY

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# Window config
		width = 1024
		height = 720
		pos_x = int(SCREEN_GEOMETRY.width()/2 - width/2)
		pos_y = int(SCREEN_GEOMETRY.height()/2 - height/2)

		with open("style.qss") as style:
			self.setStyleSheet(style.read())
		
		self.setWindowTitle("Blender Hub v0.1.0")
		self.setGeometry(pos_x, pos_y, width, height)
		
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		
		pages = Pages()
		sidebar = Sidebar()
		sidebar.pageChanged.connect(lambda page: pages.changePage(page))
		
		layout.addWidget(sidebar)
		layout.addWidget(pages)

		central_widget = QWidget()
		central_widget.setLayout(layout)

		self.setCentralWidget(central_widget)
		self.show()

if __name__ == "__main__":
	window = MainWindow()
	sys.exit(app.exec_())
