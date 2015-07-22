#!/usr/bin/python
######################################################################
# Name:         master and commander
# Author:       A. Marocchino
# Date:			2015-06-20
# Purpose:      nml manupulation for Architect
# Source:       python
#####################################################################

### loading libraries
import re, os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string, rain_man, math
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
from rain_man import *
### --- ###

#utilities
index = 0

# path
path = os.getcwd()

#--- read namelist ---#
nml = read_nml(path,'datain.inp')

#--- loop ---#
index=1
for charge in range(30,51,5):

	nml = nml_substitution(nml,'sim_parameters%ChargeB(2)',charge)

	nml = nml_substitution(nml,'bunch_initialization%n_total_bunches',2)
	nml = nml_substitution(nml,'bunch_initialization%n_particles(2)',100000)
	nml = nml_substitution(nml,'sim_parameters%db(1)',0.5)
	nml = nml_substitution(nml,'bunch_initialization%bunch_s_x(2)',2.45)
	nml = nml_substitution(nml,'bunch_initialization%bunch_s_y(2)',2.45)
	nml = nml_substitution(nml,'bunch_initialization%bunch_s_z(2)',10.)
	nml = nml_substitution(nml,'bunch_initialization%bunch_gamma_m(2)',200.)
	nml = nml_substitution(nml,'bunch_initialization%bunch_eps_x(2)',1.)
	nml = nml_substitution(nml,'bunch_initialization%bunch_eps_y(2)',1.)

 	path_complete = os.path.join(path,"%0.5d" % index)
 	if not os.path.exists(path_complete):
 		os.makedirs(path_complete)
 		write_nml(path_complete,nml,'datain.inp')
 	index = index + 1
	
	
	
#modifying spike timing
# for i in linspace(2.69400e-08,3.09400e-08,60):
# 	nml = nml_substitution(nml,'coet_2(2)',i)
# 	nml = nml_substitution(nml,'coet_2(3)',i + 5.35e-10)
# 	nml = nml_substitution(nml,'coet_2(4)',i + 5.35e-10 + 8.02e-10)
# 	nml = nml_substitution(nml,'coet_2(5)',i + 2.0*5.35e-10 + 8.02e-10)
# 	
# 	path_complete = os.path.join(path,"%0.5d" % index)
# 	if not os.path.exists(path_complete):
# 		os.makedirs(path_complete)
# 		write_nml(path_complete,nml)
# 	index = index + 1

#modifying spike-power & plateau-power
# for plateau in linspace(25.0,85.0,7):        #Plateau
# 	for spike in linspace(0.0,800.0,9):    #Spike
# 		
# 		time = -6.538329e-1*(plateau**(0.41e0)) + 5.0000e-4*spike + 1.4091937e1
# 		time = time * 1e-9
# 		print index,' > ',plateau,spike,time
# 			
# 		nml = read_nml(path)
# 		
# 		tend = 13.5e-9
# 		nml = nml_substitution(nml,'TMAX',tend)
# 		nml = nml_substitution(nml,'TPULSE',tend+1e-10)
# 		nml = nml_substitution(nml,'COET(15)',tend+2e-10)
# 		nml = nml_substitution(nml,'tpulse_2',tend+1e-10)
# 		nml = nml_substitution(nml,'coet_2(6)',tend+2e-10)
# 			
# 		nml = nml_substitution(nml,'COEW(11)',plateau)
# 		nml = nml_substitution(nml,'COEW(12)',plateau)
# 		nml = nml_substitution(nml,'coew_2(3)',spike)
# 		nml = nml_substitution(nml,'coew_2(4)',spike)
# 		
# 		nml = nml_substitution(nml,'coet_2(2)',time)
# 		nml = nml_substitution(nml,'coet_2(3)',time + 0.2e-9)
# 		nml = nml_substitution(nml,'coet_2(4)',time + 0.5e-9)
# 		nml = nml_substitution(nml,'coet_2(5)',time + 0.7e-9)
# 		
# 		path_complete = os.path.join(path,"%0.5d" % index)
# 		if not os.path.exists(path_complete):
# 			os.makedirs(path_complete)
# 			write_nml(path_complete,nml)
# 		index = index + 1
	
