#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:25:11 2023

@author: haotian
"""

import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd

# [-4,2]
d = np.random.rand(100)*6-4
print(d)
plt.plot(d,'r.')
plt.show()