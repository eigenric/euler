# author: Ricardo Ruiz

"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_all_multiples(of=[3, 5], below=1000):
    """Return the sum of all the multiples of=[3,5], below=[1000]"""
    return sum(num for num in range(1, below)
               if any(not num % div for div in of))


if __name__ == '__main__':
    print(sum_all_multiples())
