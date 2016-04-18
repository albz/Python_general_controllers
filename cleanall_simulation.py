#!/usr/bin/python
######################################################################
# Name:         run_forrest_run
# Author:       A. Marocchino
# Date:			01-03-2011
# Date:			26-12-2011
# Purpose:      delete all files in a folder but dued.nml, saves the FORTRAN file!!!
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, sys, shutil, time, string
### --- ###


#Path
path = os.getcwd()

#namelist files
nml_file = ['dued.nml','dued_1D.nml','dued.nml_1D','dued_2D.nml','dued.nml_2D','architect.nml','makefile','Makefile'];

#Exclusion List
Exc_list = ['.nml','nml_1D','nml_2D','.f','.f90','.c','.cpp','.py','.inp','.m'];


#Search and Delete
for root_dir, sub_dirs, files in os.walk(path):
	nml_exists = 0
	for file in files:
		if file in nml_file:
			nml_exists += 1
		if file not in nml_file and os.path.splitext(file)[1] not in Exc_list:
			os.remove(os.path.join(root_dir,file))

	if nml_exists > 0 and os.path.exists(os.path.join(root_dir,'out')) == True:
 		shutil.rmtree(os.path.join(root_dir,'out'))
	if nml_exists > 0 and os.path.exists(os.path.join(root_dir,'dump')) == True:
 		shutil.rmtree(os.path.join(root_dir,'dump'))
