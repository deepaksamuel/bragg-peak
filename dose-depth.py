#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries'] 
# df = pd.read_csv('data/150.000000-MEV-10000000-EVTS.txt',skiprows=3,header=0,names=colnames) 
# plt.scatter(df['Z'],df['Total Dose'])


directory = "data" # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']     
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".txt"): #or filename.endswith(".py"): 
         print(os.path.join(directory, filename))
         df = pd.read_csv(os.path.join(directory, filename),skiprows=3,header=0,names=colnames)   
#         plt.scatter(df['Z'],df['Entries'])
         plt.plot(df['Z'],df['Total Dose'])
         # print(os.path.join(directory, filename))
         #break
     else:
         continue


# %%
