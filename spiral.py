#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 01:14:13 2019

@author: hannakristensen


module for spiral
"""

def spiral():
	x = 0
	y = 0
	d = 1
	m = 1
	listX = []
	listY = []
	for i in range(0, 10):
		while((2 * x * d) < m):
			listX.append(x)
			listY.append(y)
			x = x + d
		while((2 * y * d) < m):
			listX.append(x)
			listY.append(y)
			y = y + d
		d = -1 * d
		m = m + 1
	
	return listX, listY
