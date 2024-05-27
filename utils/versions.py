from os import listdir, path

from utils.blender.run import get_version

class InstalledVersionsList():
	'''
	Get all the Blender versions installed on the system.
	
	Args:
	 installs_path: Path where all Blender versions are installed.
	'''
	def __init__(self, installs_path):
		self.installs_path = installs_path
		self.installed = []
		self.paths = {}
		self.check()

	def check(self):
		try:
			# New data will be stored in local variables
			# so current data won't be overwritten if any
			# error ocurrs 
			_installed = []
			_paths = {}
			
			if path.isdir(self.installs_path):
				# Getting all installed Blender versions
				for item in listdir(self.installs_path):
					_blender_path = path.join(self.installs_path, item)
					
					# Checking if it's a Blender folder
					# This is an optional step due to here only
					# should be auto-installed applications
					if path.isdir(_blender_path):
						_version = get_version(_blender_path)

						_installed.append(_version)
						_paths[_version] = _blender_path

			# Update varibale with new data
			self.installed = _installed
			self.paths = _paths
		
		except Exception as e:
			print(f"Error checking installed versions: {e}")

class ConfigList():
	'''
	'''
	def __init__(self, config_path):
		self.config_path = config_path
		self.versions =[]
		self.check()

	def check(self):
		for version in listdir(self.config_path):
			self.versions.append(version)

		self.versions.sort()
