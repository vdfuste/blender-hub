from os import path
from subprocess import Popen, run, CalledProcessError, DEVNULL

def get_version(blender_path):
	try:
		blender_path = path.join(blender_path, "blender")
		output = run([blender_path, "--version"], capture_output=True, text=True).stdout
		
		return output.split('\n')[0].replace("Blender ", "")
	
	except CalledProcessError:
		print("[Blender Hub] Error checking Blender version.")

def get_project_version(file_name):
	try:
		with open(file_name, "rb") as file:
			# Output shold look "BLENDER-vXYZ"
			output = file.read(12).decode("utf-8")

		mayor, minor = (int(output[9]), int(output[10:]))

		return f"{mayor}.{minor}.?"
	
	except CalledProcessError:
		print("[Blender Hub] Error reading the project.")

def new_project(file_name, blender_path):
	try:
		blender_path = path.join(blender_path, "blender")
		Popen([blender_path, "-P", "utils/blender/scripts/new.py", file_name])
	
	except CalledProcessError:
		print("[Blender Hub] Error creating a new project.")

def open_project(file_name, blender_path):
	try:
		blender_path = path.join(blender_path, "blender")
		Popen([blender_path, file_name])
	
	except CalledProcessError:
		print("[Blender Hub] Error opening the project.")

def open_blender(blender_path):
	try:
		blender_path = path.join(blender_path, "blender")
		Popen(blender_path)
	
	except CalledProcessError:
		print("[Blender Hub] Error opening blender.")
