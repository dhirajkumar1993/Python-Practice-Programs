# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 02:05:05 2018

@author: Dhiraj Kumar
"""
import math
number = 100

for i in range(2,int(number**(0.5))):
	if (number % i == 0):
		print ("Number is composite")
	else:
		print("Number is prime")