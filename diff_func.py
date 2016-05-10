#! /usr/bin/env python
"""
File: diff_func.py

Copyright (c) 2016 Michael Seaman

License: MIT

Description: a module for analyzing the approximated
derivatives of given functions, that have particularly
chaotic behavior
"""


import numpy as np
import matplotlib.pyplot as plt
from calculus import discrete_func

def f(x):
    return np.log(x + .01)

def g(x):
    return np.cos( np.exp(10 * x) )

def h(x):
    return x ** x

def f_prime(x):
    return 1 / (x + .01)

def g_prime(x):
    return -10 * np.exp(10 * x) * np.sin( np.exp(10 * x) )

def h_prime(x):
    lnx)xx+xxx−1
    return np.log(x) * h(x) + x* x** (x-1)

def linear_func(x):
    return 8*x - 12


def plot_approx_derivative(f, a, b, n):
    """
    Takes a function f and calculates its derivative with 'diff2'
    then plots it over the interval a to b.
    """
    xList = np.linspace(a, b, n+1)
    yList = diff2(f, a, b, n)
    plt.plot(xList, yList)
    plt.title(f.__name__ + "'(x)")
    plt.show()

def plot_analytic_and_discrete_derivatives(f, f_prime, a, b, n):
    """
    Takes original function f and it's found analyitic derivative. Evaluates
    the functions derivative according to the finite difference formula over a
    to b and plots the discrete values alongside the discretized f_prime.
    """
    xList_discrete = np.linspace(a, b, n+1)
    yList_discrete = diff2(f, a, b, n)
    plt.plot(xList_discrete, yList_discrete, 'r')
    xList_analytic = discrete_func(f_prime, a, b, n)[0]
    yList_analytic = discrete_func(f_prime, a, b, n)[1]
    plt.plot(xList_analytic, yList_analytic, 'g')
    plt.title("Analytic " + f.__name__ + "'(x) [green] vs Approximated " + f.__name__ + "'(x) [red]")
    plt.show()


def diff2(f, a, b, n):
    """
    Re-worked from CW 5
    
    Evaluates the derivative over a to b with n finite difference points
    Uses matrix multiplaction to sum the indivdual weights
    """
    x, y = discrete_func(f, a, b, n)
    h = ( b - a ) / float(n)

    ident_h = np.identity(n - 1) * 1 / (2 * h)
    ident_h = np.lib.pad(ident_h, ((1,1), (2,0)), 'constant', constant_values=(0)) 
    ident_neg_h = np.identity(n - 1) * -1 / (2 * h)
    ident_neg_h = np.lib.pad(ident_neg_h, ((1,1), (0,2)), 'constant', constant_values=(0))
    matrix =  ident_h + ident_neg_h

    matrix[0][0] = -1 / h
    matrix[0][1] = 1 / h
    matrix[-1][-1] = 1 / h
    matrix[-1][-2] = -1 / h
    return np.dot(matrix, y)

def test_diff2_linear():
    """
    Tests the matrix-multiplaction based differentiation method on a linear function
    which it should approximate perfectly, including the edges
    f(x) = 8x - 12
    f'(x) = 8
    """
    a = -20
    b = 20
    n = 1000
    exact_dfdx = np.zeros(n + 1) + 8
    print exact_dfdx
    print diff2(linear_func, a, b, n)
    assert np.allclose(exact_dfdx, diff2(linear_func, a, b, n))
