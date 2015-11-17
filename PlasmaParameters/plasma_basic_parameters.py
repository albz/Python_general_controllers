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
from scipy.constants import codata
# - #
home_path = os.path.expanduser('~')
sys.path.append(os.path.join(home_path,'/Codes/Python_general_controllers/PlasmaParameters'))
### --- ###


#--- physical constants ---#
physical_const = codata.physical_constants #SI
# most common
electron_mass	 		= physical_const['electron mass'][0]
electron_charge 		= physical_const['elementary charge'][0]
proton_mass_SI 			= physical_const['proton mass'][0]
boltzmann_constant_JK 	= physical_const['Boltzmann constant'][0]
boltzmann_constant_eVK 	= physical_const['Boltzmann constant in eV/K'][0]
eps0					= physical_const['electric constant'][0]
mu0						= physical_const['mag. constant'][0]
c						= physical_const['speed of light in vacuum'][0]
#--- *** ---#

def coulomb_logarithm(Te,ni,Z):
	TeeV = Te*boltzmann_constant_eVK
	ni   = ni/1e6 #from m^-3 to cm^-3
	
	if TeeV >= 10.*Z**2:
		CL = 24.0 - 0.5*log(ni) + log(TeeV)
	else:
		CL = 23.0 - 0.5*log(ni) - log(Z) + 3./2.*log(TeeV)

	return CL



def plasma_frequency_electron(ne):
	return (ne * electron_charge**2 / electron_mass / eps0)
	
	
def plasma_wavenumber_electron(ne):
	return plasma_frequency_electron(ne)/c

	
def plasma_wavelength_electron(ne):
	return 2.*np.pi/plasma_wavenumber_electron(ne)

