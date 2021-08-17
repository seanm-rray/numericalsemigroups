import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# reads in the file (make sure you use the one with renamed column headings)
data=pd.read_csv('bigdata.tsv',sep='\t')

# put column headings here that you want to plot for x,y,z
# THESE HAVE BEEN RENAMED so they only use approved characters for Python variable names
# choices are 'p', 'q', 'r', 'gcd_p_q', 'gcd_p_r', 'gcd_q_r',
# 'p_over_gcd_p_q', 'p_over_gcd_p_r', 'q_over_gcd_p_q', 'q_over_gcd_q_r',
# 'r_over_gcd_p_r', 'r_over_gcd_q_r', 'Genus', 'Frobenius', 'MinSet', 'Embedding'

# pick your three variables here:
x="p"
y="gcd_p_r"
z="Embedding"

# this filters the data so that only points where the condition you put is TRUE are used
data=data[data.gcd_p_r>1]

# use .max() or .min() in the line below
grouped=data[[x,y,z]].groupby([x,y]).min() # this calculates the max or min z-value for each value of (x,y)

# for some reason we have to do this, idk why
grouped=grouped.reset_index()

# defining the input arrays for the fitting
XY=grouped[[x,y]].values
X=grouped[x].values
Y=grouped[y].values
Z=grouped[z].values

# here is where you define what kind of function you want to fit
# arguments to the function have to be (1) your data and (2) all the coefficients you want it to use
# I put some different examples, use whichever you like or write more if you want!

def linear_fit(inputs,a,b,c): # this is for fitting a linear/planar function
    x=inputs[:,0]
    y=inputs[:,1]
    return a*x+b*y+c

def quadratic_fit(inputs,a,b,c,d,e,f): # this is for fitting a quadratic (degree 2) function
    x=inputs[:,0]
    y=inputs[:,1]
    return a*x*x+b*y*y+c*x*y+d*x+e*y+f

def rational_fit(inputs,a,b,c,d,e,f): # this is for fitting a rational function
    x=inputs[:,0]
    y=inputs[:,1]
    return g/(a*x*x+b*y*y+c*x*y+d*x+e*y+f)

# performs the curve fit and prints the best choice for the coefficients
coeffs,_ = curve_fit(linear_fit,XY,Z)
print("best coefficients for the function you picked are",coeffs)

# this is for the scatter plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
ax1.scatter(X,Y,Z, marker='.',color='b') # display original data in blue
# VERY IMPORTANT -- you can replace coeffs[0], coeffs[1] etc. with hand-picked values if you like
# ALSO VERY IMPORTANT -- if you use a different function, change the name in the line below,
# and pass it the correct number of coeffs[0], coeffs[1], etc. arguments
ax1.scatter(X,Y,linear_fit(XY,coeffs[0],coeffs[1],coeffs[2]),marker='.',color='r') # displays fitted function in red
ax1.set_xlabel(x)
ax1.set_ylabel(y)
ax1.set_zlabel(z)

# this is for the surface plot -- comment this section out if your data is too linear looking
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
ax2.plot_trisurf(X,Y,Z,color='b') # display original data in blue
# VERY IMPORTANT -- you can replace coeffs[0], coeffs[1] etc. with hand-picked values if you like
# ALSO VERY IMPORTANT -- if you use a different function, change the name in the line below,
# and pass it the correct number of coeffs[0], coeffs[1], etc. arguments
ax2.plot_trisurf(X,Y,linear_fit(XY,coeffs[0],coeffs[1],coeffs[2]),color='r') # displays fitted function in red
ax2.set_xlabel(x)
ax2.set_ylabel(y)
ax2.set_zlabel(z)

# actually displays the plots
plt.show()
