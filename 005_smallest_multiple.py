# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

# Inputs
# 2
# 3
# 10

# Outputs
# 6
# 2520

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(input(''))) # Get n

for n in ns:
    # To find the smallest number divisible by 1 to n, we need to find a list of prime factors of numbers 1 to n and multiply them together
    # Test each number below n and if it is prime, add it to the list
    # If it's not prime, we may still need to add additional copies of primes
    # E.g. i = 4 needs a second 2 because 4's prime factors are 2 instances of 2
    primes = []
    for i in range(2, n + 1):
        # First, divide out any primes currently in the list
        quotient = i
        for prime in primes:
            if quotient % prime == 0:
                quotient = quotient / prime
        # We divided out everything so now we should be left with either 1 (if all factors are already on the list) or a prime number
        # It may be a duplicate prime number such as if 4 divided by 2 left us with 2 but that is needed anyway as stated above
        if quotient != 1:
            primes.append(quotient)
                                    
    # Now that we made our list of factors, multiply them all together for the answer
    smallestMultiple = 1
    for prime in primes:
        smallestMultiple = smallestMultiple * prime
    print smallestMultiple