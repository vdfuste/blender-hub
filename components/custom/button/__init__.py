from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSizePolicy
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
