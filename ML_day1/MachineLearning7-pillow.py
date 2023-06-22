#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:37:36 2023

@author: haotian
"""

from PIL import Image
import numpy as np

a = Image.open("lena.png")
print(a)
b = np.array(a)
print(b)
print(type(b))
print(b.shape)