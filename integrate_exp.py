#! /usr/bin/env python
"""
File: integrate_exp.py

Copyright (c) 2016 Michael Seaman

License: MIT

Description: a module for evaluating the improper integral
of f from -inf to +inf given below. The integrator class and
the midpoint integrator from HW 9 will be used as it already
has running tests.
f(x) = e^(-x^2)
"""

import numpy as np
from Integrator import Midpoint
import pandas as pd

def f(x):
    return np.exp(-1 * x**2)

def T(n, L):
    """
    Calculates the integral of f above from 0 to L
    with n trapazoids.
    """
    a = 0
    b = L
    mid_int = Midpoint(a, b, n)
    return mid_int.integrate(f)

def T_dataframe(n, L):
    """
    Calculates the integral of f above from 0 to every value in
    the array_like L every value in n for the number of approximations.
    Outputs a pandas DataFrame.
    """
    data = np.zeros((len(L),len(n)))
    for i in xrange(len(L)):
        for j in xrange(len(n)):
            data[i][j] = T(n[j], L[i])
    df = pd.DataFrame(data)
    df.index = ["L = " + str(i) for i in L]
    df.columns = ["n = " + str(i) for i in n]
    return df

def T_dataframe_error(n, L):
    """
    Calculates the difference in sqrt(pi) and the integral of f above from 0 to every value in
    the array_like L every value in n for the number of approximations.
    Outputs a pandas DataFrame.
    """
    data = np.zeros((len(L),len(n)))
    for i in xrange(len(L)):
        for j in xrange(len(n)):
            data[i][j] = .5 * np.pi**.5 - T(n[j], L[i])
    df = pd.DataFrame(data)
    df.index = ["L = " + str(i) for i in L]
    df.columns = ["n = " + str(i) for i in n]
    return df