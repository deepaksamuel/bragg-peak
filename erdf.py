#%%
# creates the erdf file and also plots the erdf curves.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


directory = "data" # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']
<<<<<<< HEAD
for i in range(200,201) :
=======
dd =[]
for i in range(0,298) :
>>>>>>> f21ae8d9c9ca0cad51b5e32dff3c04158e3e3bf7
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
<<<<<<< HEAD
    plt.show()
=======
    dd.append(first_val)
    
np.savetxt('erdf.txt',dd,delimiter='\t')
plt.show()
# ERDF data: Columns correspond to energy. First column: 100 MeV Last column: 250 MeV, Step: 2 MeV. 
# Rows correspond to WEPL. First row: 0 mm; last row: 299 mm; step: 1 mm
>>>>>>> f21ae8d9c9ca0cad51b5e32dff3c04158e3e3bf7


# %%