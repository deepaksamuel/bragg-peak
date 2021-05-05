#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


x = np.arange(-15,15,0.0001)
y = np.sin(x)
z = np.sin(x)
dydx = np.sin(x)

idx=0

for i in x:
  if i<0 or i> np.pi:
    z[idx]= 0
  else:
    z[idx]=1
  idx = idx+1

z = z*y
#plt.plot(x,z)
#plt.plot(x,y*z)

idx=0
while idx<len(z)-1:
  dydx[idx] = (z[idx+1] - z[idx])/(x[idx+1] - x[idx])
  idx= idx+1

plt.scatter(x,dydx)
plt.show()
