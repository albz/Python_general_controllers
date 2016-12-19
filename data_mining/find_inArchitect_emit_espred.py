#!/usr/bin/python
######################################################################
# Name:         find_inArchitect_emit_espred.py
# Author:        A. Marocchino
# Date:			  2016-12-14
# Purpose:     find for a series of systematic scan performed with Architect the final emittance and Energy Spread
# Source:       python
#####################################################################

### loading shell commands
import re, os, os.path, glob, sys
import numpy as np
sys.path.append(os.path.join(os.path.expanduser('~'),'Codes/Python_general_controllers/nml_manipulation'))
from rain_man import *
###>>>

# --- *** ---#
sz = np.arange(30.,81.,5.)
sx = np.append(2,np.arange(4.,64.,4.))
emittance = np.zeros((sx.shape[0],sz.shape[0]))
espread = np.zeros((sx.shape[0],sz.shape[0]))

# --- *** ---#
path = os.getcwd()
for root_dir, sub_dirs, files in os.walk(path):
    for file in files:
        if file == 'architect.nml':
            print 'analysing ::',root_dir
            nml_sz = find_in_nml(root_dir,'bunch_initialization%bunch_s_z(1)','architect.nml')
            nml_sx = find_in_nml(root_dir,'bunch_initialization%bunch_s_x(1)','architect.nml')
            bunch = np.loadtxt(os.path.join(root_dir,'out','integrated_diagnostics','bunch_integrated_quantity_2.dat'))

            pos_sx=np.argmin(np.abs(sx-nml_sx))
            pos_sz=np.argmin(np.abs(sz-nml_sz))

            emittance[pos_sx,pos_sz]=bunch[-1,13]
            espread[pos_sx,pos_sz]=bunch[-1,16]

np.savetxt(sz,'sz.dat')
np.savetxt(sx,'sx.dat')
np.savetxt(emittance,'emittance.dat')
np.savetxt(espread,'espread.dat')
