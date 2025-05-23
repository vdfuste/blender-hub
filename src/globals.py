import sys
from os import getenv, path
from sys import platform
from PyQt5.QtWidgets import QApplication
from utils.external_files import ConfigList, DownloadList, InstallsDataList, InstalledVersionsList

# Constant Variables
application = QApplication(sys.argv)
SCREEN_GEOMETRY = application.desktop().screenGeometry()

# Getting some paths based on the OS
if platform == "linux" or platform == "linux2":
	BLENDER_INSTALLS_FOLDER = "/opt/blender"
	USER_FOLDER = path.expanduser("~")
	DOCUMENTS_FOLDER = path.join(USER_FOLDER, "Documents")
	TEMP_USER_FOLDER = path.join(USER_FOLDER, ".cache")
	CONFIG_USER_FOLDER = path.join(USER_FOLDER, ".config", "blender")

elif platform == "win32":
	BLENDER_INSTALLS_FOLDER = "C:/Program Files/Blender Foundation"
	USER_FOLDER = getenv("USERPROFILE")
	DOCUMENTS_FOLDER = path.join(USER_FOLDER, "Documents")
	# C:\Users\Victor\AppData\Roaming\Blender Foundation\Blender (APPDATA)
	TEMP_USER_FOLDER = getenv("LOCALAPPDATA")

#elif platform == "darwin":
#	DOCUMENTS_FOLDER = Path.home()/"Documents"
#	TEMP_USER_FOLDER = ""

APP_NAME_FOLDER = "blender_hub"
PROJECTS_FILE_NAME = "projects.txt"
DOWNLOADS_FILE_NAME = "url_downloads.txt"
TEMP_FOLDER_PATH = path.join(TEMP_USER_FOLDER, APP_NAME_FOLDER)
PROJECTS_FILE_PATH = path.join(TEMP_FOLDER_PATH, PROJECTS_FILE_NAME)
DOWNLOADS_FILE_PATH = path.join(TEMP_FOLDER_PATH, DOWNLOADS_FILE_NAME)

BLENDER_RELEASES_URL = "https://www.blender.org/download/releases"
BLENDER_ALL_VERSIONS_URL = "https://download.blender.org/release"

VERSIONS_DATA_GIST_URL = "https://gist.githubusercontent.com/vdfuste/7b04b1851999fa8c38b4798f27b1a0c0/raw/blender-hub-installs.json"

# Global Objects
versions = InstalledVersionsList(BLENDER_INSTALLS_FOLDER)
# projects = ProjectsList(PROJECTS_FILE_PATH, versions)
downloads = DownloadList(DOWNLOADS_FILE_PATH)
config = ConfigList(CONFIG_USER_FOLDER)

installs = InstallsDataList()
installs.fetch_data(VERSIONS_DATA_GIST_URL)
