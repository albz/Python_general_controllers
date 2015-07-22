#!/usr/bin/python
######################################################################
# Name:         dued_read_frm.py
# Author:       A. Marocchino
# Date:			2013-07-30
# Purpose:      reads dued binary frm output
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib
import struct
from scipy import *
import numpy as np
from matplotlib import *
import pylab as pyl
### --- ###



# - #
def read_read(dir_path,nframe):

	# - #
	#dir_path = '/Volumes/Macintosh_HD_2/sims/non_local_electrons/polar_spike_pushing/f_007_00024'
	sub_path = os.path.join(os.path.join('out','frm'),'2D')
	name     = '%3s%0.4i.dued'%('frm',nframe)
	path     = os.path.join(os.path.join(dir_path,sub_path),name)

	f = open(path,'rb')

	struct.unpack('i', f.read(4)); niverg = struct.unpack('i', f.read(4)); struct.unpack('i', f.read(4))
	struct.unpack('i', f.read(4)); time = struct.unpack('d', f.read(8))[0]; struct.unpack('i', f.read(4))
	struct.unpack('i', f.read(4)); NIP1 = struct.unpack('i', f.read(4))[0]; NJP1 = struct.unpack('i', f.read(4))[0]; struct.unpack('i', f.read(4));

	#---***---#
	z = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			z[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	r = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			r[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	rho = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			rho[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	te = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			te[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	ti = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			ti[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	ur = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			ur[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	uz = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			uz[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	tr = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			tr[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	zs = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			zs[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	p = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			p[i,j] = struct.unpack('d', f.read(8))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	imater = np.zeros((NIP1,NJP1))
	struct.unpack('i', f.read(4))
	for i in range(0,NIP1):
		for j in range(0,NJP1):
			imater[i,j] = struct.unpack('i', f.read(4))[0]
	struct.unpack('i', f.read(4))

	#---***---#
	struct.unpack('i', f.read(4)); tetam = struct.unpack('d', f.read(8))[0]; struct.unpack('i', f.read(4))
	struct.unpack('i', f.read(4)); zsmin = struct.unpack('d', f.read(8))[0]; struct.unpack('i', f.read(4))

	#---***---#
	f.close()


	return time, NIP1, NJP1, r, z, rho, te, ti, ur, uz, tr, zs, p, imater, tetam, zsmin
