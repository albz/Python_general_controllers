#!/usr/bin/python
######################################################################
# Name:         find_Gain_cresco
# Author:       A. Marocchino
# Date:			26-06-2013
# Purpose:      find maximum Gain for all subfolders - Cluster version for Cresco
# Source:       python
#####################################################################


### loading libraries
import re, os, os.path, glob, sys #, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string
# from scipy import *
# from numpy import *
# import matplotlib as plt
# from pylab import *
# - #

# find in > sim.out
def find_in_simout(path,string_to_search,strategy):
	f=[]
	for line in open(os.path.join(path,'sim.out'),"r"):
		if string_to_search in line:
		#if re.match("\s*"+re.escape(string_to_search)+"\s"+"\s*",line): #Exact Matching: much slower
			for t in line.split():
				try:
					f.append(float(t))
				except ValueError:
					pass
	if strategy == 'max':
		return max(f)
	if strategy == 'all':
		return f


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

