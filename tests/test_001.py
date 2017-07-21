import unittest
from euler001 import sum_all_multiples

class SumMultiplesTest(unittest.TestCase):


	def test_10(self):

		result = sum_all_multiples(below=10)
		expected = 23

		self.assertEqual(result, expected)



if __name__ == '__main__':

	unittest.main()