# time optimization plateau = 35 TW
# for plateau in linspace(40.0,40.0,1):        #Plateau
#  	for spike in linspace(0.0,800.0,9):    #Spike
#  		
#  		time = -6.538329e-1*(plateau**(0.41e0)) + 5.0000e-4*spike + 1.4091937e1
#  		time = time * 1e-9
#  		
#  		for optimized_time in linspace(time-350e-12,time+350e-12,16):
#  			print index,' > ',plateau,spike,time,optimized_time
#  			
#  			nml = read_nml(path)
#  		
#  			tend = 13.5e-9
#  			nml = nml_substitution(nml,'TMAX',tend)
#  			nml = nml_substitution(nml,'TPULSE',tend+1e-10)
#  			nml = nml_substitution(nml,'COET(15)',tend+2e-10)
#  			nml = nml_substitution(nml,'tpulse_2',tend+1e-10)
#  			nml = nml_substitution(nml,'coet_2(6)',tend+2e-10)
#  			
#  			nml = nml_substitution(nml,'COEW(11)',plateau)
#  			nml = nml_substitution(nml,'COEW(12)',plateau)
#  			nml = nml_substitution(nml,'coew_2(3)',spike)
#  			nml = nml_substitution(nml,'coew_2(4)',spike)
#  		
#  			nml = nml_substitution(nml,'coet_2(2)',optimized_time)
#  			nml = nml_substitution(nml,'coet_2(3)',optimized_time + 0.2e-9)
#  			nml = nml_substitution(nml,'coet_2(4)',optimized_time + 0.5e-9)
#  			nml = nml_substitution(nml,'coet_2(5)',optimized_time + 0.7e-9)
#  		
#  			path_complete = os.path.join(path,"%0.5d" % index)
#  			if not os.path.exists(path_complete):
#  				os.makedirs(path_complete)
#  				write_nml(path_complete,nml)
#  			index = index + 1


#dense scan
# v = concatenate((arange(0.0,80.0,1.0),arange(80.0,91.0,2.5)))
# w = concatenate((arange(0.0,401.0,1.0),arange(400.0,800.0,10.0)))
# 
# for plateau in v:        #Plateau
#  	for spike in w:      #Spike
# 		
# 		index=index+1
# 		print index
# 		
#  		time = -6.538329e-1*(plateau**(0.41e0)) + 5.0000e-4*spike + 1.4091937e1
#  		time = time * 1e-9
#  		
#  		for optimized_time in linspace(time-350e-12,time+350e-12,16):
#  			print index,' > ',plateau,spike,time,optimized_time
#  			
#  			nml = read_nml(path)
#  		
#  			tend = 13.5e-9
#  			nml = nml_substitution(nml,'TMAX',tend)
#  			nml = nml_substitution(nml,'TPULSE',tend+1e-10)
#  			nml = nml_substitution(nml,'COET(15)',tend+2e-10)
#  			nml = nml_substitution(nml,'tpulse_2',tend+1e-10)
#  			nml = nml_substitution(nml,'coet_2(6)',tend+2e-10)
#  			
#  			nml = nml_substitution(nml,'COEW(11)',plateau)
#  			nml = nml_substitution(nml,'COEW(12)',plateau)
#  			nml = nml_substitution(nml,'coew_2(3)',spike)
#  			nml = nml_substitution(nml,'coew_2(4)',spike)
#  		
#  			nml = nml_substitution(nml,'coet_2(2)',optimized_time)
#  			nml = nml_substitution(nml,'coet_2(3)',optimized_time + 0.2e-9)
#  			nml = nml_substitution(nml,'coet_2(4)',optimized_time + 0.5e-9)
#  			nml = nml_substitution(nml,'coet_2(5)',optimized_time + 0.7e-9)
#  		
#  			path_complete = os.path.join(path,"%0.5d" % index)
#  			if not os.path.exists(path_complete):
#  				os.makedirs(path_complete)
#  				write_nml(path_complete,nml)
#  			index = index + 1



