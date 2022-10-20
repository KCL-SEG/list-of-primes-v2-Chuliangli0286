"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    if number == 2:
        return True
    else:
        for i in range(2, number//2 + 1):
            if number % i == 0:
                return False
        return True

def primes(n):
    i = 2
    list = []
    if n <= 0:
        raise ValueError
    else:
        while True:
            if isPrime(i):
                list.append(i)
                if len(list) == n:
                    break
            i = i + 1

    return(list)
