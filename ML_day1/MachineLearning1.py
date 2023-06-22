#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:02:34 2023

@author: haotian
"""

import numpy as np
import matplotlib.pyplot as plt

p = np.random.rand(10000)
np.set_printoptions(edgeitems= 5000, suppress= True)
print(p)
plt.hist(p,bins = 20, color= 'g', edgecolor = 'k')
plt.show()

N= 10000
times = 100
z = np.zeros(N)
for i in range(times):
    z+= np.random.rand(N)
z/= times
plt.hist(z,bins = 20, color='m',edgecolor = 'k')
