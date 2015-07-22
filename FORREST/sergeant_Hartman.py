#!/usr/bin/python
######################################################################
# Name:         sergeant_Hartman
# Author:       A. Marocchino
# Date:			22-12-2012
# Purpose:      run a series of commands in dued run folders
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil, time
### --- ###

#--- *** ---# shell inputs
print " "
print "usage(1) *** 3-inputs  : python   sergeant_Hartman.py   exec_path   output_fname   nproc"
print "usage(4) *** 4-inputs  : python   sergeant_Hartman.py   exec_path   input_for_exe  output_fname   nproc"
print " "
if(len(sys.argv) not in range(4,6)):
	print "***WHATCH OUT*** wrong usage!"
	sys.exit()
	
	
#--- *** ---# reading input parameters
if len(sys.argv) == 4:
	exe             =  sys.argv[1]
	output_filename =  sys.argv[2]
	nmaxjobs        =  int(sys.argv[3])
elif len(sys.argv) == 5:
	exe             =  sys.argv[1]
	input_for_exe   =  sys.argv[2]
	output_filename =  sys.argv[3]
	nmaxjobs        =  int(sys.argv[4])
path            =  os.getcwd()



#--- *** ---# prune not necessary sub dirs
def prune_dirs(dirs):
	if 'out' in dirs:
		dirs.remove('out')
	if 'dump' in dirs:
		dirs.remove('dump')

#--- *** ---# find a full run simulation (and not yet analyzed! or not beING analyzed)
def folder_to_analyze():
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
		# 1st line  -  full run sim
		# 2nd line  -  not yet analyzed
		# 3rd line  -  not being analyzed
		if 'dued.nml' in files and '==completed==' in files \
		and output_filename not in files \
		and output_filename + '_tmp' not in files :               
			print 'analyzing folder >>>',root_dir
			return root_dir
			
#--- *** ---# finds how many simulations to run in total
def total_number_of_simulations():
	i = 0
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
		for file in files:
			if file == 'dued.nml':
				if (os.path.exists(os.path.join(root_dir, "==completed==")) == True) and (os.path.exists(os.path.join(root_dir,output_filename)) == False): 
					i = i + 1
	return i-nmaxjobs

#--- *** ---# launching process subroutine
def launch1(jobid):
	global nrunning
	pid = os.fork()
	if pid == 0:
		#print "Jobid ", jobid
		path_to_run = folder_to_analyze()
		os.chdir(path_to_run)
		if len(sys.argv) == 4:
			command = exe + '> ' + output_filename + '_tmp'
			#print command
		if len(sys.argv) == 5:
			command = exe + ' < ' + input_for_exe +'  >  ' + output_filename + '_tmp'
			#print command
 		os.system(command)   #running command
 		
 		shutil.move(os.path.join(path_to_run,output_filename + '_tmp'), os.path.join(path_to_run,output_filename))
		
		sys.exit()
	else:
 		nrunning=nrunning+1




#--- *** ---# 
#   main    #
#--- *** ---#
if __name__ == '__main__':
	print "Sergeant Hartman begins to give orders... get ready to follow instructions!"
	print "\n"
	nrunning=0
	
	for n in range(0,nmaxjobs):
		launch1(n)
		time.sleep(0.3)

	while total_number_of_simulations() > 0:
		os.waitpid(-1,0)
		nrunning=nrunning-1
		n=n+1
		launch1(n)
		time.sleep(0.3)

	while(nrunning>0):
		os.waitpid(-1,0)
		#print "Still running:",nrunning
		nrunning=nrunning-1

	print "End of runs for this task"

