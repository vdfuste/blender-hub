from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QPixmap

from app.components.custom.frame import Frame

from app.globals import SCREEN_GEOMETRY

class MenuItem(Frame):
	clicked = pyqtSignal()

	def __init__(self, title, name="menu-item"):
		super().__init__(name)

		label = QLabel(title)
		self.addWidget(label)

	def mousePressEvent(self, event):
		self.clicked.emit()

class Menu(Frame):
	optionSelected = pyqtSignal(str)
	
	def __init__(self, name="menu", layout=QVBoxLayout):
		super().__init__(name, layout)

		self.hide()
		self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.initUI()

	def initUI(self):
		#self.loadStyle(__file__)

		# Shadow effect
		shadow = QGraphicsDropShadowEffect()
		shadow.setBlurRadius(24)
		shadow.setOffset(0, 4)
		shadow.setColor(QColor(0, 0, 0, 128))
		self.setGraphicsEffect(shadow)
		self.layout.setContentsMargins(24, 24, 28, 24)

	def addItem(self, label):
		item = MenuItem(label)
		item.clicked.connect(lambda label=label: self.clickItem(label))

		self.addWidget(item)
	
	def addTitle(self, title):
		title = QLabel(title)
		title.setObjectName("menu-title")
		self.addWidget(title)

	def popup(self, pos):
		self.move(pos)
		self.show()

	def clickItem(self, label):
		self.optionSelected.emit(label)
		self.hide()

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
		icon.setPixmap(QPixmap("app/src/images/icons/caret-down.svg"))
		self.addWidget(icon)

	def mousePressEvent(self, event):
		global_pos = self.mapToGlobal(self.pos())

		# Moving menu to left if it's to close to right border screen
		if(global_pos.x() < SCREEN_GEOMETRY.width()/2):
			offset = QPoint(self.width(), -self.height() - 10)
		else:
			offset = QPoint(-self.menu.width() + 12, -self.height() - 10)

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
