# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:37:48 2021

@author: clydemichelle
"""

#Defining the X variables
x1 = -2
x2 = 5

#Function to solve greater than comparison
def getX(x1,x2):
    if x1 > x2:
        print("x1:",x1," is greater than x2",x2)
    elif x2 > x1:
        print("x2:",x2, "is greater than x1:",x1)
    else:
        print("Both values are equal")
 
#Calling the function
greaterX = getX(x1, x2)
print(greaterX)
