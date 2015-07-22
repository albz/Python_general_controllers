#!/usr/bin/python
######################################################################
# Name:         stop_forrest_stop
# Author:       A. Marocchino
# Date:			05-04-2011
# Purpose:      suspends all running simulations, flag ==suspend==
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil, time, signal
### --- ###


### Path
path = os.getcwd()

### Search - add FLAGs - abort Python RunForrestRun
for root_dir, sub_dirs, files in os.walk(path):
	for file in files:
		if file == ".run_forrest_run_pid":
			f = open(os.path.join(root_dir,file),'r')
			for line in f:
				pid = line.strip()
				try:
					os.kill(int(pid), signal.SIGTERM)
					print "run_forrest_run python program stopped, in:",root_dir,"  -- pid:",pid
					print " "
				except:
					pass
			f.close()
 			os.remove(os.path.join(root_dir,file))
		if file == "==started==":
			tmp = open(os.path.join(root_dir, '==suspend=='), 'w')
			tmp.close()
			print "Simulation suspended @:",root_dir

