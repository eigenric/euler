# -*- coding: utf-8 -*-
# author: Ricardo Ruiz


def sum_all_multiples(of=[3,5], below=1000):
	"""Return the sum of all the multiples of=[3,5], below=[1000]"""

	return sum(num for num in range(1, below) if any(not num % div for div in of))


if __name__ == '__main__':

	print(sum_all_multiples())

