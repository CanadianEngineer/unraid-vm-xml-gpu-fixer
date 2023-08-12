import os
import xml.etree.ElementTree as ET

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

def fix_file(xmlFile):
	# Read XML File
	print("\nFixing File \'{file}\'".format(file=xmlFile.name))

	tree = ET.parse(xmlFile.name)
	root = tree.getroot()

	hostdevElements = root.findall('./devices/hostdev')

	gpuElement = None;

	# Finding GPU element (element that has a ROM)
	for hostdevElement in hostdevElements:
		roms = hostdevElement.findall('rom')
		if(len(roms) > 0):
			gpuElement = hostdevElement

	gpuSourceAddress = gpuElement.find('./source/address')
	gpuGuestAddress = gpuElement.find('./address')

	# Finding sound device
	gpuSoundElement = None;
	for hostdevElement in hostdevElements:
		sourceAddress = hostdevElement.find('./source/address')
		if(sourceAddress != None):
			if(
				sourceAddress.attrib['domain'] == gpuSourceAddress.attrib['domain']
				and sourceAddress.attrib['bus'] == gpuSourceAddress.attrib['bus']
				and sourceAddress.attrib['slot'] == gpuSourceAddress.attrib['slot']
				and sourceAddress.attrib['function'] != gpuSourceAddress.attrib['function']
			):
				gpuSoundElement = hostdevElement
				gpuSoundSourceAddress = gpuSoundElement.find('./source/address')
				gpuSoundGuestAddress = gpuSoundElement.find('./address')

	# NOTE: Usually the sound device in Unraid is setup as a second device
	# This change makes it on the same device, but separate function

	gpuElement.set('multifunction', 'on')
	gpuSoundElement.set('multifunction', 'on')

	# Bus and Slot should match
	gpuSoundGuestAddress.set('bus', gpuGuestAddress.attrib['bus'])
	gpuSoundGuestAddress.set('slot', gpuGuestAddress.attrib['slot'])

	# Function should take on the same value as the source address
	gpuSoundGuestAddress.set('function', gpuSoundSourceAddress.attrib['function'])

	outputFileName = "{origFileName}-edited.xml".format(origFileName=xmlFile.name[:-4])
	print("Saving changes to '{outputFileName}'".format(outputFileName=outputFileName))
	tree.write(outputFileName)
