# -*- coding: utf-8 -*-
# author: Ricardo Ruiz

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def is_prime(number):

	if number == 2: return True
	for x in range(2, number):
		if not number % x: return False
	return True

def primes():
	pass

def factorize(number):
	pass

def largest_prime_factor(number):
	pass


if __name__ == '__main__':

	main()
