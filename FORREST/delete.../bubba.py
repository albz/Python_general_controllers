#!/usr/bin/python
######################################################################
# Name:         bubba
# Author:       A. Marocchino
# Date:			05-06-2010
# Purpose:      run a series of independent simulations for post-processing
#               it requires the file ==completed== or ==running== to be in
#				in the folder
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil
### --- ###

### shell inputs
if(len(sys.argv)<2):
	print "usage  : %s exec_path nproc" % sys.argv[0]
	print "example: %s ~/Codes/ciao_belli.exe 4" % sys.argv[0]
	sys.exit()

exe=sys.argv[1]
nmaxjobs=int(sys.argv[2])
path = os.getcwd()
sims_to_run=[]


### finds all simulations to run
def simulations_to_run():
	N_sims_to_run=0
	for root_dir, sub_dirs, files in os.walk(path):
		for file in files:
			if file == 'dued.nml':
				if (os.path.exists(os.path.join(root_dir, "==running==")) == True) or (os.path.exists(os.path.join(root_dir, "==completed==")) == True): 
					sims_to_run.append(root_dir)
					N_sims_to_run = N_sims_to_run + 1
	return N_sims_to_run


### launching process subroutine
def launch1(jobid,runned):
	global nrunning
	pid = os.fork()
	if pid == 0:
		print "Jobid ", jobid
		path_to_run = sims_to_run[runned]
		os.chdir(path_to_run)
		command = exe + '< ~/Codes/DUED_PP_Fourier_Series/cos_k.txt' + '> bubba.out'
 		os.system(command)   ###RUNNING COMMAND
		sys.exit()
	else:
 		nrunning=nrunning+1


### main
if __name__ == '__main__':
	print "Forrest begins to run... runs begin here"
	
	N_sims_to_run = simulations_to_run()
	runned  = 0
	nrunning= 0
	
	for n in range(0,nmaxjobs):
		print 'runned > ',runned
		launch1(n,runned)
		runned=runned+1

	while N_sims_to_run > runned:
		os.waitpid(-1,0)
		nrunning=nrunning-1
		n=n+1
		print 'runned > ',runned
		launch1(n,runned)
		runned = runned + 1
	
	while(nrunning>0):
		os.waitpid(-1,0)
		print "Still running:",nrunning
		nrunning=nrunning-1


	print "End of runs for this task"
