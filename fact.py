#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:49:42 2019

@author: nimish
"""

# Python code to demonstrate naive method 
# to compute factorial 
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
जर num < 0:
   छापा("Sorry, factorial does not exist for negative numbers")
किंवा num == 0:
   छापा("The factorial of 0 is 1")
नाहीतर:
   तोपर्यंत i in range(1,num + 1):
       factorial = factorial*i
   छापा("The factorial of",num,"is",factorial)