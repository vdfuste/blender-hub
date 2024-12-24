from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

from components.custom.frame import Frame

from globals import SCREEN_GEOMETRY

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
		super().__init__(f"{name}-wrapper", layout)

		self.hide()
		self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.initUI(name)

	def initUI(self, name):
		self.loadStyle(__file__)
		self.layout.setContentsMargins(20, 24, 28, 24)

		self.menu = Frame(name, QVBoxLayout)
		self.addWidget(self.menu)
		
		# Shadow effect
		shadow = QGraphicsDropShadowEffect()
		shadow.setBlurRadius(24)
		shadow.setOffset(0, 4)
		shadow.setColor(QColor(0, 0, 0, 128))
		self.menu.setGraphicsEffect(shadow)

	def addItem(self, label):
		item = MenuItem(label)
		item.clicked.connect(lambda label=label: self.clickItem(label))
		self.menu.addWidget(item)
	
	def addTitle(self, title):
		title = QLabel(title)
		title.setObjectName("menu-title")
		self.menu.addWidget(title)

	def popup(self, pos):
		self.move(pos + QPoint(-24, -20))
		self.show()

	def clickItem(self, label):
		self.optionSelected.emit(label)
		self.hide()
