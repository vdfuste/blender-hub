from requests import get
from bs4 import BeautifulSoup
from json import dumps

from globals import BLENDER_RELEASES_URL, BLENDER_ALL_VERSIONS_URL

"""
TO-DO List:
 - Consider the option to use ".msix" files.
"""

def getAllInstallers(platfom):
	all_versions = []

	def getLinks(url):
		links = []
		
		try:
			response = get(url)
			html = BeautifulSoup(response.text, "html.parser")
			anchors = html.find_all("a", href=True)

			for a in anchors:
				links.append(a["href"])

			return links

		except Exception as e:
			print(f"Error getting links from {url}. Error: {e}")
			return []
	
	# Getting all the directories
	for directory in getLinks(BLENDER_ALL_VERSIONS_URL):
		# "directory" should look like "Blender4.2/", 
		# if it looks like "BlenderBenchmark2.0"
		# or something else it will be skipped.
		
		# Skipping specific versions and Benchmarks.
		skip_versions = ["1.0", "1.60", "1.73", "1.80", "2.04", "Benchmark"]
		
		for version in skip_versions:
			if version in directory: continue
		
		# Checking if it's a Blender directory.
		if "Blender" in directory:
			card_version = {
				"version": directory[:-1],
				"subversions": [],
				"urls": [],
				"image": "url/to/image.jpg"
			}

			# Getting every single link on the directory.
			# The url should look like "https://download.blender.org/release/Blender4.2/".
			for link in getLinks(f"{BLENDER_ALL_VERSIONS_URL}/{directory}"):
				# "link" should look like "blender-4.2.0-linux-x64.tar.xz".
				
				# The version is surrounded by "-" so in order to get
				# the version "link" is splitted by "-".
				url = link.split('-')
				full_version = url[1]

				# All the urls starts with "blender-version-", there is no need
				# to store that part of the url so it can be removed.
				url = '-'.join(url[2:])

				# Store all the available versions in the directory
				if full_version not in card_version["subversions"]:
					card_version["subversions"].insert(0, full_version)
				
				# Storing the urls 
				if url not in card_version["urls"]:
					card_version["urls"].insert(0, url)
				
				# Getting all the data.
				# The data must be generated based on the specified platform.
				# Checking if "Linux" or "linux" is on the link.
				if platform == "linux" and "inux" in link:
						getData(version, link)
				
				# Checking if is a Windows file
				elif platform == "windows" and (".msi" in link or ".exe" in link):
						getData(version, link)
			
			all_versions.insert(0, version)

	#file = open("all_installers.txt", "w")
	#file.close()

getAllInstallers()
