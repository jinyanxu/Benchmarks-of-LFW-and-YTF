
# coding: utf-8

# In[1]:

import numpy as np
from skimage import io
import h5py


# In[2]:

def load_lfw_data(txt_name):
    path = open('/home/danning/face_verif/'+txt_name, 'r')
    #load data from pairs.txt
    lines = path.readlines()
    X_1 = []
    X_2 = []
    Y = []
    
    for i in range(len(lines)):
        lines[i]=' '.join(lines[i].split())
        list=lines[i].split(' ')
        X_1.append(io.imread('/home/danning/face_verif/lfw_#2/'+list[0]+'_'+list[1].zfill(4)+'.bmp'))
        if len(list)==3:
            #images of same person
            Y.append(1)
            X_2.append(io.imread('/home/danning/face_verif/lfw_#2/'+list[0]+'_'+list[2].zfill(4)+'.bmp'))
        else:
            #images of different people
            Y.append(0)
            X_2.append(io.imread('/home/danning/face_verif/lfw_#2/'+list[2]+'_'+list[3].zfill(4)+'.bmp'))
    return (np.asarray(X_1),np.asarray(X_2),Y)


# In[16]:

def load_ytf_data(txt_name):
    path = open('/home/danning/face_verif/'+txt_name, 'r')
    lines = path.readlines()
    X_1 = []
    X_2 = []
    Y = []
    for i in range(len(lines)):
        list=lines[i].split(', ')
        first = list[2].split('/')
        second = list[3].split('/')
        X_1.append(io.imread('/home/danning/face_verif/ytf_one_faces/'+first[0]+'_'+first[1]+'.jpg'))
        X_2.append(io.imread('/home/danning/face_verif/ytf_one_faces/'+second[0]+'_'+second[1]+'.jpg'))
        #print(int(list[4][0]))
        Y.append(int(list[4]))
    #print(Y)
    return (np.asarray(X_1),np.asarray(X_2),np.asarray(Y))
        


# In[21]:

def compress_data(txtname):
    (X_1, X_2, Y) = load_ytf_data(txtname)
    #Y = [a.encode('utf8') for a in Y]


    # Create the HDF5 file
    f = h5py.File('ytf_data.h5', 'w')

    # Create the image and palette dataspaces
    face1set = f.create_dataset('face1', data = X_1)
    face2set = f.create_dataset('face2', data = X_2)
    yset = f.create_dataset('y', data = Y)


    #Close the file
    f.close()


# In[22]:

#compress_data('splits.txt')


# In[23]:

def loadData(path):
    f = h5py.File(path, 'r')
    data = [f['face1'][:], f['face2'][:], f['y'][:]]
    return data

