from os import listdir, path

from utils.blender.run import get_version

class InstalledVersionsList():
	'''
	Get all the Blender versions installed on the system.
	
	Args:
	 installs_path: Path where all Blender versions are installed.
	'''
	def __init__(self, installs_path):
		self.installed = []
		self.paths = {}
		self.check(installs_path)

	def check(self, installs_path):
		try:
			if path.isdir(installs_path):
				# Getting all installed Blender versions
				for item in listdir(installs_path):
					_blender_path = path.join(installs_path, item)
					
					# Checking if it's a Blender folder
					# This is an optional step due to here only
					# should be auto-installed applications
					if path.isdir(_blender_path):
						_version = get_version(_blender_path)

						self.installed.append(_version)
						self.paths[_version] = _blender_path

		
		except Exception as e:
			print(f"Error checking installed versions: {e}")

class AvailableInstallsList():
	'''
	'''
	def __init__(self):
		pass
