#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:41:51 2023

@author: haotian
"""
import numpy as np

a = np.arange(1,10000000) # quand a --> infini   result_pi --> pi

result_pi = np.sqrt( 6* np.sum(1/( a ** 2 )))

print(result_pi)

x = np.arange(1,20)
print(np.sum(1/x.cumprod())+1) #  e