from os import mkdir, path
from shutil import rmtree
from sys import platform
from subprocess import call, run, Popen, CalledProcessError
from PyQt5.QtWidgets import QDialog

from pages.dialogs.password import PasswordDialog
from globals import CONFIG_USER_FOLDER

'''
TO-DO list:
 - Generate the config files folder when Blender had been installed.
'''

# Install methods
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
			# run(["sudo", "-S", "mkdir", "-p", "temp"], input=password.encode(), check=True)
			run("sudo -S mkdir -p temp".split(), input=password.encode(), check=True)
			
			# Download installation file if not exists
			if not path.isfile(f"temp/{blender_file}"):
				run(f"sudo curl -o temp/{blender_file} {url}".split(), check=True)
			
			# Extract file content
			run(f"tar -xf temp/{blender_file}".split(), check=True)

			# Move content
			run(f"sudo mv {blender_folder} /opt/blender".split(), check=True)

			# Create alias (optional)
			# run(f"sudo ln -s /opt/blender/{blender_folder}/blender /usr/local/bin/blender".split(), check=True)

			# TO-DO: Generate the config files

			# Remove the temporal folder with the installation file
			run(f"sudo rm -rf temp".split(), check=True)

			# Feedback message
			print(f"\nBlender {version} successfully installed.")
		
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

# Uninstall methods
def uninstallBlender(version, blender_path, parent):
	if platform == "linux" or platform == "linux2": uninstallOnLinux(version, blender_path, parent)
	elif platform == "win32": uninstallOnWindow(version, blender_path, parent)
	elif platform == "darwin": uninstallOnMac(version, blender_path, parent)
	else: print("Apparently your OS is not supported. Please contact me and let's see what I can do to fix that.")

def uninstallOnLinux(version, blender_path, parent):
	password_dialog = PasswordDialog(version, parent)

	print(blender_path)
	
	if password_dialog.exec_() == QDialog.Accepted:
		password = password_dialog.getPassword()
		
		try:
			# Remove the folder from /opt/blender
			if path.isdir(blender_path):
				run(f"sudo -S rm -rf {blender_path}".split(), input=password.encode(), check=True)

			# Remove the folder from .config/blender
			config_folder = path.join(CONFIG_USER_FOLDER, version[:-2])
			if path.isdir(config_folder):
				run(f"sudo rm -rf {config_folder}".split(), check=True)

			# Feedback message
			print(f"\nBlender {version} successfully uninstalled.")

		except Exception as e:
			print(f"Error uninstalling Blender: {e}")

	else: print("Cancelled")

def uninstallOnWindow(version, blender_path, parent):
	pass

def uninstallOnMac(version, blender_path, parent):
	pass
