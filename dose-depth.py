#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries'] 
df = pd.read_csv('250-MEV.txt',skiprows=3,header=0,names=colnames) 
plt.plot(df['Z'],df['Total Dose'])



# %%
