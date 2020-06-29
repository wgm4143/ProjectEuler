# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number n?

# Inputs
# 2
# 10
# 17

# Outputs
# 5
# 17

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(input(''))) # Get n

for n in ns:
    largestPrime = 1
    # Start with first 'prime' to test, 2
    prime = 2 
    # Loop through 'primes' until the p we are testing is greater than the square root of n
    # When p^2 is greater than n, it is no longer a possible factor
    # This is because the root of n is the upper limit of its factors as shown by perfect squares
    # E.g. 7 is the largest factor of 49
    while prime * prime <= n: 
        if n % prime == 0: # If it is a factor (has no remainder)
            largestPrime = prime
            while n % prime == 0: # Divide out the factor then set n to the quotient
                n = n / prime
        # Loop through our 'primes', just 2 plus odd numbers: 2,3,5,7,9,11...
        # This is not the most performant due to it testing against odd non primes (9,15...)
        if prime == 2:
            prime = 3
        else:
            prime = prime + 2
    # Since we divided out all numbers less than the root,
    # Anything left in n must be a prime itself
    if n != 1:
        print n
    # Otherwise, n is 1 meaning we divided out a prime so print the largest prime we found
    else:
        print largestPrime