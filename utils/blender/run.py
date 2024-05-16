from os import path
from subprocess import Popen, CalledProcessError

def new_project(file_name):
	try:
		_blender_path = f"/opt/blender/blender-4.1.1-linux-x64/blender"

		Popen([_blender_path, "-P", "utils/blender/scripts/new.py", file_name])
	
	except CalledProcessError:
		print(f"Error opening {self.project_name} project.")

def open_project(file_name):
	try:
		_blender_path = f"/opt/blender/blender-4.1.1-linux-x64/blender"

		Popen([_blender_path, file_name])
	
	except CalledProcessError:
		print(f"BLENDER HUB: Error opening {self.project_name} project.")