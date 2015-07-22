#!/usr/bin/python
######################################################################
# Name:         find_Gain
# Author:       A. Marocchino
# Date:			26-06-2013
# Purpose:      find maximum Gain for all subfolders
# Source:       python
#####################################################################


### loading libraries
import re, os, os.path, glob, sys #, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string
# from scipy import *
# from numpy import *
# import matplotlib as plt
# from pylab import *
# - #
###>>>
sys.path.append('/Users/gaps/Codes/Python_Programs/DUED/nml_manipulation')
###>>>
import rain_man
from rain_man import *
### --- ###

#utilities
index = 1

# path
path = os.getcwd()

#analyze sim.out --> results
print 'Directory','\t','Gain'
for root_dir, sub_dirs, files in os.walk(path):
	for file in files:
		if file == 'sim.out':
			print root_dir,'\t',find_in_simout(root_dir,'GAIN ','max')

