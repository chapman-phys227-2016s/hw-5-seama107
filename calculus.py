#!/usr/bin/python
"""
Cw5 the pinacle of grupwork and efficienceyc and comroodery

Calculus module implementing
discrete function function
differentiation function
and trapezoidal integration function

"""


import numpy as np
import math

def diff(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = np.zeros(len(x))
    z = np.zeros(len(x))
    h = (b-a)/float(n)
    for i in xrange(len(x)):
        y[i] = f(x[i])
    for i in xrange(len(x)-1):
        z[i] = (y[i+1] - y[i])/h
    z[n] = (y[n] - y[n-1])/h
    return y, z


def discrete_func(f, a, b, n):
    x = np.linspace(a, b, n+1)
    g = np.vectorize(f)
    y = g(x)
    return x, y

def diff2(f, a, b, n):
    x, y = discrete_func(f, a, b, n)
    matrix = np.zeros((n,n))
    h = ( b - a ) / float(n)
    count = -1
    for i in range(n):
        if(count >= 0 and count < n-2):
            matrix[i][count] = 1 / (2 * h)
            matrix[i][count + 2] = -1 / (2 * h)
        count += 1
    matrix[0][0] = -1 / h
    matrix[0][1] = 1 / h
    matrix[-1][-1] = 1 / h
    matrix[-1][-2] = -1 / h
    print np.dot(matrix, matrix)



def trapezoidal_matrix(f, a, b, n):
    """Trapezoidal integration via matrix multiplication."""
    h = (b-a)/float(n)
    indexer = np.linspace(a, b, n)
    values = f(indexer)
    matrixer = np.zeros(n)
    matrixer.fill(h)
    matrixer[0] = h/2.0
    matrixer[n - 1] = h/2.0
    I = np.dot(values, matrixer)
    return I

def test_trap_matrix():
    """Trapezoidal integration via matrix multiplication verified by integrating
    the sine function on the integral 0 to pi over 2."""
    apt = np.abs(trapezoidal_matrix(np.sin, 0, np.pi/2.0, 10000) - 1) < 1e-3
    msg = 'That aint how the sine do.'
    assert apt, msg
