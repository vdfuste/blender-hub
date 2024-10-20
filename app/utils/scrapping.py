import requests
from bs4 import BeautifulSoup

from app.globals import BLENDER_RELEASES_URL, BLENDER_ALL_VERSIONS_URL

def getAvailableVersions():
	'''
	Scrapping all the available Blender versions from the website.

	Return:
	 An array of strings with all the available versions.
	 If the connection fails returns an empty list.
	'''

	try:
		# Get all available versions (mayor and minor)
		cards_response = requests.get(BLENDER_RELEASES_URL)
		html = BeautifulSoup(cards_response.text, "html.parser")
		cards = html.find_all("div", { "class": "cards-list-item-inner" })

		versions = []
		
		for card in cards:
			title = card.find("a", { "class": "cards-list-item-title" }).text
			url_image = card.find("img")["src"]
			version = title.replace("Blender ", "").replace(" LTS", "")

			version = {
				"title": title,
				"urlImage": card.find("img")["src"],
				"subversions": []
			}

			# Get all subversions for current version
			subversions_response = requests.get(BLENDER_ALL_VERSIONS_URL)
			
			versions.append(version)

			print(version)

		return versions
	
	except Exception as e:
		print(f"Error checking new available versions. {e}")
		
		return []
