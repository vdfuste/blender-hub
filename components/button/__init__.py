from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap

class Button(QFrame):
	clicked = pyqtSignal()
	
	def __init__(self, label="", icon="", name="button", align=Qt.AlignCenter):
		super().__init__()
		
		self.initUI(label, icon, name, align)

	def initUI(self, label, icon, name, align):
		self.loadStyle("components/button")

		self.setObjectName(name)
		self.setFrameShape(QFrame.Panel)
		
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		self.label = QLabel(label)
		self.label.setObjectName("label")
		self.label.setAlignment(align)
		layout.addWidget(self.label)

		#layout.addStretch()

		self.icon = QLabel()
		self.icon.setObjectName("icon")
		self.icon.hide()
		
		if icon != "":
			self.icon.setPixmap(QPixmap(icon))
			self.icon.show()
		
		layout.addWidget(self.icon)
		
		self.setLayout(layout)

	def loadStyle(self, path):
		with open(f"{path}/style.qss") as style:
			self.setStyleSheet(style.read())

	def mousePressEvent(self, event):
		self.clicked.emit()
	
	def setLabel(self, label):
		self.label.setText(label)
