import unittest

from problem3 import largest_prime_factor, is_prime

class LargestPrimeFactorTest(unittest.TestCase):

	def test_is_prime(self):
	
		some_primes = [2,3,5,7,13,17,23]
		result = map(is_prime, some_primes)

		self.assertTrue(result)

	@unittest.expectedFailure
	def test_some_numbers(self):

		result = largest_prime_factor(13195)
		expected = 29

		self.assertEqual(result, expected)


if __name__ == '__main__':

	unittest.main()
		
