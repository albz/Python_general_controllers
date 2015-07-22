#!/usr/bin/python
######################################################################
# Name:         nml_quick_change
# Author:       A. Marocchino
# Date:			01-07-2013
# Purpose:      substiture (recursively in the subdirectories) a single nml entry
# Source:       python
#####################################################################


### loading libraries
import re, os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string, rain_man
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
# - #
from rain_man import *
### --- ###


#- shell inputs
if(len(sys.argv)<2):
	print 'not enought input arguments'
	print '#1 -> nml entry'
	print '#2 -> set value'
	sys.exit()
	
nml_entry = str(sys.argv[1])
tochange  = sys.argv[2]
try:
	tochange = int(tochange)
except:
	try:
		tochange = float(tochange)
	except:
		tochange = str(tochange)


# path
path = os.getcwd()



#--- *** ---# prune not necessary sub dirs
def prune_dirs(dirs):
	if 'out' in dirs:
		dirs.remove('out')
	if 'dump' in dirs:
		dirs.remove('dump')



#os.walk and change
for root_dir, sub_dirs, files in os.walk(path):
	prune_dirs(sub_dirs)
	if 'dued.nml' in files:
		print 'changing nml @:',root_dir
		nml = read_nml(root_dir,'dued.nml')
		nml = nml_substitution(nml,nml_entry,tochange)
		write_nml(root_dir,nml)
