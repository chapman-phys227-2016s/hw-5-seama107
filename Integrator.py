#!\usr\bin\python
"""
File: Integrator.py

Copyright (c) 2016 Michael Seaman

License: MIT

A class for integration, to be used inherited by MCint_class.py
Stores the function to be differentiated, and the stepsize h for evaluation
"""

import numpy as np
from unittest import TestCase


class Integrator:
    """
    Super class that other integrating classes inherit from
    takes a and b as bounds and a number n of approximations
    """
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError("no rule in class %s" % self.__class__.__name__)

    def integrate(self, f):
        """
        Abstract - Implemented by it's children
        """
        raise NotImplementedError("no rule in class %s" % self.__class__.__name__)

    def integrate(self, f):
        """
        Sums up all the values of points to be evaluated by f(x) and their respective weights
        """
        s=0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

    def vectorized_integrate(self, f):
        """
        Sums up all the values of points to be evaluated by f(x) and their respective weights
        Uses numpy.dot instead of python looping
        """
        return np.dot(self.weights, f(self.points))


class Midpoint(Integrator):
    """
    Implements the construct_method method using the midpoint integration rule
    returns an array of n x values to be evaluated on f and an array of n weights
    all equal to h
    """
    def construct_method(self):
        a, b, n = self.a, self.b, self.n
        h = (b-a)/np.array(n).astype(float)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
    	return x, w

def linear_func(x):
	return 5.5*x - 22

def linear_func_integral(x):
	return 2.75 * x**2 - 22 * x


class Test_Integrator(TestCase):
    def test_midpoint_int(self):
        """
        Tests the midpoint integration method on a linear function. The linear
        function should be  perfectly integrated by the method for any 
        n, b or a
        """
        a, b = -3.5, 6.5
        m1 = Midpoint( a, b,10)
        m2 = Midpoint( a, b, 20)
        m3 = Midpoint( a, b, 100)
        exact_integral =  linear_func_integral(b) - linear_func_integral(a)
        assert (exact_integral == m1.vectorized_integrate(linear_func) and 
        	exact_integral == m2.vectorized_integrate(linear_func) and
        	exact_integral == m3.vectorized_integrate(linear_func))

