from os import listdir, path

class InstalledVersionsList():
	def __init__(self, installs_path):
		self.installs_path = installs_path
		self.installed = []
		self.paths = {}
		self.check()

	def check(self):
		try:
			if path.isdir(self.installs_path):
				for item in listdir(self.installs_path):
					
					version_path = path.join(self.installs_path, item)
					
					if path.isdir(version_path):
						version = listdir(version_path)[0]
						self.installed.append(version)
						self.paths[version] = version_path
		
		except Exception as e:
			print(f"Error checking installed versions: {e}")