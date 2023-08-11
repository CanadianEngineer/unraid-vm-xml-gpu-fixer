import os
import json
import xml.etree.ElementTree as ET

from functions import *

os.system('clear') # Clearing the terminal screen

# Loading config from package.json
with open('package.json') as packageJsonFile:
	packageJson = json.load(packageJsonFile);

# Printing title

print(packageJson['name'])
print(packageJson['author'])
print("-" * len(packageJson['name']))

selectedFile = False;
while(selectedFile == False):
	selectedFile = prompt_file_select();
	if(selectedFile == -1):
		exit(1) # Exit 1 => stop console running
	print(selectedFile)

# Parse file

# Confirm adjustments

# Save adjustments to new file

print("\nDone!\n")
exit(0) # Exit 0 => End script successfully