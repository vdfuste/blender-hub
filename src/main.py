import sys

from window import MainWindow
from globals import application

def run():
	window = MainWindow()
	sys.exit(application.exec_())

if __name__ == "__main__":
	run()
