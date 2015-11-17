#!/usr/bin/python
######################################################################
# Name:         PlasmaParameters
# Author:       A. Marocchino
# Date:			2015-11-17
# Purpose:      series of python function to calculate basic plasma paramteres
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil, time
import numpy as np
import scipy as scy
import pylab as pyl
# - #
home_path = os.path.expanduser('~')
sys.path.append(os.path.join(home_path,'/Codes/Python_general_controllers/PlasmaParameters'))
from phy_constants import *
### --- ###


def coulomb_logarithm(Te,ni,Z):
	TeeV = Te*boltzmann_constant_eVK
	ni   = ni/1e6 #from m^-3 to cm^-3
	
	if TeeV >= 10.*Z**2:
		CL = 24.0 - 0.5*log(ni) + log(TeeV)
	else:
		CL = 23.0 - 0.5*log(ni) - log(Z) + 3./2.*log(TeeV)

	return CL



def plasma_frequency_electron(ne):
	ne = ne/1e6 #from m^-3 to cm^-3
	return ( 4.*np.pi* ne *electron_charge_cgs**2 / electron_mass_cgs )**(1./2.)
	
	
def plasma_wavenumber_electron(ne):
	return plasma_frequency_electron(ne/1e6)/c_cgs

	
def plasma_wavelength_electron(ne):
	return 2.*np.pi/plasma_wavenumber_electron(ne/1e6)

