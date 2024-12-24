from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QMenu, QSizePolicy
from PyQt5.QtGui import QPixmap

from components.custom.frame import Frame

class Button(Frame):
	clicked = pyqtSignal()
	
	def __init__(self, label="", icon="", name="button", align=Qt.AlignCenter):
		super().__init__(name)
		
		self.initUI(label, icon, name, align)

	def initUI(self, label, icon, name, align):
		self.loadStyle(__file__)

		self.label = QLabel(label)
		self.label.setObjectName("label")
		self.label.setAlignment(align)
		self.addWidget(self.label)

		#layout.addStretch()

		self.icon = QLabel()
		self.icon.setObjectName("icon")
		self.icon.hide()
		
		if icon != "":
			self.icon.setPixmap(QPixmap(icon))
			self.icon.show()
		
		self.addWidget(self.icon)

	def mousePressEvent(self, event):
		self.clicked.emit()
	
	def setLabel(self, label):
		self.label.setText(label)

class OptionsButton(Button):
	def __init__(self):
		super().__init__("⋮", name="options-button")

		self._menu = QMenu()
		
	def addAction(self, label, action):
		new_action = self._menu.addAction(label)
		new_action.triggered.connect(action)

	def show(self):
		pos = QPoint(0, 32)
		self._menu.exec_(self.mapToGlobal(pos))

	def mousePressEvent(self, event):
		self.show()
