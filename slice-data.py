#%%
# plots the depth-dose distribution from the datasets in data folder
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# this slice the bragg peak data into several sections of n_points 
n_points=3
threshold =5000
directory = "data" # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']
colnames2=['Energy','p1','p2','p3']


def get_energy(file):
    #print(file)
    e = file.split("-")
    return e[0]


d =[]

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): #or filename.endswith(".py"): 
        #print(os.path.join(directory, filename))
        energy=get_energy(filename)
        df = pd.read_csv(os.path.join(directory, filename),skiprows=3,header=0,names=colnames)   
        #plt.plot(df['Z'],df['Total Dose'])
        for i in range(0,299-n_points-1,n_points):
            if(df['Total Dose'][i]>threshold):
                d.append([energy,df['Total Dose'][i],df['Total Dose'][i+1],df['Total Dose'][i+2]])
        continue
    else:
        continue

df_merged = pd.DataFrame(d,columns=colnames2)
plt.plot(df_merged['Energy'],df_merged['p2'])

#%%