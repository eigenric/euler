import unittest

from problem2 import sum_all_fib_even_numbers, fibonacci, nearest

class FibonnaciTest(unittest.TestCase):

	def test_fibonacci(self):

		self.assertEqual(fibonacci(10), 55)

	def test_nearest_34(self):

		self.assertEqual(nearest(34), 9)

	def test_nearest_100(self):

		self.assertEqual(nearest(100), 11)

	def test_sum_100(self):

		result = sum_all_fib_even_numbers(limit=100)
		expected = 2 + 8 + 34

		self.assertEqual(result, expected)

	def test_sum_144(self):

		result = sum_all_fib_even_numbers(limit=144)
			
		expected = 2 + 8 + 34 + 144

		self.assertEqual(result, expected)


if __name__ == '__main__':

	unittest.main()
		
