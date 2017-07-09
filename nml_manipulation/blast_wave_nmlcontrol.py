#!/usr/bin/python
######################################################################
# Name:         bast_wave_nmlcontrol
# Author:       A. Marocchino
# Date:			2017-07-08
# Purpose:      namelist easy manipulator for blast-wave simulations
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, shutil, time, sys
import numpy as np
### --- ###
sys.path.append(os.path.join(os.path.expanduser('~'),'Codes/Python_general_controllers/nml_manipulation'))
from rain_man import *
### --- ###

#Path
path = os.getcwd()

#Constants
kb = 1.3806488e-23;   #Boltzmann constant [J/k]
u  = 1.660538921e-24; #atomic mass unit [g]


# Calculate Temperature from Energy-numberdensity-Volume
def temperature_from_E_n_Vol(E,n,Vol):
	eps = E / Vol; #Energy per unit volume
	T   = eps / 3.0 / kb / n; #Temperature in [k]
	return T



# Calculate Density from numberdensity-Material
def density_from_n_Material(n,Material):
	if Material == 'H':
		return n*1.00794*u #[g/cm^3]
	if Material == 'He':
		return n*4.002602*u #[g/cm^3]
	if Material == 'Ar':
		return n*39.948*u #[g/cm^3]
	if Material == 'Xe':
		return n*131.29*u #[g/cm^3]


### --- namelist manipulation --- ###
nml = read_nml(path,'dued_original.nml')
index = 0

for peak_temperature in np.arange(0.1e3,2.1e3,0.1e3): #peak temperature in eV
	nml = nml_substitution(nml,	'delta_T00', peak_temperature*1.16e4)
	print(peak_temperature)

	#write nml
	path_complete = os.path.join(path,"%0.5d" % index)
	if not os.path.exists(path_complete):
		os.makedirs(path_complete)
		write_nml(path_complete,nml,'dued.nml')
	index = index + 1



### --- ### Some Standard Inputs [cgs] more or less...
# n = 4e19;  #number density [cm^-3]
# E = 15;    #Total input energy [J]
# Z = 1e-1;  #Plasma width [cm]
# R = 20e-4; #Plasma radius [cm]
# Radiation_Transport = False; #Radiation Transport ON-OFF
# Radiation_Loss      = False; #Radiation Loss ON-OFF
# Thermal_Conduction  = False; #Thermal Conduction ON-OFF
# Material = 'H'; #Material used
# #
# zero_counter = 200; #first folder where to print new namelist
# ### --- ###
#
# #read namelist
# nml = read_nml(path)
#
# index = zero_counter
# for i in range(0,1):
# 	nml    = nml_substitution(nml,	'stub',	('BW_%0.5d' % (index)) )
#
# 	nml    = nml_substitution(nml,	'T00(1,1)',	temperature_from_E_n_Vol(E,n,Z*R*R*numpy.pi) )
# 	nml    = nml_substitution(nml,	'T00(2,1)',	temperature_from_E_n_Vol(E,n,Z*R*R*numpy.pi) )
#
# 	nml    = nml_substitution(nml,	'RO00(1,1)', density_from_n_Material(n,Material) )
# 	nml    = nml_substitution(nml,	'RO00(1,1)', density_from_n_Material(n,Material) )
#
# 	if Radiation_Loss == True:
# 		nml    = nml_substitution(nml,	'RADLOS', '.T.' )
# 	else:
# 		nml    = nml_substitution(nml,	'RADLOS', '.F.' )
#
# 	if Radiation_Transport == True:
# 		nml    = nml_substitution(nml,	'LMULTG', '.T.' )
# 	else:
# 		nml    = nml_substitution(nml,	'LMULTG', '.F.' )
#
# 	if Thermal_Conduction == True:
# 		nml    = nml_substitution(nml,	'THC', '.T.' )
# 	else:
# 		nml    = nml_substitution(nml,	'THC', '.F.' )
#
#
#
#
# 	nml    = nml_substitution(nml,	'c1', '  simulation number: %0.5i' % (zero_counter) )
# 	nml    = nml_substitution(nml,	'c2', '  n: %g [cm^-3]; Etot: %g [J];' % (n,E) )
# 	nml    = nml_substitution(nml,	'c3', '  Radiation Transport: %d; Radiation Loss: %d;' % (Radiation_Transport,Radiation_Loss) )
# 	nml    = nml_substitution(nml,	'c4', '  material: %s' % (Material) )
#
#
#
# 	#write nml
# 	path_complete = os.path.join(path,"%0.5d" % index)
# 	if not os.path.exists(path_complete):
# 		os.makedirs(path_complete)
# 		write_nml(path_complete,nml)
# 	index = index + 1
