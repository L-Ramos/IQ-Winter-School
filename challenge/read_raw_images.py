#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:32:29 2018

@author: user
"""

def Read_Raw_Images(path_data,path_labels):
    
    """
    Takes the path of the data and labels, read the images and saves 4 numpy arrays with training and testing data and labels
    """
    
    data = skimage.io.imread(path_data).astype(np.float32)
    for i in range(data.shape[0]):
        data[i,...] = skimage.exposure.rescale_intensity(data[i,...], out_range=(0,1))
    data_labels = skimage.io.imread(path_labels) > 0
    
    training_data=data[0:25,:,:]
    training_labels=data_labels[0:25,:,:]
    
    testing_data=data[25:data.shape[0],:,:]
    testing_labels=data_labels[25:data.shape[0],:,:]
        
    np.save("data.npy",training_data)
    np.save("labels.npy",training_labels)
    np.save("data_validation.npy",testing_data)
    np.save("labels_validation.npy",testing_labels)
    
    return()