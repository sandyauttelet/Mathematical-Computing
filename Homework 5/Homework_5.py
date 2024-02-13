"""
Created on Wed Jul 26 13:28:06 2023

@author: sandy
"""

import numpy as np
import scipy as sc
import sympy as sp
import matplotlib.pyplot as plt

#Homework 5: Integration 1

def f(x):
    return np.sin(x)

F = -np.cos(2*np.pi) + np.cos(0)

Integrals = []
dx = [1,0.1,0.01,0.001,0.0001,0.00001,0.000001]
for i in range(len(dx)):
    x = np.arange(0,2*np.pi,dx[i])
    I = sum(f(x))*dx[i]
    Integrals.append(I)

errors = []
for i in range(len(Integrals)):
    error = np.abs(F - Integrals[i])
    errors.append(error)
    
for i in range(len(errors)):
    #print(errors[i],dx[i],dx[i]**2,dx[i]**3)
    print(dx[i]**2,dx[i]**3)
    
#Homework 5: Integration 2
h = 0.01
def f(x):
    return np.exp(-x**2)

def F(x):
    return sc.integrate.quad(f,0,x)

def edF(x):
    constants = np.array([-1/12,2/3,0,-2/3,1/12])
    funvals = np.array([F(x+2*h),F(x+h),\
                        F(x),F(x-h),F(x-2*h)])
    return (1/h)*np.dot(constants,funvals)

assert np.allclose(f(2),edF(2)[0])
print(f(2),edF(2))

A = [[1,2,3],[4,5,6],[7,8,9]]
n = len(A)
trace = sum(np.diag(A))

e = np.eye(n)
A_inv = np.zeros((n,n))
for i in range(n):
    A_inv[i] = np.linalg.solve(A,e[i])
    
A_inv_true = np.linalg.inv(A)

assert np.allclose(A_inv,A_inv_true)
