#%%
# merges all depth dose data into one single table
# first column: energy; rest of the columns: dose at the depths
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


directory = "data" # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']
colnames=['Energy','D1','D2']
df_merged = pd.DataFrame()
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): #or filename.endswith(".py"): 
        #print(os.path.join(directory, filename))
        df = pd.read_csv(os.path.join(directory, filename),skiprows=3,header=0,names=colnames)   
        plt.plot(df['Z'],df['Total Dose'])
        continue
    else:
        continue


# %%