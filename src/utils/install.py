from os import mkdir, path
from shutil import rmtree
from sys import platform
from subprocess import call, run, Popen, CalledProcessError
from PyQt5.QtWidgets import QDialog

from pages.dialogs.password import PasswordDialog
from globals import versions, CONFIG_USER_FOLDER

'''
TO-DO list:
 - Generate the config files folder when Blender had been installed.
'''

# Install methods
def installBlender(version, url, parent):
	if platform == "linux" or platform == "linux2": installOnLinux(version, url, parent)
	elif platform == "win32": installOnWindow(version, url, parent)
	elif platform == "darwin": installOnMac(version, url, parent)
	else: print("[Blender Hub] Apparently your OS is not supported. Please contact me and let's see what I can do to fix that.")

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
			run(["sudo", "-S", "mkdir", "-p", "temp"], input=password.encode(), check=True)

			# Create Blender directory for the first time
			if not path.isdir("/opt/blender"):
				run(["sudo", "mkdir", "/opt/blender"], check=True)
			
			# Download installation file if not exists
			if not path.isfile(f"temp/{blender_file}"):
				try:
					run(["sudo", "curl", "-o", f"temp/{blender_file}", url], check=True)
				except Exception as e:
					print(f"[Blender Hub] Error downloading .tar file: {e}")
			
			# Extract file content
			run(["tar", "-xf", f"temp/{blender_file}"], check=True)

			# Move content
			run(["sudo", "mv", blender_folder, "/opt/blender"], check=True)

			# Create alias (optional)
			# run(["sudo", "ln", "-s", f"/opt/blender/{blender_folder}/blender", "/usr/local/bin/blender"], check=True)

			# TO-DO: Generate the config files

			# Remove the temporal folder with the installation file
			run(["sudo", "rm", "-rf", "temp"], check=True)

			# Feedback message
			print(f"\n[Blender Hub] Blender {version} successfully installed.")
		
		except CalledProcessError as e:
			print(f"[Blender Hub] Failed to install Blender: {e}")

		except Exception as e:
			print(f"[Blender Hub] Failed to install Blender: {e}")

def installOnWindow(version, url, parent):
	# extension = ".msi"
	# blender_file = path.split(url)[-1].replace(extension)

	commands = []

def installOnMac(version, url, parent):
	# extension = ".dmg"
	# blender_file = path.split(url)[-1].replace(extension)

	commands = []

# Uninstall methods
def uninstallBlender(version, parent):
	# Get the path of the folder. It should look like "/opt/blender/blender-x.y.z".
	blender_path = versions.paths[version]

	if platform == "linux" or platform == "linux2": uninstallOnLinux(version, blender_path, parent)
	elif platform == "win32": uninstallOnWindow(version, blender_path, parent)
	elif platform == "darwin": uninstallOnMac(version, blender_path, parent)
	else: print("[Blender Hub] Apparently your OS is not supported. Please contact me and let's see what I can do to fix that.")

def uninstallOnLinux(version, blender_path, parent):
	password_dialog = PasswordDialog(version, parent)
	if password_dialog.exec_() == QDialog.Accepted:
		password = password_dialog.getPassword()
		
		try:
			# Remove the folder from /opt/blender
			if path.isdir(blender_path):
				run(["sudo", "-S", "rm", "-rf", blender_path], input=password.encode(), check=True)

			# Remove the folder from .config/blender
			#config_folder = path.join(CONFIG_USER_FOLDER, version[:-2])
			#if path.isdir(config_folder):
			#	run(f"sudo rm -rf {config_folder}".split(), check=True)

			# Feedback message
			print(f"\n[Blender Hub] Blender {version} successfully uninstalled.")

		except Exception as e:
			print(f"[Blender Hub] Error uninstalling Blender: {e}")

	else: print("[Blender Hub] Cancelled")

def uninstallOnWindow(version, blender_path, parent):
	pass

def uninstallOnMac(version, blender_path, parent):
	pass
