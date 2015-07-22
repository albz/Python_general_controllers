### Program for multiple DUED RUN using Python
### This Python script generates the subfolder and inserts
### the appropiate DUED.NML as requested 
### 
### A. Marocchino 21-05-2010
###


### loading shell commands
import numpy
import os
import write_nml
from numpy import *
from write_nml import *
### --- ###

### --- INPUT VALUES ---###
l         = 100
times_NI  = linspace(0.8,1.2,2)
times_NJ  = linspace(0.8,2.0,2)
C_Filter  = linspace(0.19,1.19,2)
###---


print "times_NI = ", times_NI
print "times_NJ = ", times_NJ
print "C_Filter = ", C_Filter




folder_counter = 0

for i in range(times_NI.shape[0]):
	for j in range(times_NJ.shape[0]):
		for k in range(C_Filter.shape[0]):
			name_folder = "%0.5d" %folder_counter
			actual_path = os.getcwd()
			path        = actual_path + "/" + name_folder
			if not os.path.exists(path):
				#print "this folder does not exists"
				os.makedirs(path)
			### writing DUED.NML
			write_nml(path, l, times_NI[i], times_NJ[j], C_Filter[k])
			folder_counter = folder_counter + 1
			
			
