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
index = 200

# path
path = os.getcwd()

#--- read namelist ---#
nml = read_nml(os.path.join(path,'0140'),'architect.nml')

#--- loop ---#
for current in np.arange(10.,101.,5.):

	nml = nml_substitution(nml,'Bpoloidal%background_current_A(1)',current)

 	path_complete = os.path.join(path,"%0.5d" % index)
 	if not os.path.exists(path_complete):
 		os.makedirs(path_complete)
 		write_nml(path_complete,nml,'architect.nml')
 	index = index + 1
