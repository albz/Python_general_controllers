#!/usr/bin/python
######################################################################
# Name:         plotcpu
# Date:			06-04-2011
# Purpose:      sobstitute the old plotmtv *cpu, Simulation time VS CPU time
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
### --- ###

# - #
map     = get_cmap('jet')

# - # plot in 'hours'
if len(sys.argv)>1 and sys.argv[1] == '-h':
	plot_in_hours = True
else:
	plot_in_hours = False

### --- ###
for J in range(0,len(sys.argv)):
	#Path from argument
	if len(sys.argv) == 1:
		path = os.getcwd()
	else:
		path = sys.argv[J]
	
	#Search & Load
	for files in glob.glob(os.path.join(path,'cpu')):
		cpu_file = files
		print 'eccolo',cpu_file
		#Load
		data = numpy.genfromtxt(cpu_file, unpack=True)
		CPU_time =  data[0,range(1,data.shape[1])]	
		SIM_time =  data[1,range(1,data.shape[1])]
		NSTEP    =  data[2,range(1,data.shape[1])]
		
		#CPU_time scaled
		if plot_in_hours == True:
			CPU_time = CPU_time/3600
		
		#Plot
		subplot(211)
		plot(CPU_time,SIM_time*1e9, label=os.path.split(path)[1], lw=1.3 )
		subplot(212)
		plot(NSTEP,SIM_time*1e9, label=os.path.split(path)[1], lw=1.3 )

subplot(211)
grid(True)
if plot_in_hours == True:
	xlabel('CPU Time [h]')
else:
	xlabel('CPU Time [s]')
ylabel('Simulation Time (ns)')

subplot(212)
grid(True)
xlabel('n-steps')
ylabel('Simulation Time (ns)')
legend(loc="lower right")

show()
