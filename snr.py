#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 08:23:08 2018

@author: docboy (Atharva)

git: atdocboy

Edit changes required
1). time param needs to be changed from the last value TO the index of the last value
              
"""

import numpy as np
import pandas as pd


# Code to get the graphical representations of Suport and Resistance line

# We define a function that takes in three params-
# 1). data - a time series/1-D vector
# 2). lag - This defines a window of consideration, wherein we perform the 
#           analysis related to plotting the support and resistance lines
#         #######  The default value of lags is set to 1/3 of the length of data series #######
#
# 3). time - This clarifies the point preceeding which the lines are plotted.
#           ####### Default value is last point of data series ##############

def snr(data, lags=None, time=None): 
    
    ##############################
    
    # checking input param validity
    if ((type(lags) is int) or (lags is None)):
        pass
    else:
        return('lags param must be an int value')
    if (type(time) is int) or (time is None):
        pass
    else:
        return('time param must be an int value')
    
    # Defining the input params explicitly
    
    # Check for data param
    
    data = np.array(data)
       
    if (data.ndim ==1):     # Checks for 1-D 
       pass
    else:
        return('Please check the dimensions of the entered data, must be a 1-D array')
        
    # Check for lags
    if lags is None:
        print ('The value of the window paramter is set to default')
        print ('viz:- (1/3)rd of length of the data series, ie :-')
        
        lags = round((1/3)*(len(data)))
        print (lags)
    
    if (lags>len(data)):
        print('The value of lag specified exceeds the length of data series')
        print('Enter a new value of lags less than:-', len(data))
        
        a = int(input('Enter new value of lags:'))
        if (a>len(data)):
            return('EXITING FUNCTION AS lags EXCEEEDS DATA LENGTH')
        else:
            print('lags has been set to:', a)
            lags = a
    
    # Check for time
    if time is None:
        print ('time param has been set to default viz: last entry of data series:-')
        time = data[len(data)-1]    # NOTE: len(data)-1 has been used to offset the indexing in python
        print (time)
    
    if (time>len(data)):
        print('The value of time specified exceeds the length of data series')
        print('Enter a new value of time less than:-', len(data))
        
        b = int(input('Enter new value of time:'))
        if (b>len(data)):
            return('EXITING FUNCTION AS lags EXCEEEDS DATA LENGTH')
        else:
            print('time has been set to:', b)
            lags = b
        return ('time exceeds data length, rerun the function')          
               
    else:
        pass
    
    ################################

    # Begin snr logic
    
          
   ############

               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               