from os import makedirs, path, remove
from time import ctime

from app.utils.blender.run import get_project_version

from app.globals import versions

'''
TO-DO list:
 * ProjectsList:
  - Check if projects are still available
'''

class ProjectsData():
	'''
	Reads an external .txt file and creates a list, if the file doesn't exists it will be created.
	Any change updates both the external file and the list keeping them synchonized.

	Args:
	
	file_path: Path to the external file.
	'''
	def __init__(self, file_path):
		
		self.file_path = file_path
		self.items = []
		self.read()
	
	def read(self):
		try:
			# Reading the stored paths from "projects.txt" file
			with open(self.file_path, 'r') as file:
				# Clean the content
				self.items = []
				
				for line in file:
					if line != '\n' or line != None:
						file_name, date, version = line[:-1].split(';')  # Last character '\n' is removed
						
						data = {
							"file_name": file_name,
							"date": date,
							"version": version,
						}
						
						self.items.append(data)

		except FileNotFoundError:
			_folder_path = path.split(self.file_path)[0]
			
			# Check if folder exists
			if not path.exists(_folder_path):
				makedirs(_folder_path)
			
			# If the file not exists it will be created
			with open(self.file_path, 'w') as file:
				pass # Do nothing
	
	def write(self):
		# Write all the paths on "projects.txt" file
		try:
			with open(self.file_path, 'w') as file:
				for item in self.items:
					file.write(self.parseToText(item) + '\n')

		except IOError as error:
			print(f"[Blender Hub] An error ocurred writing the file: {error}")
	
	def addProject(self, file_name, date="", version="", index=None, check_path=""):
		# Generate some data
		date = date if date != "" else ctime(path.getmtime(file_name))
		version = version if version != "" else get_project_version(file_name)

		# When the version has "?" means the subversion is not defined
		# so the higher subversion will be assignated.
		if "?" in version:
			version = version.replace("?", "")
			
			for vi in versions.installed:
				if version in vi:
					version = vi
					break
		
		data = {
			"file_name": file_name,
			"date": date,
			"version": version,
		}

		if index is None:
			index = len(self.items)

		self.items.insert(index, data)
		self.write()

		return [data, len(self.items) - 1]
	
	def parseToText(self, data):
		return f'{data["file_name"]};{data["date"]};{data["version"]}'
	
	def removeProject(self, index, delete=False):
		# Delete both .blend and .blend1 files from disk
		if delete:
			file_name = self.items[index]["file_name"]
			
			if path.isfile(file_name): remove(file_name)
			if path.isfile(file_name + "1"): remove(file_name + "1")
		
		# Remove the item
		del self.items[index]
		self.write()
