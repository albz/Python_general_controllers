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
from csg_basic_constants import *
### --- ###


#--- physical constants ---#
physical_const = codata.physical_constants #SI
# most common
electron_mass	 		= physical_const['electron mass'][0]
electron_charge 		= physical_const['elementary charge'][0]
proton_mass 			= physical_const['proton mass'][0]
boltzmann_constant_JK 	= physical_const['Boltzmann constant'][0]
boltzmann_constant_eVK 	= physical_const['Boltzmann constant in eV/K'][0]
eps0					= physical_const['electric constant'][0]
mu0						= physical_const['mag. constant'][0]
c						= physical_const['speed of light in vacuum'][0]
#--- *** ---#


### --- --- --- --- --- --- ###
#  All input are in SI Units  #
### --- --- --- --- --- --- ###

def coulomb_logarithm(Te,ne,Z):
	TeeV = Te*boltzmann_constant_eVK
	ne   = ne/1e6 #from m^-3 to cm^-3
	
	if TeeV >= 10.*Z**2:
		CL = 24.0 - 0.5*log(ne) + log(TeeV)
	else:
		CL = 23.0 - 0.5*log(ne) - log(Z) + 3./2.*log(TeeV)
		
	return CL



def plasma_frequency_electron(ne):
	return (ne * electron_charge**2 / electron_mass / eps0)

	
	
def plasma_wavenumber_electron(ne):
	return plasma_frequency_electron(ne)/c


	
def plasma_wavelength_electron(ne):
	return 2.*np.pi/plasma_wavenumber_electron(ne)


def electron_gyrofrequency(B):
	B_cgs=B/1e4
	return electron_charge_csg*B_cgs /c_cgs /electron_mass_cgs

def ion_gyrofrequency(B,Z,mu):
	B_cgs=B/1e4
	return Z*electron_charge_csg*B_cgs /c_cgs /(mu*proton_mass_cgs)



def electron_plasma_frequency(B):
	return electron_gyrofrequency(B) /2./np.pi
	
def ion_plasma_frequency(B):
	return ion_gyrofrequency(B,Z,A) /2./np.pi



def electron_collision_rate(ne,Te,Z):
	ne_cgs	= ne/1e6
	TeeV 	= Te*boltzmann_constant_eVK
	CL		= coulomb_logarithm(Te,ni,Z)
	return 2.91e-6 * ne_cgs * CL * TeeV**1.5 

def electron_thermal_velocity(Te):
	return np.sqrt(boltzmann_constant_ergK*Te/electron_mass_cgs)

def ion_thermal_velocity(Ti,mu):
	return np.sqrt(boltzmann_constant_ergK*Ti/mu/proton_mass_cgs)