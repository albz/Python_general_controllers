#!/usr/bin/python
######################################################################
# Name:         run_forrest_run
# Author:       A. Marocchino
# Date:			2015-10-22
# Purpose:      count jpg files
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, sys, shutil, time, string
### --- ###


#Path
path = os.getcwd()

#Exclusion List
extension = ['.jpg','.JPG'];

count = 0
#Search and count
for root_dir, sub_dirs, files in os.walk(path):
	for file in files:
		if os.path.splitext(file)[1] in extension:
			count+=1
			
print 'jpg file:',count	
		
	
				