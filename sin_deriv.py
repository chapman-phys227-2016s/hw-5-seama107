#! /usr/bin/env python
"""
File: sin_deriv.py

Copyright (c) 2016 Michael Seaman

License: MIT

Description: a module for plotting the approximated derivative of 
a given function f alongside its analyitical derivative.
f(x, e) = sin((x+e)^-1)
f'(x, e) = -cos((x+e)^-1)/(x+e)^2
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x, e):
    return np.sin(1/(x + e))

def f_prime(x, e):
    return -1 * np.cos(1/(x + e)) * (x + e)**-2

def diff(f, e, a, b, n):
    """
    Re-worked from classwork 5 - 
    Takes a function f(x, e) and returns discrete values
    evaluated along its derivative.
    """
    f = np.vectorize(f)
    x = np.linspace(a, b, n+1)
    y = np.zeros(len(x))
    z = np.zeros(len(x))
    h = (b-a)/float(n)
    y = f(x, e)
    for i in xrange(len(x)-1):
        z[i] = (y[i+1] - y[i])/h
    z[n] = (y[n] - y[n-1])/h
    return z

def plot_alongside_derivative(f, f_prime, e, a, b, n):
    """
    Plots a function f(x, e) alongside its derivative
    f_prime(x, e) that is found through the finite 
    difference formula from a to b with n points
    """
    f = np.vectorize(f)
    x = np.linspace(a, b, n+1)
    df = f_prime(x, e)
    df_approx = diff(f, e, a, b, n)
    plt.plot(x, df, 'g')
    plt.plot(x, df_approx, 'r')
    plt.title("Approx f'(x) [green] vs given f'(x) [red] for n = {} and e = {}".format(n, e))
    plt.show()

