"""
Jonathan Argueta-Herrera
Module 13: 8.1 Generator Assignment
"""

from math import sqrt


# function that outputs fibonacci numbers
def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


# function to determine if number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True


# create list to store numbers
fib_primes = []

# creates intance of fibonacci function
fibonacci = fibonacci_generator()

# find the first 4 Fibonacci primes
while len(fib_primes) < 4:
    fib_number = next(fibonacci)  # call to get the next Fibonacci number
    if is_prime(fib_number):  # check if number prime
        fib_primes.append(fib_number)  # adds number to fib_primes list

print(fib_primes)

# find the next 4 Fibonacci primes
while len(fib_primes) < 8:
    fib_number = next(fibonacci)
    if is_prime(fib_number):
        fib_primes.append(fib_number)

print(fib_primes)

# find the next 3 Fibonacci primes
while len(fib_primes) < 11:
    fib_number = next(fibonacci)
    if is_prime(fib_number):
        fib_primes.append(fib_number)

print(fib_primes)
# output:
# [2, 3, 5, 13]
# [2, 3, 5, 13, 89, 233, 1597, 28657]
# [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073]
