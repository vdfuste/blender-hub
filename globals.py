from os import getenv, path
from sys import platform

from utils.external import ProjectsList

# Constant Variables
# Getting some paths based on the OS
if platform == "linux" or platform == "linux2":
	USER_FOLDER = path.expanduser("~")
	DOCUMENTS_FOLDER = path.join(USER_FOLDER, "Documents")
	TEMP_USER_FOLDER = path.join(USER_FOLDER, ".cache")

elif platform == "win32":
	USER_FOLDER = getenv("USERPROFILE")
	DOCUMENTS_FOLDER = path.join(USER_FOLDER, "Documents")
	TEMP_USER_FOLDER = getenv("LOCALAPPDATA")

#elif platform == "darwin":
#	DOCUMENTS_FOLDER = Path.home()/"Documents"
#	TEMP_USER_FOLDER = "MacOS"

APP_NAME_FOLDER = "blender_hub"
PROJECTS_FILE_NAME = "projects.txt"
TEMP_FOLDER_PATH = path.join(TEMP_USER_FOLDER, APP_NAME_FOLDER)
PROJECTS_FILE_PATH = path.join(TEMP_FOLDER_PATH, PROJECTS_FILE_NAME)

BLENDER_ALL_VERSIONS_URL = "https://download.blender.org/release"
BLENDER_DOWNLOADS_URL = "https://download.blender.org/release/Blender"

# Global Objects
projects = ProjectsList(PROJECTS_FILE_PATH)
