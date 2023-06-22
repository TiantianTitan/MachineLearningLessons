#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:27:41 2023

@author: haotian
"""

import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd

x = np.linspace(0,1,100)
print(x)
y = x**x
plt.plot(x,y,'r-',linewidth = 3)
plt.show()



