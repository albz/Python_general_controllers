# Date:			2012-12-21
# Purpose:      namelist easy manipulator for blast-wave simulations
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
### --- ###
###>>>
sys.path.append('/Users/alberto/Codes/Python_Programs/DUED/nml_manipulation')
###>>>
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

# Calculate Temperature from Energy-numberdensity-Volume
def El_from_temperature_n_focalspot(T,n,f):
	Vol = np.pi*f**2
	eps = 3.0/2.0*kb * (T*1.16e4) * n*Vol; #Energy per unit volume
	return eps


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
		



### --- ### Inputs
n = 9.2e17;  #number density [cm^-3]
Te_peak = 105e3; #Electron peak temperature [eV]
Ti_peak = 0.6897; #Ion peak temperature [eV]
f = 1.5e-3 #focal spot [cm]
Z = 1e-1;  #Plasma width [cm]
Material = 'Ar'; #Material used
### --- ###

rho = density_from_n_Material(n,Material)
eps_e = El_from_temperature_n_focalspot(Te_peak,18*n,f)
eps_i = El_from_temperature_n_focalspot(Ti_peak,   n,f)
eps = (eps_e+eps_i)*1e7 #in [erg]

print 'rho: %g [g/cm^-3]' % (rho)
print 'Energy per unit length: %g [erg/cm]' % (eps)
print 'Energy Density E/rho: %g' % (eps/rho)



### --- ### Input Deck2
n = 9.2e17;  #number density [cm^-3]
Te_peak = 350e3; #Electron peak temperature [eV]
Ti_peak = 0.6897; #Ion peak temperature [eV]
f = np.sqrt(2)*1.5E-3*.385 #focal spot [cm]
Z = 1e-1;  #Plasma width [cm]
Material = 'Ar'; #Material used
### --- ###

rho = density_from_n_Material(n,Material)
eps_e = El_from_temperature_n_focalspot(Te_peak,18*n,f)
eps_i = El_from_temperature_n_focalspot(Ti_peak,   n,f)
eps = (eps_e+eps_i)*1e7 #in [erg]

print 'rho: %g [g/cm^-3]' % (rho)
print 'Energy per unit length: %g [erg/cm]' % (eps)
print 'Energy Density E/rho: %g' % (eps/rho)

