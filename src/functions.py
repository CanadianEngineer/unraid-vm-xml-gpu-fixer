import os

# Prompts user for file select
# Returns -1, 0, or a file
# return -1 = Failure, don't retry (ie. failed to find a file)
# Return 0 = Failure, retry (ie. Reprmpt the user)
# Return file
def prompt_file_select():
	# Find XML file
	files = []

	for (dirpath, dirnames, filenames) in os.walk('./'):
		for filename in filenames:
			if(filename[-4:] == '.xml'):
				files.extend([filename])
		break

	# Confirm XML file

	if(len(files) == 0):
		print("No XML files were found.")
		print("Please save your xml data to an xml file in the root directory")
		print("")
		return -1;

	elif(len(files) == 1):
		print("There was only 1 xml file found: \'{filename}\'".format(filename=files[0]))
		confirmSingleInput = input("Do you want to fix {filename}? [y/N] ".format(filename=files[0]))
		confirm = confirmSingleInput == 'Y' or confirmSingleInput == 'y'

		if(confirm):
			fileName = files[0]
			selectedFile = open(fileName);
			return selectedFile
		else:
			print("User rejected the XML file, and no other XML files were found.")
			return -1;
	else: # Multiple files
		print("There was more than 1 XML file found. Please select which file you want to fix.")
		for file_i in range(len(files)):
			fileName = files[file_i]
			print("{index}: {name}".format(index=file_i + 1, name=fileName))
		selectedFileInput = input("Select which file you want to fix: ");
		selectedFileName = files[int(selectedFileInput) - 1]
		selectedFile = open(selectedFileName)
		return selectedFile;
