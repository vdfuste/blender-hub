import requests
from bs4 import BeautifulSoup

from globals import BLENDER_ALL_VERSIONS_URL

def getAvailableVersions():
	'''
	Scrapping all the available Blender versions from the website.

	Return:
	 An array of strings with all the available versions.
	 If the connection fails returns an empty list.
	'''
	
	try:
		response = requests.get(BLENDER_ALL_VERSIONS_URL)
		html = BeautifulSoup(response.text, "html.parser")
		links = html.find_all("a")

		versions = []
		
		for link in links:
			if "Blender" in link.text:
				versions.append(
					link.text
						.replace("Blender", "")
						.replace("/", "")
				)
		
		return versions
	
	except:
		print(f"Error checking new available versions.")
		
		return []
