# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the n-th prime number?

# Inputs
# 2
# 3
# 6

# Outputs
# 5
# 13

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(input(''))) # Get n

# We will hold on to a list of primes so we don't require recalculation between tests
# We will seed this list with the first two primes, 2 and 3
primes = []
primes.append(2)
primes.append(3)
    
for n in ns:
    # If we don't already have n primes in our list, calculate more until we reach n
    # Start with the last prime + 2 since all primes after 2 will be odd
    currentTestPrime = primes[-1] + 2
    while len(primes) < n:
        # We will first assume it is prime the try to divide by all lower primes
        isPrime = True
        for prime in primes:
            if currentTestPrime % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(currentTestPrime)
        # Add 2 to go to the next odd number
        currentTestPrime = currentTestPrime + 2
    # Print the answer
    print primes[n-1]