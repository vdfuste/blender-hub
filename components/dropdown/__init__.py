from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QPixmap

from globals import SCREEN_GEOMETRY

class MenuItem(QWidget):
	clicked = pyqtSignal()

	def __init__(self, title, name="menu-item"):
		super().__init__()
		self.initUI(title)

	def initUI(self, title):
		self.loadStyle("components/dropdown")

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		item = QWidget()
		item.setObjectName("menu-item")
		item_layout = QVBoxLayout()
		item_layout.setContentsMargins(0, 0, 0, 0)
		item_layout.setSpacing(0)

		label = QLabel(title)
		item_layout.addWidget(label)

		item.setLayout(item_layout)
		layout.addWidget(item)

		self.setLayout(layout)

	def loadStyle(self, path):
		with open(f"{path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def mousePressEvent(self, event):
		self.clicked.emit()

class Menu(QWidget):
	optionChanged = pyqtSignal(str)
	
	def __init__(self):
		super().__init__()

		self.hide()
		self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.initUI()

	def initUI(self):
		self.loadStyle("components/dropdown")

		# Shadow effect
		shadow = QGraphicsDropShadowEffect()
		shadow.setBlurRadius(24)
		shadow.setOffset(0, 4)
		shadow.setColor(QColor(0, 0, 0, 128))
		self.setGraphicsEffect(shadow)

		layout = QVBoxLayout()
		layout.setContentsMargins(24, 24, 28, 24)

		menu = QWidget()
		menu.setObjectName("menu")
		self.menu_layout = QVBoxLayout()
		self.menu_layout.setContentsMargins(0, 0, 0, 0)
		self.menu_layout.setSpacing(0)

		menu.setLayout(self.menu_layout)
		layout.addWidget(menu)

		self.setLayout(layout)

	def loadStyle(self, path):
		with open(f"{path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def addItem(self, label):
		item = MenuItem(label)
		item.clicked.connect(lambda label=label: self.clickItem(label))

		self.menu_layout.addWidget(item)
	
	def addTitle(self, title):
		title = QLabel(title)
		title.setObjectName("menu-title")
		self.menu_layout.addWidget(title)

	def popup(self, pos):
		self.move(pos)
		self.show()

	def clickItem(self, label):
		self.optionChanged.emit(label)
		self.hide()

class Dropdown(QWidget):
	def __init__(self, name="dropdown"):
		super().__init__()

		self.options = []
		self.menu = Menu()
		self.menu.optionChanged.connect(lambda label : self.setOption(label))

		self.initUI(name)

	def initUI(self, name):
		self.setFixedHeight(42)
		self.loadStyle("components/dropdown")

		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		dropdown = QWidget()
		dropdown.setObjectName(name)
		dropdown_layout = QHBoxLayout()
		dropdown_layout.setContentsMargins(16, 0, 0, 0)
		dropdown_layout.setSpacing(0)

		self.label = QLabel()
		self.label.setObjectName("text")
		self.label.setContentsMargins(0, 0, 0, 0)
		dropdown_layout.addWidget(self.label)

		dropdown_layout.addStretch()

		icon = QLabel()
		icon.setObjectName("icon")
		icon.setContentsMargins(16, 0, 16, 0)
		icon.setPixmap(QPixmap("src/images/icons/caret-down.svg"))
		dropdown_layout.addWidget(icon)

		dropdown.setLayout(dropdown_layout)
		layout.addWidget(dropdown)

		self.setLayout(layout)

	def loadStyle(self, path):
		with open(f"{path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def mousePressEvent(self, event):
		global_pos = self.mapToGlobal(self.pos())

		# Moving menu to left if it's to close to right border screen
		if(global_pos.x() < SCREEN_GEOMETRY.width()/2):
			offset = QPoint(self.width(), -self.height() - 10)
		else:
			offset = QPoint(-self.menu.width() + 12, -self.height() - 10)

		self.menu.popup(global_pos + offset)
	
	def getOption(self):
		return self.label.text()
	
	def setOption(self, label):
		self.label.setText(label)
	
	def setOptions(self, options):
		self.options = options

		# Write first item to label.
		# First option is selected by default.
		self.setOption(self.options[0]["items"][0])

		# Adding items to menu
		for option in self.options:
			self.menu.addTitle(option["title"])

			for item in option["items"]:
				self.menu.addItem(item)

		self.menu.adjustSize()
