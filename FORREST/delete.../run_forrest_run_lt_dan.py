#!/usr/bin/python
######################################################################
# Name:         run_forrest_run_lt_dan
# Author:       A. Marocchino
# Date:			04-06-2010
# Purpose:      run a series of independent simulations from
#               lt_dan.txt input file
# Source:       python
#####################################################################

### loading shell commands
import os, sys, shutil
### --- ###

### shell inputs
if(len(sys.argv)<2):
	print "usage  : %s nproc" % sys.argv[0]
	print "example: %s 4" % sys.argv[0]
	sys.exit()

nmaxjobs=int(sys.argv[1])
path = os.getcwd()

### Counting how many process I still have to run
def counting_lines():
	f = open(os.path.join(path, 'chocolate_box.txt'), 'r')
	all = f.readlines()
	i=0
	for line in all:
		i=i+1
	f.close()
	return i

### Eliminating line for launched simulation
def remove_simulation():
	N = counting_lines()
	f = open(os.path.join(path, 'chocolate_box.txt'), 'r')
	all     = f.readlines()
	f.close()
	all_new = all[1:N]
	f = open(os.path.join(path, 'chocolate_box.txt'), 'w')
	f.writelines(all_new)
	f.close()
	print all_new
	
### Getting path to run
def get_path_to_run():
	f = open(os.path.join(path, 'chocolate_box.txt'), 'r')
	line = f.readline()
	f.close()
	return line.split()[0]
	
### Getting executable
def get_exe():
	f = open(os.path.join(path, 'chocolate_box.txt'), 'r')
	line = f.readline()
	f.close()
	return line.split()[1]	

### launching process subroutine
def launch1(jobid, path_to_run, exe):
	global nrunning
	pid = os.fork()
	if pid == 0:
		print "Jobid ", jobid
		tmp = open(os.path.join(path_to_run, '==running=='), 'w')
		tmp.close()
		os.chdir(path_to_run)
		command = exe + ' dued.nml '+ '> sim.out'
 		os.system(command)   ###RUNNING COMMAND
		tmp = open(os.path.join(path_to_run, '==completed=='), 'w')
		tmp.close()
		os.remove(os.path.join(path_to_run, '==running=='))
		sys.exit()
	else:
 		nrunning=nrunning+1


### main
if __name__ == '__main__':
	print "I am gonna get a chocolate... runs begin here"
	nrunning=0

	for n in range(0,nmaxjobs):
		path_to_run = get_path_to_run()
		exe         = get_exe()
		remove_simulation()
		launch1(n,path_to_run,exe)

	while counting_lines() > 0:
		os.waitpid(-1,0)
		nrunning=nrunning-1
		n=n+1
		path_to_run = get_path_to_run()
		exe         = get_exe()
		remove_simulation()
		launch1(n,path_to_run,exe)
	
	while(nrunning>0):
		os.waitpid(-1,0)
		print "Still running:",nrunning
		nrunning=nrunning-1

	print "End of runs for this task"
