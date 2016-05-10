#! /usr/bin/env python
"""
File: interpolate_exp_cos.py

Copyright (c) 2016 Michael Seaman

License: MIT

Description: Creates a linear interpolation function to evaluate
f = exp(-x^2) * cos(2pi x) for different numbers of interpolation 
points q and for x = -.45
"""

import numpy as np
from calculus import discrete_func

def f(x):
    return np.exp(-1 * x**2) * np.cos(2* np.pi * x)

def interpolate(x, given_x_values, given_y_values):
    """
    Returns the linearly approximated value at x of a function who's
    discrete values are given by 'given_y_values' at x values given by
    'given_x_values'. The given values for x must be in increasing order
    and must corespond with the y values.
    """
    k = np.argmax(given_x_values>x) - 1
    slope = (given_y_values[k + 1] - given_y_values[k])/float(given_x_values[k + 1] - given_x_values[k])
    return given_y_values[k] + slope*(x - given_x_values[k])

def interpolate_with_exact(x, f, a, b, n):
    """
    Returns a approximation of f(x) with n interpolation points from
    a to b. Then returns the actual value of f evaluated at x.
    """
    x_list = discrete_func(f, a, b, n)[0]
    y_list = discrete_func(f, a, b, n)[1]
    interpolated_value = interpolate(x, x_list, y_list)
    actual_value = f(x)
    return interpolated_value, actual_value

def test_interpolate_on_given_value():
    """
    Asserts that the interpolation model should perfectly model the
    function when given a value it was trained on - making the term
    (x - given_x_values[k]) go to zero.
    """
    a = -10
    b = 10
    n = 1000
    xL = np.linspace(a, b, n+1)
    yL = np.sin(xL)
    random_index = np.random.randint(n)
    assert interpolate(xL[random_index], xL, yL) == yL[random_index]
    