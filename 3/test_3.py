import unittest

from problem3 import is_prime, factorize, largest_prime_factor

class LargestPrimeFactorTest(unittest.TestCase):

	def test_is_prime(self):
	
		some_primes = [2,3,5,7,13,17,23]
		result = map(is_prime, some_primes)

		self.assertTrue(result)

	def test_not_prime(self):

		some_not_primes = [4,6,36,49]
		result = all(map(is_prime, some_not_primes))

		self.assertFalse(result)

	def test_factorize(self):

		factorized_numbers = {36: [2,3], 240: [2,3,5], 394: [2,197], 13195: [5,7,13,29]}

		for number, prime_factors in factorized_numbers.items():

			self.assertItemsEqual(factorize(number), prime_factors)

	def test_some_numbers(self):

		result = largest_prime_factor(13195)
		expected = 29

		self.assertEqual(result, expected)


if __name__ == '__main__':

	unittest.main()
		
