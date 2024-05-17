from os import path
from subprocess import Popen, CalledProcessError

from globals import BLENDER_INSTALLS_FOLDER

def new_project(file_name, blender_version):
	try:
		_blender_path = path.join(blender_version, "blender")

		Popen([_blender_path, "-P", "utils/blender/scripts/new.py", file_name])
	
	except CalledProcessError:
		print("BLENDER HUB: Error creating a new project.")

def open_project(file_name, blender_version):
	try:
		_blender_path = path.join(blender_version, "blender")

		Popen([_blender_path, file_name])
	
	except CalledProcessError:
		print("BLENDER HUB: Error opening the project.")