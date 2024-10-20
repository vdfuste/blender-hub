import sys

from app.window import MainWindow
from app.globals import application

if __name__ == "__main__":
	window = MainWindow()
	sys.exit(application.exec_())
