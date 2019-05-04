#This is a simple script made for both private and business users that adopt Enpass Password Manager.
#It is created to allow users to sync their password database between multiple Cloud services.
#In particular it makes it easy to sync an Enpass database between iOS/macOS and Windows devices.
#It works with every version of Enpass below V6. Starting from V6, iCloud is supported by default on each platform.
#Many users, especially the business ones, are not able to upgrade to Enpass V6 for various reasons.
#This script could be of help to all of them.
#It is written in Python, hence I recommend to use it on a desktop environment.
#Tested on Windows 10, Ubuntu 18.04 and macOS 10.14. However it is meant for a Windows environment, of course.

import os
import shutil

print("\nWelcome Windows user!")

from os import path


def main():
	# Let's make a duplicate of an existing file.
	if path.exists("C:/Users/User/Documents/Enpass/walletx.db/"):	#Here you can set your own path.

		# Get the path to the file in the current directory.
		src = path.realpath("C:/Users/User/Documents/Enpass/walletx.db/");	#Here you can set your own path.

		# Seperate the path from the filter.
		head, tail = path.split("C:/Users/User/Documents/Enpass/walletx.db/")	#Here you can set your own path.
		print("Path:" + head)
		print("File:" + tail)

		# Let's make a backup copy by appending "bak" to the name.
		dst = src + ".bak"

		# Now use the shell to make a copy of the file.
		shutil.copy2("C:/Users/User/Documents/Enpass/walletx.db/",
					 "C:/Users/User/iCloud Drive/Enpass/walletx.db/") #Here you can set your own paths.

		# We also want to copy over the permissions,modification.
		shutil.copystat("C:/Users/User/Documents/Enpass/walletx.db/",
						"C:/Users/User/iCloud Drive/Enpass/walletx.db/")	#Here you can set your own paths.

		print("\nYour Enpass database has been successfully copied. Bye!")

	else:
		print("\nNo database found here! Try to check the code and modify the paths in the script :)")


if __name__ == "__main__":
	main()
