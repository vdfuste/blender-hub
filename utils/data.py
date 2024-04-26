from os import makedirs, getenv, path
from sys import platform

class ProjectsList():
	def __init__(self):
		super().__init__()

		self.items = []

		# Getting some paths based on the OS
		if platform == "linux" or platform == "linux2":
			data_path = path.join(path.expanduser("~"), ".cache")
		elif platform == "win32":
			data_path = getenv("LOCALAPPDATA")
		# elif platform == "darwin":
		# 	data_path = "MacOS"

		# Creating local paths
		folder_name = "blender_hub"
		file_name = "projects.txt"
		folder_path = path.join(data_path, folder_name)
		file_path = path.join(folder_path, file_name)

		# Reading the stored paths from "projects.txt" file,
		# if the file not exists it will be created
		try:
			with open(file_path, "r") as file:
				for line in file:
					if line != "\n" or line != None:
						project = line.split(";")
						self.items.append({
							"name": project[0],
							"path": project[1],
							"version": project[2],
						})

		except FileNotFoundError:
			if not path.exists(folder_path):
				makedirs(folder_path)
			
			with open(file_path, "w") as file:
				#file.write("Suzanne;~/Desktop/MonkeyHead;3.6.1")
				pass # Do nothing
	
	def addProject(self, project):
		self.items.append(project)

	def deleteProject(self, index):
		self.items.pop(index)
