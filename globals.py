from os import getenv, path
from sys import platform

from utils.external import ProjectsList


# Constant Variables
# Getting some paths based on the OS
if platform == "linux" or platform == "linux2":
	TEMP_USER_FOLDER = path.join(path.expanduser("~"), ".cache")

elif platform == "win32":
	TEMP_USER_FOLDER = getenv("LOCALAPPDATA")

#elif platform == "darwin":
#	TEMP_USER_FOLDER = "MacOS"

APP_NAME_FOLDER = "blender_hub"
PROJECTS_FILE_NAME = "projects.txt"
TEMP_FOLDER_PATH = path.join(TEMP_USER_FOLDER, APP_NAME_FOLDER)
PROJECTS_FILE_PATH = path.join(TEMP_FOLDER_PATH, PROJECTS_FILE_NAME)


# Global Objects
projects = ProjectsList(PROJECTS_FILE_PATH)
