# -*- coding: utf-8 -*-
# author: Ricardo Ruiz


#	If we list all the natural numbers below 10 that are 
#	multiples of 3 or 5, we get 3, 5, 6 and 9.	
#	The sum of these multiples is 23.
#	Find the sum of all the multiples of 3 or 5 below 1000.


is_divisible = lambda a,b: (a % b) == 0

def is_multiple(a, *numbers):
	"""Return true if a is multiple of at last one of the numbers tuple"""

	for num in numbers:
		if is_divisible(a, num):
			return True


def sum_all_multiples(of=[3,5], below=1000):
	"""Return the sum of all the multiples of *of* below *below"""

	naturals_below = range(1, below)
	multiples = [num for num in naturals_below if is_multiple(num, *of)]
	
	return sum(multiples)

def main():

	result = sum_all_multiples()
	print(result)



if __name__ == '__main__':

	main()
