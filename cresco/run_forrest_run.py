#!/usr/bin/python
######################################################################
# Name:         run_forrest_run
# Author:       A. Marocchino
# Date:			26-06-2013
# Purpose:      run a series of independent simulations ON CRESCO
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil, time, subprocess
### --- ###


path = os.getcwd()


#--- *** ---# flags
flags_nottoberun =  ["==started==","==completed==","==suspended==","==suspend==","==failed=="]
# flags_nottoberun =  ["=started=","=completed=","=suspended=","=failed="]
flags_nottoberun = set(flags_nottoberun)


#--- *** ---# prune not necessary sub dirs
def prune_dirs(dirs):
	if 'out' in dirs:
		dirs.remove('out')
	if 'dump' in dirs:
		dirs.remove('dump')


#--- *** ---# 
#   main    #
#--- *** ---#
if __name__ == '__main__':
	print "Forrest begins to run... runs begin here"
	print "cluster version for Cresco"
	print "queue single processor runs\n\n\n"
	
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
 		if 'dued.nml' in files and len(flags_nottoberun.intersection(set(files))) == 0:
			proc = subprocess.Popen('bsub -o lsf.out -e lsf.err -q cresco_serh24 ~/scripts/runDUEDserial.sh', shell=True, cwd=root_dir)
			proc.wait()
	
 	print "\n\nLaunched everything I found in my search"



