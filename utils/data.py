from os import getenv
from sys import platform

if platform == "linux" or platform == "linux2":
	# Linux
	path = "Linux"
elif platform == "win32":
	# Windows
	path = getenv("LOCALAPPDATA")
elif platform == "darwin":
	# MacOS
	path = "MacOS"


def loadProjects():
	#with open("projects.txt") as projects:
	#	for project in projects:
	#		print(project)
	print(path)
