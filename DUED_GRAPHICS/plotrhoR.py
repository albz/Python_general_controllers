#!/usr/bin/python
######################################################################
# Name:         plotrhoR
# Author:       A. Marocchino
# Date:			15-01-2011
# Purpose:      plots: rhoR.dat VS time
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
### --- ###


if( len(sys.argv) == 1):
	#Path
	path = os.getcwd()
	
	#Load
	data = numpy.genfromtxt(os.path.join(path,'rhoR.dat'), unpack=True)
	time =  data[0,range(1,data.shape[1])]
	rhoR =  data[1,range(1,data.shape[1])]

	#Plot
	plot(time*1e9,rhoR)	
	xlabel('Time')
	ylabel('rhoR')
	title('../'+os.path.split(path)[1])
	grid(True)
	show()
	
else:
	map     = get_cmap('jet')
	for J in range(1,len(sys.argv)):
		#Path
		path = sys.argv[J]
		#Search & Load
		for files in glob.glob(os.path.join(path,'rhoR.dat')):
			rhoR_file = files
			print 'eccolo',rhoR_file
		#Load
		data = numpy.genfromtxt(rhoR_file, unpack=True)
		time =  data[0,range(1,data.shape[1])]
		rhoR =  data[1,range(1,data.shape[1])]
		#Plot
		plot(time*1e9,rhoR ,label=os.path.split(path)[1])	
	xlabel('Time')
	ylabel('rhoR')
	legend(loc="upper left")
	grid(True)
	show()

