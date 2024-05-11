import requests
from bs4 import BeautifulSoup

from globals import BLENDER_ALL_VERSIONS_URL

def getAvailableVersions():
	# Scrapping all the available versions
	response = requests.get(BLENDER_ALL_VERSIONS_URL)
	html = BeautifulSoup(response.text, "html.parser")

	versions = html.find_all("a")

	for version in versions:
		if "Blender" in version.text:
			print(
				version.text
				.replace("Blender", "")
				.replace("/", "")
			)