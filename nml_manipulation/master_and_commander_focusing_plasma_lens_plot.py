#!/usr/bin/python
######################################################################
# Name:         master and commander
# Author:       A. Marocchino
# Date:			2015-06-20
# Purpose:      nml manupulation for Architect
# Source:       python
#####################################################################

### loading libraries
import re, os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string, math
import numpy as np
import scipy as scp
import pylab as plb
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
home_path = os.path.expanduser('~')
print home_path
sys.path.append(os.path.join(home_path,'Codes/Python_general_controllers/nml_manipulation'))
###>>>
from rain_man import *
### --- ###

#utilities
current=[]; sigma=[]

#--- path ---#
path = os.getcwd()

#analyze sim.out --> results
for root_dir, sub_dirs, files in os.walk(path):
	for file in files:
		if file == 'architect.nml':
			current.append( find_in_file(root_dir,file,'Bpoloidal%background_current_A(1)','max') )
		if file == 'bunch_integrated_quantity_1.dat':
			sigma.append( np.loadtxt(os.path.join(root_dir,'bunch_integrated_quantity_1.dat'))[-1,7] )
print current
print sigma

