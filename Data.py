
# coding: utf-8

# In[11]:

import numpy as np
from skimage import io
import h5py


# In[12]:

def load_lfw_data(txt_name):
    path = open('/home/danning/lfw/'+txt_name, 'r')
    #load data from pairs.txt
    lines = path.readlines()
    X_1 = []
    X_2 = []
    Y = []
    
    for i in range(len(lines)):
        lines[i]=' '.join(lines[i].split())
        list=lines[i].split(' ')
        X_1.append(io.imread('/home/danning/lfw/lfw_#2/'+list[0]+'_'+list[1].zfill(4)+'.bmp'))
        if len(list)==3:
            #images of same person
            Y.append(1)
            X_2.append(io.imread('/home/danning/lfw/lfw_#2/'+list[0]+'_'+list[2].zfill(4)+'.bmp'))
        else:
            #images of different people
            Y.append(0)
            X_2.append(io.imread('/home/danning/lfw/lfw_#2/'+list[2]+'_'+list[3].zfill(4)+'.bmp'))
    return (np.asarray(X_1),np.asarray(X_2),Y)


# In[13]:

def compress_lfw_data():
    (X_1, X_2, Y) = load_lfw_data('pairs.txt')
    # Create the HDF5 file
    f = h5py.File('lfw_data.h5', 'w')

    # Create the image and palette dataspaces
    x1set = f.create_dataset('face1', data = X_1)
    x2set = f.create_dataset('face2', data = X_2)
    yset = f.create_dataset('y', data = Y)
    

    # Close the file
    f.close()


# In[14]:

def loadData(path):
    f = h5py.File(path, "r")
    data = [f['face1'][:], f['face2'][:], f['y'][:]]
    return data


# In[15]:

compress_lfw_data()


# In[ ]:



