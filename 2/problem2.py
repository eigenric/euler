# -*- coding: utf-8 -*-
# author: Ricardo Ruiz

from math import sqrt

phi = ( 1 + sqrt(5) ) / 2.0

def fibonacci(n):
	"""Explicit formula for the n position
	of fibonnaci sequence"""
	
	result = int((phi**n - (phi-sqrt(5))**n) / sqrt(5))

	return result

def sum_all_fib_even_numbers(limit=4000000):
	"""Because the sum of two odd numbers is even,
	even numbers are in [3, 6, 9..] positions"""

	evens = xrange(3, 100, 3)

	return sum([fibonacci(even) for even in evens if fibonacci(even) <= limit])

if __name__ == '__main__':

	solution = sum_all_fib_even_numbers()
	print(solution)
