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
						"image": "app/src/images/splash/blender_4_2_splash.webp",
						"subversions": [
							{
								"subversion": "4.2.0",
								"url": "https://download.blender.org/release/Blender4.2/blender-4.2.0-linux-x64.tar.xz"
							}
						]
					},
					{
						"version": "4.1",
						"image": "app/src/images/splash/blender_4_1_splash.jpg",
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
						"image": "app/src/images/splash/blender_40_splash.jpg",
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
						"image": "app/src/images/splash/blender_36_lts_splash.jpg",
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
