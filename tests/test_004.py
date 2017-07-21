import unittest

from euler004 import is_palindrome, largest_palindrome_product

class LargestPalindromeProductTest(unittest.TestCase):

    def test_is_palindrome(self):

        palindromes = [101, 42324, 9009, 2002]

        for palindrome in palindromes:
            self.assertTrue(is_palindrome(palindrome))

    def test_largest_palindrome_product(self):

        result = largest_palindrome_product(2)
        expected = 9009

        self.assertEqual(result, expected)


if __name__ == '__main__':

    unittest.main()

