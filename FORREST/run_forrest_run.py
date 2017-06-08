#!/usr/bin/python
######################################################################
# Name:         run_forrest_run
# Author:       A. Marocchino
# Date:			06-04-2013
# Purpose:      run a series of independent simulations
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil, time
### --- ###

### shell inputs
if(len(sys.argv)<4):
	print("usage  : %s exec_path nproc prog-name" % sys.argv[0])
	print("example: %s ~/Codes/ciao_belli.exe 4 dued" % sys.argv[0])
	sys.exit()

exe=sys.argv[1]
nmaxjobs=int(sys.argv[2])
prog=str(sys.argv[3])
path = os.getcwd()


#--- *** ---#
if(prog=='dued'):
	input_file_name = 'dued.nml'
if(prog=='architect'):
	input_file_name = 'architect.nml'

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



#--- *** ---# finds the first available simulation not yet runned or running
def first_available_simulation():
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
# 		if 'dued.nml' in files and list(flags_nottoberun)[0] in files:
# 		# check whether zombie process
# 			filerunning = open(os.path.join(root_dir, list(flags_nottoberun)[0]))
# 			pid = filerunning.readlines()
# 			filerunning.close()
# 			try:
# 				os.kill(int(pid[0]), 0)
# 			except:
# 			#zombie process
# 				tmp = open(os.path.join(root_dir, '=failed='), 'w')
# 				tmp.close()
# 				os.remove(os.path.join(root_dir, list(flags_nottoberun)[0]))
		if input_file_name in files and len(flags_nottoberun.intersection(set(files))) == 0:
			return root_dir

#--- *** ---# finds how many simulations to run in total
def total_number_of_simulations():
	i = 0
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
		if input_file_name in files and len(flags_nottoberun.intersection(set(files))) == 0:
			i = i + 1
	return i



#--- *** ---# launching process subroutine
def launch1(jobid):
	global nrunning
	pid = os.fork()
	if pid == 0:
		print("Jobid ", jobid)
		path_to_run = first_available_simulation()
		os.chdir(path_to_run)
#  		command = exe + ' dued.nml '+ '> sim.out'
		command = exe + ' ' + input_file_name + ' > sim.out'
		os.system(command)   ###RUNNING COMMAND
		sys.exit()
	else:
 		nrunning=nrunning+1


#--- *** ---# Write and Delete python file with PID IDs.
def write_python_pid(pid):
	f = os.path.join(path,'.run_forrest_run_pid')
	if  os.path.exists(f):
		f = open(f,'a+')
		f.writelines('\n'+str(pid))
	else:
		f = open(f,'w+')
		f.writelines(str(pid))
	f.close()

def delete_file_python_pid():
	f = os.path.join(path,'.run_forrest_run_pid')
	if os.path.exists(f):
		os.remove(f)



#--- *** ---#
#   main    #
#--- *** ---#
if __name__ == '__main__':
	print("Forrest begins to run... runs begin here")
	nrunning=0

	write_python_pid(os.getpid())

	for n in range(0,min(nmaxjobs,total_number_of_simulations())):
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


	delete_file_python_pid()


	print("End of runs for this task")
