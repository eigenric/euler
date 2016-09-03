# -*- coding: utf-8 -*-
# author: Ricardo Ruiz

is_divisible = lambda a,b: not a % b

def is_prime(number):

	if number == 2: return True
	if number == 0 or number == 1: return False

	for x in xrange(2, number):
		if is_divisible(number, x): return False
	return True
		
def factorize(number):

	if is_prime(number): return [1, number]

	factors = []
	
	for prime in (prime for prime in xrange(2, number) if is_prime(prime)):
		if number == 1: break
		if not is_divisible(number, prime): continue

		factors.append(prime)
		while is_divisible(number, prime):
			number /= prime
	return factors

def largest_prime_factor(number):

	return max(factorize(number))


if __name__ == '__main__':

	number = 600851475143
	factors = factorize(number)

	print("Los factores primos de {} son {}".format(number,factors))
	print("Y obviamente el mayor es {}".format(max(factors)))
