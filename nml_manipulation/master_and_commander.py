#!/usr/bin/python
######################################################################
# Name:         master_and_commander.py
# Author:       A. Marocchino
# Date:			2011-12-13
# Purpose:      rain_man control file
# Source:       python
#####################################################################

### loading libraries
import re, os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string, rain_man
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
# - #
###>>>
home_path = os.path.expanduser('~')
print home_path
sys.path.append(os.path.join(home_path,'Codes/Python_Programs/DUED/nml_manipulation'))
###>>>
from rain_man import *
### --- ###

#utilities
index = 0

# path
path = os.getcwd()

#read namelist
nml = read_nml(path)



###-> Target "s"-caling 
string = 'stub'
nml    = nml_substitution_str(nml,	string,	'simulazione_001')
string = 'DTWRIT'
nml    = nml_substitution(nml,	string,	find_in_nml(path,string) * tau)
string = 'TMAX'
nml    = nml_substitution(nml,	string,	find_in_nml(path,string) * tau)




#modifying spike timing
for i in linspace(2.84000e-08,2.96000e-08,24):
	nml = nml_substitution(nml,'coet_2(2)',i)
	nml = nml_substitution(nml,'coet_2(3)',i + 5.35e-10)
	nml = nml_substitution(nml,'coet_2(4)',i + 5.35e-10 + 8.02e-10)
	nml = nml_substitution(nml,'coet_2(5)',i + 2.0*5.35e-10 + 8.02e-10)
	nml = nml_substitution(nml,'coew_2(3)',444.372e0 * 1.1e0)
	nml = nml_substitution(nml,'coew_2(4)',444.372e0 * 1.1e0)
	
	path_complete = os.path.join(path,"%0.5d" % index)
	if not os.path.exists(path_complete):
		os.makedirs(path_complete)
		write_nml(path_complete,nml)
	index = index + 1
	
	
# for i in range(5,85,10):
# 	nml = nml_substitution(nml,'ngfp(1)',i)
# 	
# 	path_complete = os.path.join(path,"%0.5d" % index)
# 	if not os.path.exists(path_complete):
# 		os.makedirs(path_complete)
# 		write_nml(path_complete,nml)
# 	index = index + 1


#analyze sim.out
# for root_dir, sub_dirs, files in os.walk(path):
# 	for file in files:
# 		if file == 'sim.out':
# 			print root_dir,find_in_simout(root_dir,'GAIN ','max')

