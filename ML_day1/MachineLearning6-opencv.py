#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:15:22 2023

@author: haotian
"""

import cv2
image = cv2.imread("lena.png")
print(image)
print(type(image))
print(image.shape)

