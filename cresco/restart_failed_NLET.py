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


#--- *** ---# 
#--- *** ---# prune not necessary sub dirs
def prune_dirs(dirs):
	if 'out' in dirs:
		dirs.remove('out')
	if 'dump' in dirs:
		dirs.remove('dump')

#--- *** ---# dued.nml read
def read_nml(path,nml_name):
    file = open(os.path.join(path,nml_name),"r")
    nml = []
    for line in file:
    	line.strip()
    	nml.append(line)
    file.close()
    return nml

#--- *** ---# dued.nml write
def write_nml(path,nml):
    file = open(os.path.join(path,'dued.nml'),"w")
    for line in nml:
    	file.writelines(line)
    file.close()

#--- *** ---# find in dued.nml and substitute
def nml_substitution(nml,param,value_to_substitute):

	# Case 0: value_to_substitute is a NUMBER - Floating point
	if isinstance(value_to_substitute,float) == True:
		for n in range(0,len(nml)):
			line   =  nml[n]
			m      =  re.match(r"(\s*"+re.escape(param)+"\s*=\s*)([^ ,]+)(.*)$",line,re.I)
			nline  =  line
		
			if m != None:
				val = value_to_substitute
				nval = re.sub(r"[eE]","d","%e" % val) # do this for getting the double precision in the fortran nml assignement
				nline = line[:m.start(2)] + nval + line[m.end(2):] #+ '\n'
				nml[n]=nline

	# Case 1: value_to_substitute is a NUMBER - Integer
	if isinstance(value_to_substitute,int) == True:
		for n in range(0,len(nml)):
			line   =  nml[n]
			m      =  re.match(r"(\s*"+re.escape(param)+"\s*=\s*)([^ ,]+)(.*)$",line,re.I)
			nline  =  line
		
			if m != None:
				val = value_to_substitute
				nval = re.sub(r"[eE]","d","%d" % val) # do this for getting the double precision in the fortran nml assignement
				nline = line[:m.start(2)] + nval + line[m.end(2):] #+ '\n'
				nml[n]=nline

	# Case 2: value_to_substitute is a STRING
	if isinstance(value_to_substitute,str) == True:
		for n in range(0,len(nml)):
			line   =  nml[n]
			m      =  re.match(r"(\s*"+re.escape(param)+"\s*=\s*)([^ ,]+)(.*)$",line,re.I)
			nline  =  line
		
			if m != None:
				val = value_to_substitute
				nline = line[:m.start(2)] + val + ",\n" #+ line[m.end(2):] #+ '\n'
				nml[n]=nline

	return nml





#--- *** ---# 
#   main    #
#--- *** ---#
if __name__ == '__main__':
	print "Restart Failed sims on Cresco for NLET case"
	
	for root_dir, sub_dirs, files in os.walk(path):
		prune_dirs(sub_dirs)
		if 'dued.nml' in files and '==failed==' in files:
			nml = read_nml(root_dir,'dued.nml')
			time_crash = float(open(os.path.join(root_dir,'cpu'), 'r').readlines()[-1].split()[1])
			proc = subprocess.Popen('python ~/scripts/DUED/cleanallDUED.py', shell=True, cwd=root_dir)
			proc.wait()
			nml = nml_substitution(nml,'timestopnlet', time_crash - 2.0e-11 )
			write_nml(root_dir,nml)
			proc = subprocess.Popen('mkdir dump out out/eos out/exe out/frm out/frm/1D out/frm/2D out/hst out/map out/stk', shell=True, cwd=root_dir)
			proc.wait()
			proc = subprocess.Popen('bsub -o lsf.out -e lsf.err -q cresco_serh24 ~/scripts/runDUEDserial.sh', shell=True, cwd=root_dir)
			#proc = subprocess.Popen('bsub -o lsf.out -e lsf.err -q cresco_serh144 ~/scripts/runDUEDserial.sh', shell=True, cwd=root_dir)
			proc.wait()
#--- ---#



