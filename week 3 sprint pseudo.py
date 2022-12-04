# For this weeks sprint we are working with ngenuity to check the profiles so that each pc has consistent hyperx profiles
# credit to musfik for discovering shutil and filecmp to compare and replace existing files for hyperx profile settings.

import dependencies
import os
import shutil # this module can be used to copy files from the source to the destination
import filecmp # filecmp is a module that can be used to compare different files and give us the results of matches or mismatched files

dir1 = "C:/Users/VR/Desktop/Settings.db"
dir2 = "C:/Users/VR/AppData/Local/Packages/33C30B79.HyperXNGenuity_0a78dr3hq0pvt/LocalState/Settings/Settings.db" 
# here we are looking to compare the Settings.db from dir1 and dir2

match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common, shallow=False) # in this instance we are focusing on using mismatches and errors to do with the settings.db
# rather than using shallow mode, using deep comparison allows this function to give us much more information (compares content) helping us understand the relationsships between directories in more depth. 
# Shallow mode only compares the metadata of the files (size, date modified)

if mismatch =="settings.db" 
    shutil.copyfile('Settings.db', dir2)

else: print("The headphones have the correct profile running.")

*** ALTERNATIVE APPROACH ***

# Code below compares the two files line by line and outputs the differences within the files

# Open the files to be compared
# Loop through the files and compare each line of the two files.
# If lines are identical, output SAME on the output screen.
# Else, output the differing lines from both the files on the output screen.

# reading files
f1 = open("C:/Users/VR/Desktop/Settings.db", "r")
f2 = open("C:/Users/VR/AppData/Local/Packages/33C30B79.HyperXNGenuity_0a78dr3hq0pvt/LocalState/Settings/Settings.db", "r")

i = 0

for line1 in f1:
	i += 1
	
	for line2 in f2:
		
		# matching line1 from both files
		if line1 == line2:
			# print IDENTICAL if similar
			print("Line ", i, ": IDENTICAL")	
		else:
			print("Line ", i, ":")
			# else print that line from both files
			print("\tFile 1:", line1, end='')
			print("\tFile 2:", line2, end='')
		break

# closing files
f1.close()									
f2.close()			