# author: Ricardo Ruiz

"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def is_divisible(a, b):
    return not a % b


def is_prime(number):
    if number == 2:
        return True
    if number == 0 or number == 1:
        return False

    for x in range(2, number):
            if is_divisible(number, x):
                return False
    return True


def factorize(number):
    if is_prime(number):
        return [1, number]

    factors = []
    primes = (p for p in range(2, number) if is_prime(p))

    for prime in primes:
            if number == 1:
                break
            if not is_divisible(number, prime):
                continue

            factors.append(prime)
            while is_divisible(number, prime):
                    number /= prime
    return factors


def largest_prime_factor(number):
    return max(factorize(number))


if __name__ == '__main__':

    number = 600851475143
    print(max(factorize(number)))
