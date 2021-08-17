import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('bigdata.tsv',sep='\t')

# put column headings here that you want to plot for x,y,z
# choices are 'p', 'q', 'r', 'gcd(p,q)', 'gcd(p,r)', 'gcd(q,r)',
# 'p/gcd(p,q)',        'p/gcd(p,r)', 'q/gcd(p,q)', 'q/gcd(q,r)',
# 'r/gcd(p,r)', 'r/gcd(q,r)', 'Genus', 'Frobenius', 'MinSet', 'Embedding'
x="p"
y="gcd(p,r)"
z="Embedding"

# use .max() or .min() in the line below
grouped=data[[x,y,z]].groupby([x,y]).max() # this calculates the max or min z-value for each value of (x,y)

grouped=grouped.reset_index()

fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
ax1.scatter(grouped[x], grouped[y], grouped[z], marker='.')
ax1.set_xlabel(x)
ax1.set_ylabel(y)
ax1.set_zlabel(z)

X=grouped[x]
Y=grouped[y]
Z=grouped[z]

fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')

ax2.plot_trisurf(X,Y,Z, linewidth=0.2, antialiased=True)
ax2.set_xlabel(x)
ax2.set_ylabel(y)
ax2.set_zlabel(z)

plt.show()
