#%%
# plots the ERDF distribution from the datasets in data folder
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


directory = "data" # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']
for i in range(151,152) :
    first_val=[]
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): #or filename.endswith(".py"): 
            #print(os.path.join(directory, filename))
            df = pd.read_csv(os.path.join(directory, filename),skiprows=3,header=0,names=colnames)   
            first_val.append(df['Total Dose'][i])

            continue
        else:
            continue
    plt.plot(first_val)

plt.show()

# %%