from requests import get
from bs4 import BeautifulSoup
from json import dump

from app.globals import BLENDER_RELEASES_URL, BLENDER_ALL_VERSIONS_URL

def getAllInstallers():
	installs = {
		"tabs": [
			{
				"title": "LTS",
				"indexes": [78, 75, 72, 68, 64]
			},
			{
				"title": "4.x",
				"indexes": [78, 76]
			},
			{
				"title": "3.x",
				"indexes": [75, 69]
			},
			{
				"title": "2.x",
				"indexes": [68, 0]
			}
		],
		"versions": []
	}

	def is_on_list(target, checks):
		isOnList = False
		for check in checks:
			if check in target:
				isOnList = True
				continue
		return isOnList
	
	def getReleases(url):
		data = []
		
		try:
			response = get(url)
			html = BeautifulSoup(response.text, "html.parser")
			cards = html.find_all("div", { "class": "cards-item-content" })

			for card in cards:
				#release_info = card.find("span", class_="cards-item-excerpt").p.text
				data.append({
					"image": card.find("img")["src"],
					"title": card.find(class_="cards-item-title").text
				})

			return data

		except Exception as e:
			print(f"Error getting all the cards from {url}. Error: {e}")
			return []
	
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
	for index, directory in enumerate(getLinks(BLENDER_ALL_VERSIONS_URL)):
		# "directory" should look like "Blender4.2/", 
		# if it looks like "BlenderBenchmark2.0"
		# or something else it will be skipped.
		
		# Skipping specific versions and Benchmarks.
		skip_versions = ["1.0", "1.60", "1.73", "1.80", "2.04", "Benchmark"]
		if is_on_list(directory, skip_versions): continue
		
		# Checking if it's a Blender directory.
		if "Blender" in directory:
			card_version = {
				"version": directory[:-1],
				"subversions": [],
				"urls": [],
				"image": ""
			}

			# Getting every single link on the directory.
			# The url should look like "https://download.blender.org/release/Blender4.2/".
			for link in getLinks(f"{BLENDER_ALL_VERSIONS_URL}/{directory}"):
				# "link" should look like "blender-4.2.0-linux-x64.tar.xz".
				# If not skip to next link.
				if not "blender" in link or is_on_list(link, ["md5", "sha256"]): continue
				
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
			
			installs["versions"].append(card_version)

	# Getting all the url thumb images
	for card in getReleases(BLENDER_RELEASES_URL):
		version = (card["title"]
			.replace(" ", "")
			.replace("Blender", "")
			.replace("LTS", "")
			.replace("Alpha1", "")
			.replace("Alpha2", "")
			.replace("Beta", ""))
		
		for data in installs["versions"]:
			if version in data["version"]:
				data["image"] = card["image"].replace("https://www.blender.org/wp-content/uploads/", "")

	# Saving data on JSON file
	with open("installs.json", "w") as file:
		dump(installs, file)

	# Print some data
	print("All data versions saved!")
	print(f"There's {len(installs["versions"])} versions.")

getAllInstallers()
