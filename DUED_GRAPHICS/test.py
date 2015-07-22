#!/usr/bin/python
######################################################################
# Name:         dued_read
# Date:			25-07-2011
# Purpose:      read dued output
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, string
import pylab, matplotlib, math
import struct
from scipy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import pylab as pyl
# from mpl_toolkits.mplot3d import Axes3D
# from scipy.interpolate import griddata

import re, os, os.path, glob, sys, shutil, time, datetime, scipy, numpy, pylab, matplotlib, string, math
from scipy import *
from numpy import *
from matplotlib import *
from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3


### --- ###
from dued_read import *
### --- ###

dir_path = '/Volumes/Macintosh_HD_2/sims/non_local_electrons/polar_spike_pushing/f_007_00024'
step=198
dir_path = '/Users/alberto/sims/PALS/PALS_nle_001'
step=30
time, NIP1, NJP1, r, z, rho, te, ti, ur, uz, tr, zs, p, imater, tetam, zsmin = read_read(dir_path,step)

rc = np.zeros((NIP1,NJP1))
zc = np.zeros((NIP1,NJP1))
for i in range(0,NIP1-1):
	for j in range(0,NJP1-1):
		rc[i,j] = 0.25 * ( r[i,j]+r[i+1,j]+r[i,j+1]+r[i+1,j+1] )
		zc[i,j] = 0.25 * ( z[i,j]+z[i+1,j]+z[i,j+1]+z[i+1,j+1] )		

X = Y = Z = np.zeros(NIP1*NJP1)
k=0
for i in range(0,NIP1-1):
	for j in range(0,NJP1-1):
		X[k] = rc[i,j]
		Y[k] = zc[i,j]
		Z[k] = rho[i,j]
		k+=1

# fig = pyl.figure(1, figsize=(8.00, 8.00))
# ax  = plt.subplot(111)
# ax.plot(r[0:95,0:4],z[0:95,0:4])
# ax.plot(rc[1:94,1:4],zc[1:94,1:4],linestyle='none',marker='.')
# pyl.show()


#print rc.shape, rc.min()

fig = pyl.figure(1, figsize=(8.00, 8.00))
ax = fig.add_subplot(111, projection='3d')
# #ax.plot_surface(X, Y, Z)
ax.plot_surface(rc[1:-1,1:-1]*1e4, zc[1:-1,1:-1]*1e4, rho[1:-1,1:-1])
# pyl.xlim(-50,50)
# pyl.ylim(0,50)
pyl.show()

def fun(x, y):
  return x**2 + y

# fig = pyl.figure()
# ax = fig.add_subplot(111, projection='3d')
# x = y = np.arange(-3.0, 3.0, 0.05)
# X, Y = np.meshgrid(x, y)
# zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
# Z = zs.reshape(X.shape)
# 
# ax.plot_surface(X, Y, Z)


# pyl.show()


# 
# 
#

#pylab.contourf(rc, zc, rho, 50, aspect='equal') 

print  rc.min(), rc.max()
print  zc.min(), zc.max()
print len(X),len(Y),len(Z)
x = np.linspace(min(X),max(X),200)
y = np.linspace(min(Y),max(Y),200)

z = griddata(X,Y,Z,x,y)



