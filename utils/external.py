from os import makedirs, path, remove
from time import ctime

class ExternalList():
	def __init__(self, file_path):
		super().__init__()
		self.items = []
		self.file_path = file_path
		self.read()
	
	def addItem(self, item):
		self.items.append(item)

		# Append path to end of "projects.txt" file
		try:
			with open(self.file_path, 'a') as file:
				for item in self.items:
					file.write(item)

		except IOError as error:
			print(f"An error ocurred writing the file: {error}")
	
	def read(self):
		try:
			# Reading the stored paths from "projects.txt" file
			with open(self.file_path, 'r') as file:
				self.items = []
				
				for line in file:
					if line != '\n' or line != None:
						self.items.append(line[:-1]) # Last character '\n' is removed

		except FileNotFoundError:
			folder_path = path.split(self.file_path)[0]
			
			# Check if folder exists
			if not path.exists(folder_path):
				makedirs(folder_path)
			
			# If the file not exists it will be created
			with open(self.file_path, 'w') as file:
				pass # Do nothing
	
	def write(self):
		# Write all the paths on "projects.txt" file
		try:
			with open(self.file_path, 'w') as file:
				for item in self.items:
					file.write(item + '\n')

		except IOError as error:
			print(f"An error ocurred writing the file: {error}")

class ProjectsList(ExternalList):
	'''
	TO-DO list:
	 - Check if projects are still available
	'''
	def __init__(self, file_path):
		super().__init__(file_path)
	
	def readProjects(self):
		super().read()
	
	def writeProjects(self):
		super().write()
	
	def addProject(self, fileName):
		_date = ctime(path.getmtime(fileName))
		_version = "4.1.1"
		_data = f"{fileName};{_date};{_version}"

		self.items.append(_data)
		self.writeProjects()

		return [_data, len(self.items) - 1]

	def removeProject(self, index, delete):
		# Delete file from disk
		if delete:
			remove(self.items[index].split(';')[0])
		
		del self.items[index]
		self.write()
