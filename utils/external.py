from os import makedirs, path, remove
from time import ctime

# from utils.scrapping import getAvailableVersions

'''
TO-DO list:
 * ProjectsList:
  - Check if projects are still available
'''

class ExternalList():
	'''
	Reads an external .txt file and creates a list,
	if the file doesn't exists it will be created.
	Any change updates both the external file and
	the list keeping them synchonized.

	Args:
	
	file_path: Path to the external file.
	'''
	def __init__(self, file_path):
		super().__init__()

		self.file_path = file_path
		self.items = []
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
					file.write(item + '\n')

		except IOError as error:
			print(f"An error ocurred writing the file: {error}")

class ProjectsList(ExternalList):
	def __init__(self, file_path):
		super().__init__(file_path)
	
	def readProjects(self):
		super().read()
	
	def writeProjects(self):
		super().write()
	
	def addProject(self, fileName):
		_date = ctime(path.getmtime(fileName))
		_version = "3.6"
		_data = f"{fileName};{_date};{_version}"
	
	def addProject(self, file_name):
		# Generate some data
		_date = ctime(path.getmtime(file_name))
		_version = "4.1.1"
		_data = f"{file_name};{_date};{_version}"

		self.items.append(_data)
		self.writeProjects()

		return [_data, len(self.items) - 1]
	
	def removeProject(self, index, delete):
		# Delete file from disk
		if delete:
			remove(self.items[index].split(';')[0])
		
		# Remove the item
		del self.items[index]
		self.write()

class DownloadList():
	def __init__(self, file_path):
		super().__init__()

		# self.urls = ExternalList(file_path)
		self.versions = [
			{
				"serie": "4",
				"cards": [
					{
						"version": "4.1",
						"image": "src/images/blender_4_1_splash.jpg",
						"subversions": [
							{
								"subversion": "4.1.1",
								"url":
								# Linux
								"https://download.blender.org/release/Blender4.1/blender-4.1.1-linux-x64.tar.xz"
								
								# Windows
								# "https://download.blender.org/release/Blender4.1/blender-4.1.1-windows-x64.msi"

								# MacOS
								# "https://download.blender.org/release/Blender4.1/blender-4.1.1-macos-x64.dmg"
								# "https://download.blender.org/release/Blender4.1/blender-4.1.1-macos-arm64.dmg"
							},
							{
								"subversion": "4.1.0",
								"url": "https://download.blender.org/release/Blender4.1/blender-4.1.0-linux-x64.tar.xz"
							}
						]
					},
					{
						"version": "4.0",
						"image": "src/images/blender_40_splash.jpg",
						"subversions": [
							{
								"subversion": "4.0.2",
								"url": "https://download.blender.org/release/Blender4.0/blender-4.0.2-linux-x64.tar.xz"
							},
							{
								"subversion": "4.0.1",
								"url": "https://download.blender.org/release/Blender4.0/blender-4.0.1-linux-x64.tar.xz"
							},
							{
								"subversion": "4.0.0",
								"url": "https://download.blender.org/release/Blender4.0/blender-4.0.0-linux-x64.tar.xz"
							}
						]
					}
				]
			},
			{
				"serie": "3",
				"cards": [
					{
						"version": "3.6 LTS",
						"image": "src/images/blender_36_lts_splash.jpg",
						"subversions": [
							{
								"subversion": "3.6.9",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.9-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.8",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.8-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.7",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.7-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.5",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.5-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.4",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.4-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.3",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.3-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.2",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.2-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.12",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.12-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.11",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.11-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.10",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.10-linux-x64.tar.xz"
							},
							{
								"subversion": "3.6.0",
								"url": "https://download.blender.org/release/Blender3.6/blender-3.6.0-linux-x64.tar.xz"
							},
						]
					},
				]
			},
		]

	def checkUpdates(self):
		# versions = getAvailableVersions()
		pass
