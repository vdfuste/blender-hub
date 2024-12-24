import json
from os import listdir, path
from urllib.request import urlopen
from PyQt5.QtCore import pyqtSignal

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
			print(f"[Blender Hub] Error checking installed versions: {e}")

class ConfigList():
	'''
	'''
	def __init__(self, config_path):
		self.config_path = config_path
		self.versions = []
		self.check()

	def check(self):
		if path.isdir(self.config_path):
			for version in listdir(self.config_path):
				self.versions.append(version)

			self.versions.sort()

class InstallsDataList():
	data_loaded = pyqtSignal(list, list)
	
	def __init__(self):
		self.tabs = []
		self.versions = []

	def fetch_data(self, url):
		with urlopen(url) as json_data:
			data = json.load(json_data)

			self.tabs = data["tabs"]

			for index, version in enumerate(data["versions"]):
				_version = {
					"title": version["title"],
					"subversions": version["subversions"],
					"url_image": version["url_image"],
					"urls": {}
				}

				for url in version["urls"]:
					if "linux" in url:
						for sub in version["subversions"]:
							_url = f"https://download.blender.org/release/{version["title"]}/blender-{sub}-{url}"
							_version["urls"][sub] = _url
				
				self.versions.append(_version)
				#print(_version)
			
			#self.data_loaded.emit(self.tabs, self.versions)

class DownloadList():
	def __init__(self, file_path):
		super().__init__()

		self.series = [4, 3]
		self.versions = [
			{
				"serie": "4",
				"cards": [
					{
						"version": "4.2",
						"image": "resources/images/splash/blender_4_2_splash.webp",
						"subversions": [
							{
								"subversion": "4.2.0",
								"url": "https://download.blender.org/release/Blender4.2/blender-4.2.0-linux-x64.tar.xz"
							}
						]
					},
					{
						"version": "4.1",
						"image": "resources/images/splash/blender_4_1_splash.jpg",
						"subversions": [
							{
								"subversion": "4.1.1",
								"url": "https://download.blender.org/release/Blender4.1/blender-4.1.1-linux-x64.tar.xz"
							},
							{
								"subversion": "4.1.0",
								"url": "https://download.blender.org/release/Blender4.1/blender-4.1.0-linux-x64.tar.xz"
							}
						]
					},
					{
						"version": "4.0",
						"image": "resources/images/splash/blender_40_splash.jpg",
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
						"image": "resources/images/splash/blender_36_lts_splash.jpg",
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
