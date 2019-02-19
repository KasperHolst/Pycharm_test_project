# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:07:29 2018

@author: B044931
"""

def is_prime(number):
    """Return True if `number` is prime."""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True
