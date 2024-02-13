"""
Created on Mon Jul  3 09:02:51 2023

@author: sandy
"""

import numpy as np
import matplotlib.pyplot as plt

#Question 1: Show if f(g(2)) = g(f(2))
def f(x):
    f = x**2 - 6*x + 2
    return f

def g(x):
    g = -2*x
    return g

def test_f_of_g():
    x = 2
    assert f(g(x)) == g(f(x))

#Question 2: Find geometric mean
def GM(A):
    n = len(A)
    mean = A[0]
    for i in range(1,n):
        mean = A[i]*mean
    geo_mean = mean**(1/n)
    return geo_mean

#Question 3: Filter a list for numbers divisible by 5 or 8
def list_breaker(data):
    x = [x for x in data if x % 5 == 0 or x % 8 == 0]
    return x

#Question 4: Write a recursive function for f
def fn(function, n, x):
    fun = function(x)
    for i in range(1,n):
        fun = function(fun)
    return fun

#Question 5: Plot a new function
def new_f(x):
    function = np.exp(-x)*np.cos(2*np.pi*x)
    return function

def plot_f(x, function):
    plt.plot(x,function(x))
    plt.show()
    
x = np.linspace(0,5,1000)
plot_f(x, new_f)
