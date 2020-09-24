#%%
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os



directory = "data" # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']
colnames2=['Energy','p1','p2','p3']


def get_energy(file):
    #print(file)
    e = file.split("-")
    return float(e[0])



def get_subsamples(dir="data",n_points=3, threshold=5000):
    """Takes a depth-dose data and splits it into several sections
    each containing n_points. This is repeated for all dd data
    inside folder dir and an array is returned. The first column of this array is the energy
    and remaining n_points columns contain the dose at that energy.
    If the first point in the section is below the threshold, that section is not appended to the array """
    d =[]
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): #or filename.endswith(".py"): 
            #print(os.path.join(directory, filename))
            energy=get_energy(filename)
            df = pd.read_csv(os.path.join(dir, filename),skiprows=3,header=0,names=colnames)   
            #plt.plot(df['Z'],df['Total Dose'])
            #print(threshold)
            for i in range(0,299-n_points-1):
                if(df['Total Dose'][i]>threshold):
                    # TODO: This works only for n_points=3. Must change to automatically accommodate all other sizes!!
                    dose=np.empty(n_points)
                    arr =np.empty(n_points+1)
                    arr[0] = energy
                    for j in range(0,n_points):
                        dose[j]=df['Total Dose'][i+j]
                        arr[j+1]=df['Total Dose'][i+j]
                    max=np.max(dose)
                    arr = arr/max
                    arr[0] =energy 
                    #d.append([energy,df['Total Dose'][i]/max,df['Total Dose'][i+1]/max,df['Total Dose'][i+2]/max])
                    d.append(arr)
            continue
        else:
            continue
    return np.array(d)


def load_bp_data(split=75,dir="data",n_points=3, threshold=5000):
    """returns the training data and testing data 
    split% is used as training data and the rest for testing
    the other arguments are the same as get_subsamples"""
    
    a = range(1,n_points+1)
    data = get_subsamples(dir,n_points,threshold)
    e_max=np.max(data[:,[0]])

    n_test = int(0.75*data.shape[0])
    train = data[:n_test-1]
    test = data[n_test:]
    
    train_x = train[:,a]
    train_y = train[:,[0]]/e_max
    
    test_x = test[:,a]
    test_y = test[:,[0]]/e_max
    return train_x, train_y, test_x, test_y





train_x, train_y, test_x, test_y= load_bp_data(n_points=25,threshold=30000)

train_xt = np.transpose(train_x)

#plt.plot(train_xt[:,range(0,100)])
reg = MLPRegressor(solver='sgd', alpha=1e-5,hidden_layer_sizes=(100, 100), random_state=1)
reg.fit(train_x,train_y)
predictions=reg.predict(train_x) 
#np.append(predictions,test_y, axis=1)
train_y = train_y.flatten()
diff = predictions-test_y
plt.scatter(train_y,predictions)
