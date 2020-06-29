# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers that is less than n.
# n > 1000000
# n < 1000000

# Inputs
# 2
# 101110
# 800000

# Outputs
# 101101
# 793397

def has3DigitFactors(np):
    a = 100
    while a < 1000:
        if np%a == 0:
            b = np/a
            if b>100 and b <1000:
                return True
        a = a + 1
    return False

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(input(''))) # Get n

for n in ns:
     # First 3 characters of n
    n1 = int(str(n)[0:3])
    # Ensure n is 3 digits
    while n1 > 99: 
        # Make a palindrome of n1 + inverse n1
        np = int(str(n1) + str(n1)[::-1])
        # Make sure our palindrome is less than or equal our starting number, otherwise subtract and try again
        if np > n:
            n1 = n1 - 1 
            continue
        # Start with the first 3 digit number as a possible factor
        # We can skip 100 because any multiple would end in 00 and our palindrome can't start with 00
        a = 101
        # Then we iterate through 3 digit numbers
        while a < 1000:
            # If a is a 3 digit factor:
            if np%a == 0:
                # See if it divides out to another 3 digit factor, b
                b = np/a
                if b>100 and b <1000:
                    # It does have a and b as 3 digit factors so print our palindrome
                    print np
                    # Reset n1 so we break out of this test of n
                    n1 = 99
                    break
            a = a+1
        n1 = n1 - 1 
