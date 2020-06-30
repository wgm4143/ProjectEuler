# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below n.

# Inputs
# 2
# 10
# 100

# Outputs
# 23
# 2318

# Sigma is like factorial but with addition instead of multiplication, i/e if n=100, return 5050 (100+99+98+...+2+1)
def sigma(n):
	# Let n =  100; for each outermost pair [(100,1),(99,2),(98,3)...(51,50)] they all add to 101 aka (n + 1) and they are pairs so there exist (n / 2) pairings
	# With this we can calculate without iterating as the total of the first group (n + 1) times the total number of groups (n / 2)
    return int((n + 1) * n / 2)

t = input('') # Get number of tests
ns = []
for i in range(t):
    ns.append(int(raw_input(''))) # Get n

for n in ns:
	# In the following section we must understand the following about sigma and multiples
	# Sum(1,2,3,4..) * x = sum(x,2x,3x,4x..) via the distributive property
	# So for the multiples of 7 below 98: 
	# Sigma(97//7) = 91 (97 because we want digits below 98 but sigma is inclusive)
	# And scale that by 7, 91*7 = 637
	# So sum(7,14,21...91) = 637
	# Thus sum(multiples of d < n) = sigma(n-1//d) * d

    sigmaThrees = sigma(int((n - 1) / 3)) * 3 # Get sum of multiples of 3, (3,6,9,12,15,18...)
    sigmaFives = sigma(int((n - 1) / 5)) * 5 # Get sum of multiples of 5, sum(5,10,15,20...)
    sigmaFifteens = sigma(int((n - 1) / 15)) * 15 # Get sum of multiples of 15, sum(15,30...)
    print sigmaThrees + sigmaFives - sigmaFifteens # Add sum of fives and sum of threes but subtrack 15s because those were counted twice