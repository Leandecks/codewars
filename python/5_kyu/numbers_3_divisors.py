# def solution(n, m):
#     return [number for number in range(n, m + 1) if len([divisor for divisor in range(2, number) if number % divisor == 0]) == 3]

# def solution(n, m):
#     divisors_3_numbers = []
#
#     for number in range(n, m + 1):
#         divisors = []
#
#         for divisor in range(2, number):
#             if number % divisor == 0:
#                 divisors.append(divisor)
#
#         print(number, divisors)
#
#         if len(divisors) == 3:
#             divisors_3_numbers.append(number)
#
#     return divisors_3_numbers

import math

def primes(n, m):
    primes = []

    for number in range(2, m + 1):

        isPrime = True

        for prime in primes:
            if number % prime == 0:
                isPrime = False

        if isPrime:
            primes.append(number)

    return [prime for prime in primes if n <= prime <= m]

def solution(n, m):
    return [x ** 4 for x in primes(round(math.sqrt(math.sqrt(n))), round(math.sqrt(math.sqrt(m)))) if n <= x ** 4 <= m]

print(solution(27302708673322, 86413072951064130123))
'''
[16, 81, 625, 2401, 14641, 28561, 83521]

2^4 = 16 = [2, 4, 8]
3^4 = 81 = [3, 9, 27]
5^4 = 625 = [5, 25, 125]
7^4 = 2401 = [7, 49, 343]
11^4 = 28561 = [11, 121, 1331]
13^4 = 83521 = [13, 169, 2197]
17^4 = 14641 = [17, 289, 4913]
'''