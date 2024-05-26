from os import path
from subprocess import Popen, run, CalledProcessError, DEVNULL

def get_version(file_name):
	try:
		_blender_path = path.join(file_name, "blender")
		_output = run([_blender_path, "--version"], capture_output=True, text=True).stdout
		
		return _output.split('\n')[0].replace("Blender ", "")
	
	except CalledProcessError:
		print("BLENDER HUB: Error opening the project.")

def new_project(file_name, blender_path):
	try:
		blender_path = path.join(blender_path, "blender")

		Popen([blender_path, "-P", "utils/blender/scripts/new.py", file_name])
	
	except CalledProcessError:
		print("BLENDER HUB: Error creating a new project.")

def open_project(file_name, blender_path):
	try:
		blender_path = path.join(blender_path, "blender")

		Popen([blender_path, file_name])
	
	except CalledProcessError:
		print("BLENDER HUB: Error opening the project.")