# dense scan - resolving gradients
# plateau_vector = arange(25.0,90.1,2.5)
# spike_vector   = arange(0.0,800.1,20.0)
# for plateau in plateau_vector:        #Plateau
#  	for spike in spike_vector:          #Spike
#  		
#  		time = -6.538329e-1*(plateau**(0.41e0)) + 5.0000e-4*spike + 1.4091937e1
#  		time = time * 1e-9
#  		
# 		print index,' > ',plateau,spike,time
#  			
# 		nml = read_nml(path)
#  		
# 		tend = 13.5e-9
# 		nml = nml_substitution(nml,'TMAX',tend)
# 		nml = nml_substitution(nml,'TPULSE',tend+1e-10)
# 		nml = nml_substitution(nml,'COET(15)',tend+2e-10)
# 		nml = nml_substitution(nml,'tpulse_2',tend+1e-10)
# 		nml = nml_substitution(nml,'coet_2(6)',tend+2e-10)
#  			
#  		nml = nml_substitution(nml,'COEW(11)',plateau)
#  		nml = nml_substitution(nml,'COEW(12)',plateau)
#  		nml = nml_substitution(nml,'coew_2(3)',spike)
#  		nml = nml_substitution(nml,'coew_2(4)',spike)
#  		
#  		nml = nml_substitution(nml,'coet_2(2)',time)
#  		nml = nml_substitution(nml,'coet_2(3)',time + 0.2e-9)
#  		nml = nml_substitution(nml,'coet_2(4)',time + 0.5e-9)
#  		nml = nml_substitution(nml,'coet_2(5)',time + 0.7e-9)
#  		
#  		path_complete = os.path.join(path,"%0.5d" % index)
#  		if not os.path.exists(path_complete):
#  			os.makedirs(path_complete)
#  			write_nml(path_complete,nml)
#  		index = index + 1



# time optimization gradient area
# for plateau in linspace(45.0,85.0,17):        #Plateau
# 	r     = -7.5*plateau + 737.5
# 	punti = math.floor(-0.4*plateau+38)
# 	#print plateau,r,punti
#  	for spike in linspace(0.0,r,punti):          #Spike
#  		
#  		time = -6.538329e-1*(plateau**(0.41e0)) + 5.0000e-4*spike + 1.4091937e1
#  		time = time * 1e-9
#  		
# 		print index,' > ',plateau,spike,time,punti
#  			
# 		nml = read_nml(path)
#  		
# 		tend = 13.5e-9
# 		nml = nml_substitution(nml,'TMAX',tend)
# 		nml = nml_substitution(nml,'TPULSE',tend+1e-10)
# 		nml = nml_substitution(nml,'COET(15)',tend+2e-10)
# 		nml = nml_substitution(nml,'tpulse_2',tend+1e-10)
# 		nml = nml_substitution(nml,'coet_2(6)',tend+2e-10)
#  			
#  		nml = nml_substitution(nml,'COEW(11)',plateau)
#  		nml = nml_substitution(nml,'COEW(12)',plateau)
#  		nml = nml_substitution(nml,'coew_2(3)',spike)
#  		nml = nml_substitution(nml,'coew_2(4)',spike)
#  		
#  		nml = nml_substitution(nml,'coet_2(2)',time)
#  		nml = nml_substitution(nml,'coet_2(3)',time + 0.2e-9)
#  		nml = nml_substitution(nml,'coet_2(4)',time + 0.5e-9)
#  		nml = nml_substitution(nml,'coet_2(5)',time + 0.7e-9)
#  		
#  		path_complete = os.path.join(path,"%0.5d" % index)
#  		if not os.path.exists(path_complete):
#  			os.makedirs(path_complete)
#  			write_nml(path_complete,nml)
#  		index = index + 1

	
# for i in range(5,85,10):
# 	nml = nml_substitution(nml,'ngfp(1)',i)
# 	
# 	path_complete = os.path.join(path,"%0.5d" % index)
# 	if not os.path.exists(path_complete):
# 		os.makedirs(path_complete)
# 		write_nml(path_complete,nml)
# 	index = index + 1


#analyze sim.out
# A=[]
# for root_dir, sub_dirs, files in os.walk(path):
# 	for file in files:
# 		#if file == 'sim.out' or file == 'dued.nml':
# 		if file == 'sim.out':
# 			plateau = str(find_in_nml(root_dir,'COEW(11)'))
# 			spike   = str(find_in_nml(root_dir,'coew_2(3)'))
# 			time    = str(find_in_nml(root_dir,'coet_2(2)'))
# 			Gain    = str(find_in_simout(root_dir,'GAIN ','max'))
# 			print '> ',plateau,spike,time,Gain
# 			A.append(plateau +'\t'+ spike +'\t'+ time +'\t'+ Gain + '\n')
# 
# if os.path.exists(os.path.join(path,'solution.dat')):
# 	os.remove(os.path.join(path,'solution.dat'))
# file = open(os.path.join(path,'solution.dat'),"w")
# for line in A:
#  	file.writelines(line)
# file.close()