#!/usr/bin/python
######################################################################
# Name:         rain_man.py
# Author:       A. Marocchino
# Date:			2011-12-13
# Purpose:      nml manupulation for DUED
# Source:       python
#####################################################################

# <<< >>>
# rain_man.py
# <<< >>>
#
# nml manupulation
#       +
# sim.out reading with values extraction
# only subrotuines
#
# A. Marocchino 13-12-2011
#

### loading libraries
import re, os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
### --- ###




# dued.nml read
def read_nml(path,nml_name):
    file = open(os.path.join(path,nml_name),"r")
    nml = []
    for line in file:
    	line.strip()
    	nml.append(line)
    file.close()
    return nml



# dued.nml write
def write_nml(path,nml,nml_name):
    file = open(os.path.join(path,nml_name),"w")
    for line in nml:
    	file.writelines(line)
    file.close()



# find in dued.nml and substitute
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


#--- old version: works for sim.out ---#
#--- the new version works with the file.name from input ---#
# find in > sim.out
def find_in_simout(path,string_to_search,strategy):
	f=[]
	for line in open(os.path.join(path,'sim.out'),"r"):
		if string_to_search in line:
		#if re.match("\s*"+re.escape(string_to_search)+"\s"+"\s*",line): #Exact Matching: much slower
			for t in line.split():
				try:
					f.append(float(t))
				except ValueError:
					pass
	if strategy == 'max':
		return max(f)
	if strategy == 'all':
		return f

#-new version-#
# find in > file
def find_in_file(path,filename,string_to_search,strategy):
	f=[]
	for line in open(os.path.join(path,filename),"r"):
		if string_to_search in line:
		#if re.match("\s*"+re.escape(string_to_search)+"\s"+"\s*",line): #Exact Matching: much slower
			for t in line.split():
				t = re.sub(r"[dD]","e","%s" % t)
				try:
					f.append(float(t))
				except ValueError:
					pass
	if strategy == 'max':
		return max(f)
	if strategy == 'all':
		return f



# find in > dued.nml
def find_in_nml(path,param):

	#f   = []
	nml = read_nml(path,'dued.nml')

	for n in range(0,len(nml)):
		line   =  nml[n]
		m      =  re.match(r"(\s*"+re.escape(param)+"\s*=\s*)([^ ,]+)(.*)$",line,re.I)
		nline  =  line

		if m != None:
			digging_in = line[m.start(2):].lower()
			digging_in=digging_in.replace(',',' ')
			digging_in=digging_in.replace('d','e')
			for t in digging_in.split():
				try:
					return float(t)
				except ValueError:
					pass
	f = -1
	return f



# find in > sigma.txt
def find_in_sigma(path):
	f=[]
	file = open(os.path.join(path,'out/sigma/sigma.txt'),"r")
	read = file.readlines()
	file.close()
	del read[0:279] #Remove Headers
	for line in read:
		#if string_to_search in line:
		for t in line.split():
			try:
				f.append(float(t))
			except ValueError:
				pass
	return f[2],f[4]
