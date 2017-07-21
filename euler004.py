# author: Ricardo Ruiz

"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools

def is_palindrome(number):

	return str(number)[::-1] == str(number)

def largest_palindrome_product(digits):

	possible_products = itertools.product(range(1, 10**digits), repeat=2)

	largest = 0
	for a, b in possible_products:
		product = a * b

		if is_palindrome(product) and product > largest:
			largest = product

	return largest

if __name__ == '__main__':

	print(largest_palindrome_product(3))
