from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

from components.custom.frame import Frame
from components.custom.menu import Menu

from globals import SCREEN_GEOMETRY

class Dropdown(Frame):
	optionSelected = pyqtSignal(str)
	
	def __init__(self, name="dropdown"):
		super().__init__(name)

		self.menu = Menu()
		self.menu.optionSelected.connect(lambda option : self.optionChanged(option))

		self.initUI(name)

	def initUI(self, name):
		self.loadStyle(__file__)

		self.setFixedHeight(42)
		self.layout.setContentsMargins(16, 0, 0, 0)
		#self.layout.setSpacing(0)

		self.label = QLabel()
		self.label.setObjectName("text")
		self.label.setContentsMargins(0, 0, 0, 0)
		self.addWidget(self.label)

		self.layout.addStretch()

		icon = QLabel()
		icon.setObjectName("icon")
		icon.setContentsMargins(16, 0, 16, 0)
		icon.setPixmap(QPixmap("resources/images/icons/caret-down.svg"))
		self.addWidget(icon)

	def mousePressEvent(self, event):
		global_pos = self.mapToGlobal(QPoint(0, 48))
		self.menu.popup(global_pos)
	
	def getOption(self):
		return self.label.text()
	
	def setOption(self, label):
		self.label.setText(label)
	
	def setOptions(self, options):
		# Write first item to label.
		# First option is selected by default.
		default_written = False

		# Adding items to menu
		for option in options:
			if len(option["items"]) == 0:
				continue

			if "title" in option and option["title"] != "":
				self.menu.addTitle(option["title"])

			for item in option["items"]:
				if not default_written:
					self.setOption(item)
					default_written = True

				self.menu.addItem(item)

		self.menu.adjustSize()

	def optionChanged(self, option):
		self.setOption(option)
		self.optionSelected.emit(option)
