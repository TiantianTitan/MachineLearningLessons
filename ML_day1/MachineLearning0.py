#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:54:32 2023

@author: haotian
"""

import numpy as np
import matplotlib.pyplot as plt

# d = np.random.rand(10)
# print(d)
# print(d<0.5)
# print(d[d<0.5]) # index bool



data = 2* np.random.rand(10000,2) -1
print(data)
x = data[:,0]
y = data[:,1]
idx = x**2 + y** 2 <1
hole = x**2 + y ** 2 < 0.25
idx = np.logical_and(idx,~hole)
plt.plot(x[idx],y[idx],'go',markersize = 1)
plt.show()



