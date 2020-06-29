# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers that is less than n where n is a 6 digit number.

# Inputs
# 2
# 101110
# 800000

# Outputs
# 101101
# 793397

# This function checks if i has 2 3-digit factors
def has3DigitFactors(i):
    # Start with the first 3 digit number as a possible factor
    # We can skip 100 because any multiple would end in 00 and our palindrome can't start with 00
    factorA = 101
    # Then we iterate through 3 digit numbers
    while factorA < 1000:
        # If a is a 3 digit factor:
        if i % factorA == 0:
            # See if it divides out leaving another 3 digit factor, b
            factorB = i / factorA
            if factorB > 100 and factorB < 1000:
                return True
        factorA = factorA + 1
    return False

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(input(''))) # Get n

for n in ns:
     # First 3 characters of n
    firstHalfN = int(str(n)[0:3])
    # Ensure n is 3 digits
    while firstHalfN > 99: 
        # Make a palindrome of firstHalfN + inverse firstHalfN
        nPalindrome = int(str(firstHalfN) + str(firstHalfN)[::-1])
        # Make sure our palindrome is less than or equal our starting number, otherwise subtract and try again
        if nPalindrome > n:
            firstHalfN = firstHalfN - 1 
            continue
        # If it has 2 3-digit factors, print it and break the loop
        if has3DigitFactors(nPalindrome):
            print nPalindrome
            break
        firstHalfN = firstHalfN - 1 
