#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:53:42 2018

@author: docboy (Atharva)

git: atdocboy
"""


###### Import useful libraries #########

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######################################

def snr (y, window = None):
    # This function takes in the parameter y: a 1D vector.
    # The function attempts to calculate the levels of Support and Resistance.


    ########## Init param checks ###########
    
    # First convert y to a 1D array
    y = np.array(y)
    
   # We now initiate checks to ensure that the input y is a 1-D vector
    
    if (y.ndim ==1):
       pass
    else:
        return('Please check the dimensions of the entered array')
        
    if window is None:
        print ('The value of the window paramter is set to default')
        print ('The default value of the window param is:-')
        print ('##############') # There is a need for clarification here.
        
    ######################################
    
