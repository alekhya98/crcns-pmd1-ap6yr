# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
from scipy.io import loadmat

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MD_1 = loadmat('MM_S1_processed.mat')
MD_1.keys() #tells us this is a dictionary with differnt levels

type(MD_1)['Data'], MD_1['Data'].shape #1 by 1 array with 16 structures (sub-levels)

def read_neuron(md, key='Data', value = 'kinematics', row = (0,1), column = 0):
       return(md[key][0,0][value][row, column])

read_neuron(MD_1)

#this function only accesses kinematics data via 'value = "kinematics"', but we also anticipate accessing neural recording data in the same way so that we can ask questions about how neural activity in certain brain regions and reach kinematics are related