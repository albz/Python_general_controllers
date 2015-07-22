#!/usr/bin/python
######################################################################
# Name:         S-Bubba   
# Author:       Angelo Schiavi 2010
# Purpose:      run a series of independent simulations
# Source:       python
#####################################################################
import os
import sys
import shutil


if(len(sys.argv)<5):
	print "usage  : %s exec_path nproc nmin nmax" % sys.argv[0]
	print "example: %s ~/Codes/foo.exe 4 0 35" % sys.argv[0]
	sys.exit()


exe=sys.argv[1]
nmaxjobs=int(sys.argv[2])
n0=int(sys.argv[3])
n1=int(sys.argv[4])
nrunning=0

def launch1(jobid):
	global nrunning
	pid = os.fork()
	if pid == 0:
		print "Jobid ", jobid
		path = "%05d" % jobid 
# 		os.mkdir(path)
# 		shutil.copy2('dued.nml', path)
		os.chdir(path)
		command = exe + "> sim.out"
 		os.system(command)
		sys.exit()
	else:
 		nrunning=nrunning+1

if __name__ == '__main__':
	print "Running from",n0,"to",n1
	nrunning=0
	for n in range(n0,n0+nmaxjobs):
		launch1(n)

	while n<n1:
		os.waitpid(-1,0)
		nrunning=nrunning-1
		n=n+1
		launch1(n)
	
	while(nrunning>0):
		os.waitpid(-1,0)
		print "Still running:",nrunning
		nrunning=nrunning-1
	
	print "End of runs"