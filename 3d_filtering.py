import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# reads in the file (make sure you use the one with renamed column headings)
data=pd.read_csv('C:\\Users\\14842\Desktop\\xyz.txt',sep='\t')

# put column headings here that you want to plot for x,y,z
# THESE HAVE BEEN RENAMED so they only use approved characters for Python variable names
# choices are 'p', 'q', 'r', 'gcd_p_q', 'gcd_p_r', 'gcd_q_r',
# 'p_over_gcd_p_q', 'p_over_gcd_p_r', 'q_over_gcd_p_q', 'q_over_gcd_q_r',
# 'r_over_gcd_p_r', 'r_over_gcd_q_r', 'Genus', 'Frobenius', 'MinSet', 'Embedding'

# pick your three variables here:
x="x"
y="y"
z="z"

# this filters the data so that only points where the condition you put is TRUE are used
#data=data[data.gcd_p_r==1]

# you can filter more than one condition, too, like this:
#data=data[(data.gcd_q_r==1) & (data.p==data.r)]

# use .max() or .min() in the line below
grouped=data[[x,y,z]].groupby([x,y]).max() # this calculates the max or min z-value for each value of (x,y)

# for some reason we have to do this, idk why
grouped=grouped.reset_index()

# just to save typing I did these lines
X=grouped[x]
Y=grouped[y]
Z=grouped[z]

# this is for the scatter plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
ax1.scatter(X,Y,Z, marker='.')
ax1.set_xlabel(x)
ax1.set_ylabel(y)
ax1.set_zlabel(z)

# I've left the surface plot commented out because if the filtering results
# in a linear-looking plot, triangulated surface plotting won't work

#fig2 = plt.figure()
#ax2 = fig2.gca(projection='3d')
#ax2.plot_trisurf(X,Y,Z, linewidth=0.2, antialiased=True)
#ax2.set_xlabel(x)
#ax2.set_ylabel(y)
#ax2.set_zlabel(z)

# actually displays the scatter plot
plt.show()
