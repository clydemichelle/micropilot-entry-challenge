# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:37:48 2021

@author: clydemichelle
"""

#Defining the X variables
x1 = -2
x2 = 5

#Adding the variable to a list
X = []
X.append(x1)
X.append(x2)


#function to get greatest value of X
def getX(X):
#Traversing through the list
    for i in X:
        greaterX = 0
        if i > greaterX:
            greaterX+=i
            print(i)

greatestX = getX(X)
print(greatestX)
        
