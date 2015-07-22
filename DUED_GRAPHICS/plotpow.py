#!/usr/bin/python
######################################################################
# Name:         plotpow
# Author:       A. Marocchino
# Date:			10-01-2011
# Purpose:      sobstitute the old plotmtv *cpu, Simulation time VS CPU time
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, csv, getopt
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
### --- ###


#shell inputs
plot_log               = False
inputs_count           = 1
display                = 0
print sys.argv
if '-0' in sys.argv:
	display = 0
	inputs_count += 1
if '-1' in sys.argv:
	display = 1
	inputs_count += 1
if '-2' in sys.argv:
	display = 2
	inputs_count += 1
if '-3' in sys.argv:
	display = 3
	inputs_count += 1
if '-l' in sys.argv:
	plot_log = True
	inputs_count += 1
	
directories_to_analyze = sys.argv[inputs_count:]
if len(directories_to_analyze) < 1:
	directories_to_analyze = ['.']	
	
print "display >>> ",display
print "Directories to analyze: >",directories_to_analyze

#Path
path = os.getcwd()


#---graphics output begins here---#
N_plots = len(directories_to_analyze)
map     = get_cmap('jet')
legenda = ['tlapot', 'laser-energy', 'ene-absorbed', 'powrde', 'powrdi', 'pdvdta', 'radpot']
for J in range(0,N_plots):

	for files in glob.glob(os.path.join(directories_to_analyze[J],"pow")):
		pow_file = files
		print pow_file
		f = open(os.path.join(path,pow_file))

	#Read & Close
	read = f.readlines()
	f.close()
	del read[0:5] #Remove Headers

	#Matrix Initialization
	row       = read[0]
	dim_row   = len(row.split())
	dim_line  = len(read)
	print "dimension data matrix",dim_row,dim_line
	data      = zeros( (dim_row,dim_line) )

	#Matrix filling
	for i in range(0,dim_line):
		row       = read[i]
		splitted  = row.split()
		for j in range(0,dim_row):
			data[j,i] = double(splitted[j])
			
	###---> 1 <---### Laser profile
	if display==0 or display==1:
		figure(1)
		i = 2
		
		if plot_log == False:
			plot(data[0,range(1,data.shape[1])]*1e9,data[i,range(1,data.shape[1])]/1e19, color=map(1./(J+1)), lw=2.0, label=str([legenda[1],os.path.split(directories_to_analyze[J])[1]]) )
		if plot_log == True:
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[i,range(1,data.shape[1])]/1e19, color=map(1./(J+1)), lw=2.0, label=str([legenda[1],os.path.split(directories_to_analyze[J])[1]]) )
		
		xlabel('Time (ns)')
		legend(loc="best")
		grid(True)
			
	###---> 2 <---### Laser profile + Energy absorbed
	if display==0 or display==2:
		figure(2)

		if plot_log == False:
			plot(data[0,range(1,data.shape[1])]*1e9,data[2,range(1,data.shape[1])], color=map(1./(J+1)), lw=2.0, label=str([legenda[1],os.path.split(directories_to_analyze[J])[1]]) )
			plot(data[0,range(1,data.shape[1])]*1e9,data[3,range(1,data.shape[1])], '--', color=map(1./(J+1)), lw=2.0, label=str([legenda[2],os.path.split(directories_to_analyze[J])[1]]) )
		if plot_log == True:
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[2,range(1,data.shape[1])], color=map(1./(J+1)), lw=2.0, label=str([legenda[1],os.path.split(directories_to_analyze[J])[1]]) )
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[3,range(1,data.shape[1])], '--', color=map(1./(J+1)), lw=2.0, label=str([legenda[2],os.path.split(directories_to_analyze[J])[1]]) )

		xlabel('Time (ns)')
		legend(loc="best")
		grid(True)

	###---> 3 <---###
	if display==0 or display==3:
 		figure(3)

		if plot_log == False:
			plot(data[0,range(1,data.shape[1])]*1e9,data[0,range(1,data.shape[1])], color=map(1./(J+1)), lw=2.0, label=str([legenda[0],os.path.split(directories_to_analyze[J])[1]]) )
			plot(data[0,range(1,data.shape[1])]*1e9,data[1,range(1,data.shape[1])], '--', color=map(1./(J+1)), lw=2.0, label=str([legenda[1],os.path.split(directories_to_analyze[J])[1]]) )
			plot(data[0,range(1,data.shape[1])]*1e9,data[2,range(1,data.shape[1])], ':', color=map(1./(J+1)), lw=2.0, label=str([legenda[2],os.path.split(directories_to_analyze[J])[1]]) )
			plot(data[0,range(1,data.shape[1])]*1e9,data[3,range(1,data.shape[1])], '.', color=map(1./(J+1)), lw=2.0, label=str([legenda[3],os.path.split(directories_to_analyze[J])[1]]) )
 			plot(data[0,range(1,data.shape[1])]*1e9,data[4,range(1,data.shape[1])], ',', color=map(1./(J+1)), lw=2.0, label=str([legenda[4],os.path.split(directories_to_analyze[J])[1]]) )
	 		plot(data[0,range(1,data.shape[1])]*1e9,data[5,range(1,data.shape[1])], '+', color=map(1./(J+1)), lw=2.0, label=str([legenda[5],os.path.split(directories_to_analyze[J])[1]]) )
			plot(data[0,range(1,data.shape[1])]*1e9,data[6,range(1,data.shape[1])], '|', color=map(1./(J+1)), lw=2.0, label=str([legenda[6],os.path.split(directories_to_analyze[J])[1]]) )
		if plot_log == True:
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[0,range(1,data.shape[1])], color=map(1./(J+1)), lw=2.0, label=str([legenda[0],os.path.split(directories_to_analyze[J])[1]]) )
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[1,range(1,data.shape[1])], '--', color=map(1./(J+1)), lw=2.0, label=str([legenda[1],os.path.split(directories_to_analyze[J])[1]]) )
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[2,range(1,data.shape[1])], ':', color=map(1./(J+1)), lw=2.0, label=str([legenda[2],os.path.split(directories_to_analyze[J])[1]]) )
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[3,range(1,data.shape[1])], '.', color=map(1./(J+1)), lw=2.0, label=str([legenda[3],os.path.split(directories_to_analyze[J])[1]]) )
 			semilogy(data[0,range(1,data.shape[1])]*1e9,data[4,range(1,data.shape[1])], ',', color=map(1./(J+1)), lw=2.0, label=str([legenda[4],os.path.split(directories_to_analyze[J])[1]]) )
	 		semilogy(data[0,range(1,data.shape[1])]*1e9,data[5,range(1,data.shape[1])], '+', color=map(1./(J+1)), lw=2.0, label=str([legenda[5],os.path.split(directories_to_analyze[J])[1]]) )
			semilogy(data[0,range(1,data.shape[1])]*1e9,data[6,range(1,data.shape[1])], '|', color=map(1./(J+1)), lw=2.0, label=str([legenda[6],os.path.split(directories_to_analyze[J])[1]]) )

		xlabel('Time (ns)')
		legend(loc="best")
		title('../'+os.path.split(path)[1])
		grid(True)

show()