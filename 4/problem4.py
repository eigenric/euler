# -*- coding: utf-8 -*-
# author: Ricardo Ruiz

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
