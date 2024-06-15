from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from utils.read import loadStyle

from globals import SCREEN_GEOMETRY

'''
TO-DO list:
 - Launch "Accepted" when enter is pressed.
'''

class PasswordDialog(QDialog):
	def __init__(self, version, parent=None):
		super().__init__()
		
		width = 480
		height = 100
		pos_x = int(SCREEN_GEOMETRY.width()/2 - width/2)
		pos_y = int(SCREEN_GEOMETRY.height()/2 - height/2)
		
		loadStyle("src/qss/pages/dialogs/new_project.qss", self)

		# Init UI
		self.setParent(parent)
		self.setObjectName("password-dialog-page")
		self.setGeometry(pos_x, pos_y, width, height)
		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.Tool)

		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignTop)
		
		# Dialog Content
		title_label = QLabel("Enter the password to install", objectName="title")
		layout.addWidget(title_label)

		self.password_line = QLineEdit(objectName="input-text")
		self.password_line.setEchoMode(QLineEdit.Password)
		self.password_line.textChanged.connect(lambda: accept_btn.setDisabled(self.password_line.text() == ""))
		layout.addWidget(self.password_line)

		# Buttons
		wrap_buttons = QWidget()
		buttons_layout = QHBoxLayout()
		buttons_layout.setContentsMargins(0, 10, 0, 0)
		buttons_layout.addSpacing(0)
		
		cancel_btn = QPushButton("Cancel", objectName="border-btn")
		cancel_btn.clicked.connect(lambda: self.hide())
		buttons_layout.addWidget(cancel_btn)
		
		accept_btn = QPushButton(f"Install {version}", objectName="primary-border-btn")
		accept_btn.setDisabled(True)
		accept_btn.clicked.connect(self.accept)
		buttons_layout.addWidget(accept_btn)
		
		wrap_buttons.setLayout(buttons_layout)
		layout.addWidget(wrap_buttons)

		self.setLayout(layout)

	def open(self):
		self.reset()
		return self.exec_()
	
	def reset(self):
		self.password_line.setText("")
		self.password_line.setFocus(Qt.FocusReason.ActiveWindowFocusReason)

	def getPassword(self):
		return self.password_line.text()
