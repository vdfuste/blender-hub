import sys

def loadStyle(path, widget):
	with open(path, "r") as f:
		widget.setStyleSheet(f.read())