#!/usr/bin/python
######################################################################
# Name:         forrest_whereareyou
# Author:       A. Marocchino
# Date:			05-04-2011 / 2015-07-19
# Purpose:      returns how many sims have been runned, how many are running, and how many still to go
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, sys
### --- ###


path = os.getcwd()

#--------------------------------#
#---#
class run_status:

	def __init__(self):
		self.identifier = []
		self.program = []
		self.path = []
		self.time = []
		self.dt = []
		self.status = []

	def new_sim_status(self,identifier,program,path,time,dt,status):
		self.identifier.append(counter)
		self.program.append(program)
		self.path.append(path)
		self.time.append(time)
		self.dt.append(dt)
		self.status.append(status)
		
	def print_whole_status(self):
		print self.identifier
		print self.program
		print self.path
		print self.time
		print self.dt
		print self.status
		
	def count_run(self,program,status):
		nsim=0
		for id in self.identifier:
			if self.program[id] == program and self.status[id] == status:
				nsim += 1
		return nsim

	def print_status(self,program,status):
		print program,' : ', status , ' : >>>', self.count_run(program,status)
		for id in self.identifier:
			if self.program[id] == program and self.status[id] == status:
				print self.path[id], '--- lastest sim time: %2.4f (ns) --- dt=%2.4e' % (self.time[id],self.dt[id])
	
	def print_general_status(self,program):
		print '*** *** ***'
		print "%-8s %-3s %-23s %4d" % (program,">>>","Simulations run so far:",self.count_run(program,'==completed=='))
		print "%-8s %-3s %-23s %4d" % (program,">>>","Simulations running:",self.count_run(program,'==started=='))
		print "%-8s %-3s %-23s %4d" % (program,">>>","Simulations to run:",self.count_run(program,'to_be_run'))
		print "%-8s %-3s %-23s %4d" % (program,">>>","Simulations suspended:",self.count_run(program,'==suspended=='))
		print "%-8s %-3s %-23s %4d" % (program,">>>","Simulations failed:",self.count_run(program,'==failed=='))
		print "%-8s %-3s %-23s %4d" % (program,">>>","Zombie Simulations:",self.count_run(program,'==zombie=='))
		print '*** *** ***'

#--- *** ---#
def find_running_time(path):
	try:
		return float(open(os.path.join(path,'cpu'), 'r').readlines()[-1].split()[1])*1e9
	except:
		return 0.0 

#--- *** ---#
def find_last_dt(path):
	try:
		return float(open(os.path.join(path,'cpu'), 'r').readlines()[-1].split()[1]) - float(open(os.path.join(path,'cpu'), 'r').readlines()[-2].split()[1])
	except:
		return 0.0 

#--- *** ---#
def get_flag(path):
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
		if '==started==' in files:
			f = open(os.path.join(root_dir,'==started=='),'r')
			pid = int(f.readline().strip())
			try:
				os.kill(pid, 0)
				return '==started=='
			except:
				return '==zombie=='
		elif '==completed==' in files:
			return '==completed=='
		elif '==suspended==' in files:
			return '==suspended=='
		elif '==failed==' in files:
			return '==failed=='
		else:
			return 'to_be_run'


#--- *** ---#	
def prune_dirs(dirs):
	if 'out' in dirs:
		dirs.remove('out')
	if 'dump' in dirs:
		dirs.remove('dump')




#--- *** ---#
#--  MAIN --#
#--- *** ---#

runs    = run_status()
counter = 0
for root_dir, sub_dirs, files in os.walk(path):
	prune_dirs(sub_dirs)
	if 'dued.nml' in files:
		time = find_running_time(root_dir)
		dt   = find_last_dt(root_dir)
		flag = get_flag(root_dir)
		runs.new_sim_status(counter,'dued',root_dir,time,dt,flag)
		counter += 1
		
	if 'datain.inp' in files:
		time = find_running_time(root_dir)
		dt   = find_last_dt(root_dir)
		flag = get_flag(root_dir)
		runs.new_sim_status(counter,'architect',root_dir,time,dt,flag)
		counter += 1


runs.print_general_status('dued')
runs.print_status('dued','==started==')
runs.print_status('dued','==failed==')
runs.print_status('dued','==zombie==')
runs.print_status('dued','==completed==')

runs.print_general_status('architect')
runs.print_status('architect','==started==')
runs.print_status('architect','==failed==')
runs.print_status('architect','==zombie==')
runs.print_status('architect','==completed==')

	
