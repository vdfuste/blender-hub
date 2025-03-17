from os.path import abspath, dirname, join

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
	QStackedWidget, QHBoxLayout, QVBoxLayout, QSizePolicy,
	QDialog, QLabel, QLineEdit
)

from components.custom.frame import Frame
from components.custom.button import Button

from globals import SCREEN_GEOMETRY

class TextInput(Frame):
	returnPressed = pyqtSignal()
	textChanged = pyqtSignal(str)

	def __init__(self, title="", *, name="", isPassword=False):
		super().__init__(name, QVBoxLayout)

		if title != None:
			self.title = QLabel(title, objectName="input-label")
			self.addWidget(self.title)

		self.text = QLineEdit(objectName="input-text")
		self.text.returnPressed.connect(self.returnPressed)
		self.text.textChanged.connect(lambda text=self.getText() : self.textChanged.emit(text))
		
		if isPassword:
			self.text.setEchoMode(QLineEdit.Password)
		
		self.addWidget(self.text)

	def getText(self):
		return self.text.text()
	
	def setText(self, text):
		return self.text.setText(text)

	def isEmpty(self):
		return self.getText() == ""
			
class Section(Frame):
	def __init__(self, layout=QVBoxLayout, *, name="dialog-section"):
		super().__init__(name, layout)

		self.setSpacing(12)
		
		self.sectionContent = Frame("dialog-content", layout)
		self.sectionContent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.sectionContent.layout.setAlignment(Qt.AlignTop)
		self.addWidget(self.sectionContent)

		self.buttons = Frame("dialog-buttons", QHBoxLayout)
		self.buttons.layout.setAlignment(Qt.AlignCenter)
		self.buttons.setSpacing(2)
		self.addWidget(self.buttons)
		
	def initAction(self):
		pass

	def addWidget2(self, widget):
		self.sectionContent.addWidget(widget)
	
	def addButton(self, button):
		self.buttons.addWidget(button)

	def accept(self):
		self.parent().parent().accept()

	def cancel(self):
		self.parent().parent().reject()

	def next(self):
		self.parent().parent().next()

	def prev(self):
		self.parent().parent().prev()

	def setDefaultButtons(self, *, prevLabel="Back", nextLabel="Next"):
		self.secondBtn = Button(prevLabel, name="border-button")
		self.secondBtn.clicked.connect(self.secondAction)
		self.addButton(self.secondBtn)
		
		self.primaryBtn = Button(nextLabel, name="primary-button")
		self.primaryBtn.clicked.connect(self.primaryAction)
		self.addButton(self.primaryBtn)

	def primaryAction(self):
		self.next()

	def secondAction(self):
		self.cancel()

class Dialog(QDialog):
	def __init__(self, parent=None, *, name="dialog"):
		super().__init__()
		
		self.setParent(parent)
		self.setObjectName(name)
		self.loadStyle(__file__)

		layout = QVBoxLayout()

		self.currentSection = 0
		self.sections = QStackedWidget()
		self.sections.setObjectName("ksjbfdvkjf")
		layout.addWidget(self.sections)
		
		self.setLayout(layout)
		
	def loadStyle(self, file):
		path = dirname(abspath(file))
		with open(join(path, "style.qss")) as style:
			self.setStyleSheet(style.read())
	
	def initWindow(self, *, title="Dialog", width=640, height=480):
		posX = int(SCREEN_GEOMETRY.width()/2 - width/2)
		posY = int(SCREEN_GEOMETRY.height()/2 - height/2)

		self.setWindowTitle(title)
		self.setGeometry(posX, posY, width, height)
		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.Tool)
	
	def addSection(self, section):
		self.sections.addWidget(section)
		
	def next(self):
		if self.currentSection < self.sections.count() - 1:
			self.currentSection += 1
			self.sections.setCurrentIndex(self.currentSection)
			self.sections.currentWidget().initAction()
	
	def prev(self):
		if self.currentSection > 0:
			self.currentSection -= 1
			self.sections.setCurrentIndex(self.currentSection)
