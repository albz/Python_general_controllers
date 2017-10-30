#!/usr/bin/python
######################################################################
# Name:         truncate_colormap.py
# Author:		A. Marocchino
# Date:			2017-10-30
# Purpose:      utility to truncate colormaps
# Source:       python
#####################################################################

### loading libraries
import matplotlib.pyplot as plt
import matplotlib.colors as colors
### --- ###


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap
