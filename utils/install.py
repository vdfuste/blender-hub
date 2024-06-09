from os import mkdir, path
from shutil import rmtree
from sys import platform
from subprocess import call, run, Popen, CalledProcessError
from PyQt5.QtWidgets import QDialog

from pages.dialogs.password import PasswordDialog

from utils.blender.run import get_version

def installBlender(version, url, parent):
	if platform == "linux" or platform == "linux2": installOnLinux(version, url, parent)
	elif platform == "win32": installOnWindow(version, url, parent)
	elif platform == "darwin": installOnMac(version, url, parent)
	else: print("Apparently your OS is not supported. Please contact me and let's see what I can do to fix that.")

def installOnLinux(version, url, parent):
	password_dialog = PasswordDialog(version, parent)
	
	if password_dialog.exec_() == QDialog.Accepted:
		password = password_dialog.getPassword()
		
		# Getting the file name from the url excluding the extension 
		extension = ".tar.xz"
		blender_file = path.split(url)[-1]
		blender_folder = blender_file.replace(extension, "")
		
		try:
			# Create a temporal directory and navigate to it,
			# sudo is used to insert the password before the download.
			# run(["sudo", "-S", "mkdir", "-p", "temp"], input=password.encoded(), check=True)
			run(["sudo -S mkdir -p temp".split()], input=password.encoded(), check=True)
			
			# Download installation file if not exists
			if not path.isfile(f"temp/{blender_file}"):
				run(f"curl -o temp/{blender_file} {url}".split(), check=True)
			
			# Extract file content
			run(f"tar -xf temp/{blender_file}".split(), check=True)

			# Move content
			run(f"sudo mv {blender_folder} /opt/blender".split(), check=True)

			# Create alias (optional)
			# run(f"sudo ln -s /opt/blender/{blender_folder}/blender /usr/local/bin/blender".split(), check=True)

			#Execute the application to generate the config files
			get_version(f"/opt/blender/{blender_folder}")

			# Remove the temporal folder with the installation file
			run(f"rm -rf temp".split(), check=True)
		
		except CalledProcessError as e:
			print(f"Failed to install Blender: {e}")

		except Exception as e:
			print(f"Failed to install Blender: {e}")

def installOnWindow(version, url, parent):
	# extension = ".msi"
	# blender_file = path.split(url)[-1].replace(extension)

	commands = []

def installOnMac(version, url, parent):
	# extension = ".dmg"
	# blender_file = path.split(url)[-1].replace(extension)

	commands = []

def uninstallBlender(version, url, parent):
	pass
