#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:11:11 2023

@author: haotian
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

d = np.random.rand(3,4)
print(d)
print(type(d))
data = pd.DataFrame(data =d, columns= list('abcd'))
print('='*50)
print(data)
print(type(data))
print(data['b'])
data.to_csv('data.csv',index = False, header= True)
print("file ouput succeed")