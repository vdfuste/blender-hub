from os import path

class InstalledVersions():
	def __init__(self, installs_path):
		self.read(installs_path)

	def read(self, installs_path):
		try:
			if path.isdir(installs_path): pass

		except Exception:
			print("Error getting installed versions")