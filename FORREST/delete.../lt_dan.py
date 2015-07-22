#!/usr/bin/python
######################################################################
# Name:         lt_dan
# Author:       A. Marocchino
# Date:			03-06-2010
# Purpose:      generates the list of files that still need to be run
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, sys, shutil
### --- ###

### shell inputs
if(len(sys.argv)<2):
	print "usage  : %s exec_path" % sys.argv[0]
	print "example: %s ~/Codes/ciao_belli.exe" % sys.argv[0]
	sys.exit()

exe=sys.argv[1]
path = os.getcwd()
sims_to_run_path = []

# create file if does not exist
if (os.path.exists(os.path.join(path, 'chocolate_box.txt')) == False):
	open(os.path.join(path, 'chocolate_box.txt'), 'w')

# open file to load existing paths (only the running dirs)
f = open(os.path.join(path, 'chocolate_box.txt'), 'r')
all = f.readlines()
for line in all:
	sims_to_run_path.append(line.split()[0])
	print '>>>',line.split()[0],' *** ',line.split()[1]
f.close()


# open file to append new files
f = open(os.path.join(path, 'chocolate_box.txt'), 'a')


#--- *** ---#
count = 0
for root_dir, sub_dirs, files in os.walk(path):
	for file in files:
		if file == 'dued.nml':
			if (os.path.exists(os.path.join(root_dir, "==running==")) == False) and (os.path.exists(os.path.join(root_dir, "==completed==")) == False): 
				for line in sims_to_run_path:
					count = 0
					if line.find(root_dir) == False:
						count = count+1
				if count == len(sims_to_run_path):
					f.write(root_dir)
					f.write("\t")
					f.write(exe)
					f.write("\n")
					
# closing file
f.close()