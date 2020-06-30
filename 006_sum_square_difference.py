# Problem 6
# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

# Inputs
# 2
# 3
# 10

# Outputs
# 22
# 2640

# This is the same sigma method from problem 001. It calculates the total of all numbers from 1 to n
def sigma(n):
    return int((n + 1) * n / 2)

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(raw_input(''))) # Get n

for n in ns:
	# Numbers squared and then summed are also known as pyramid numbers
	# This would be the number of blocks needed to build a square pyramid with the bottom length n
	# There is a known formula for pyramid numbers as n^3/3 + n^2/2 + n/6
	# Each part can be fractional so we will use floating points but the result will be a natural number +- floating point error
    squaresSummed = long(n**3.0/3.0 + n**2/2.0 + n/6.0)
    # Calculate the sum of numbers 1 to n using Sigma() and square it
    sumSquared = sigma(n)**2
    # Calculate and print the difference
    print sumSquared-squaresSummed