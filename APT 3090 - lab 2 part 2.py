# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:39:13 2022

@author: nshut
"""

import math
import random

def primeNumbers(a, b):
    
    primeNumbersInRange = []
    
    for number in range (a,b):
        
        if number == 0 or number == 1:
            continue
        
        #Prime numbers are greater than one
        elif number >= 1:
            
            for i in range(2, int(math.sqrt(number))+1):
                
                if (number % i) == 0:
                    break
            else:
                primeNumbersInRange.append(number)
                
        else:
            continue
    
    return primeNumbersInRange

def gcd(a,b):
    
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi(n):
    
    result = 1
    for i in range(2, n):
        if (gcd(i, n)==1):
            result += 1
    return result
    

rangeStart = int(input("Enter the first number in your range: "))

rangeEnd = int(input("Enter the last number in your range: "))

primeNumbersList = primeNumbers(rangeStart, rangeEnd)

if rangeStart < rangeEnd:
          
   if len(primeNumbersList) == 0:
       print("There are no prime numbers in the given range!")
        
   else:
       
       p = random.choice(primeNumbersList)
       q = random.choice(primeNumbersList)
       
       print("The random prime numbers p and q in your range are: ")
       
       print("p = " + str(p))
       print("q = " + str(q))
       
       print("---Applying Euler's Totient Function---")
       
       print("phi(",p,") = " ,
             phi(p), sep = "" )
       
       print("phi(",q,") = " ,
             phi(q), sep = "" )
        
else:
    print("The range you entered is invalid!")
