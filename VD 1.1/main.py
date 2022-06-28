def main():
	#---------------Import modulů a pokus o instalaci modulu-------------
	print("\n" + 50*"-")
	print("\nStarting modules...")

	import os
	from time import sleep
	err = "\n\nThere was an error with finding a module. Trying to install.\n\n"
	try:
		from pytube import YouTube
	except ModuleNotFoundError:
		# Error handling
		print(err)
		sleep(1)
		print("Starting installation of pytube module...\n")
		sleep(1)
		os.system("pip install pytube")
		sleep(1)
		print("\nImporting module...")
		from pytube import YouTube
	#-------------------------------------------------------------------

	#----------------Kontrola souboru settings.txt----------------------

	print("\nChecking the settings file...\n")
	sleep(1)

	while True:
		settingsExist = os.path.isfile('settings.txt')
		if settingsExist == False:
			print("Settings file does not exist!")
			sleep(1)
			print("\nCreating a new one...\n")
			sleep(1)
			f = open('settings.txt', 'w', encoding='utf8')
			print("Writing basic settings to the file...\n")
			sleep(1)
			f.write("downloadDirName:'Downloaded Videos'\n# Only change the text in the quotes")
			f.close()
			print("Closing the file...\n")
			sleep(1)

		else:
			sleep(1)
			print("File - OK")
			f = open('settings.txt','r')
			break

	#-------------------------------------------------------------------

	r = f.readline()
	o = r.split("'")
	# print(o)

	baseDownloadDir = o.pop(1)

	#----------------Kontrola nastavené složky--------------------------

	print("\nChecking the base directory...\n")
	sleep(1)

	def mkDir():
		print('"' + baseDownloadDir + '"' + " directory does not exist!\n")
		sleep(1)
		print("Creating a new directory named: " + '"' + baseDownloadDir + '"')
		sleep(1)
		os.mkdir(baseDownloadDir)
		sleep(1)

	while True:

		sleep(1)

		dirExists = os.path.isdir(baseDownloadDir)
		if dirExists == False:
			while True:

				dirExists = os.path.isdir(baseDownloadDir)

				if dirExists == False:
					dirExists = os.path.isdir(baseDownloadDir)
					mkDir()
				else:
					print("\nFolder created successfully!")
					sleep(1)
					break
		else:
			sleep(1)
			print("Directory - OK")

		
	#--------------------------------------------------------------------
		sleep(1)
		print("\n" + 50*"-")
	#--------------------------Jádro programu----------------------------

		print("\nEverything is OK.\n\nStarting program\n")
		sleep(1)
		print(50*'-')

		link = input("Write / Paste YT Video Link Here: ")

		print("URL link set to: " + link)

		yt = YouTube(link)

		videoResolutionPrompt = input(50*'-' + "\n 6. 144p \n 5. 240p \n 4. 360p \n 3. 480p \n 2. 720p \n 1. 1080p (no sound nor video)\nWrite resolution number: ")
		print(50*'-') 

		if videoResolutionPrompt == '1':
			print("INFO - Output video or audio could not work!")
			videoResolution = '1080p'

		if videoResolutionPrompt == '2':
			videoResolution = '720p'

		if videoResolutionPrompt == '3':
			videoResolution = '480p'

		if videoResolutionPrompt == '4':
			videoResolution = '360p'

		if videoResolutionPrompt == '5':
			videoResolution = '240p'

		if videoResolutionPrompt == '6':
			videoResolution = '144p'
		
		print("Resolution set to: " + videoResolution)

		print("Starting the video download...\n")
		# Častá chyba u spouštění ve VS Code -> Používat tento příkaz: "python main.py" - protože tam je nainstalován modul pytube
		yt.streams.filter(progressive=True,file_extension='mp4', res=videoResolution).first().download(output_path=baseDownloadDir)
		print("Video downloaded!\n")

		getAnsw = None

		while getAnsw != "y":

			getAnsw = input("Continue? [Y/N]: ").lower()

			if getAnsw == "n":
				exit()

			if getAnsw == 'y':
				print("Refreshing...")
			
			else:
				print("Invalid input")

	#-------------------------------------------------------------------

if __name__ == '__main__':
	main()