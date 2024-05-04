import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QStackedWidget
from utils.read import loadStyle

from components.pages import Pages
from components.sidebar import Sidebar

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		# Window config
		self.setWindowTitle("Blender Hub v0.1.0")
		self.setGeometry(100, 100, 1024, 720)

		# Widgets
		pages = Pages()
		sidebar = Sidebar(pages.changePage)

		# Layout
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		layout.addWidget(sidebar)
		layout.addWidget(pages)

		central_widget = QWidget()
		central_widget.setLayout(layout)
		self.setCentralWidget(central_widget)

		# Style
		loadStyle("src/qss/style.qss", self)

		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
