#%%
# Analysis using the erdf file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def create_col_names():
    dd =[]
    for i in range(100,252,2):
        dd.append("MeV "+str(i))
    return np.array(dd)

c = create_col_names()
col_list = pd.Series(np.arange(100,252,2)).astype(str) + ' MeV'
df = pd.read_csv('erdf.txt',skiprows=2,header=0,delimiter="\t",names=col_list)   


#step =10
for step in range(5,7):
    data =[]
    for w in range(295):
        energy=100
        nr=0
        dr=0
        for e  in range(0,76,step):
            nr+=df.iloc[w,e]*energy
            dr+=df.iloc[w,e]
            energy=energy+step*2
        data.append(nr/dr)
    plt.plot(data)
    

# %%