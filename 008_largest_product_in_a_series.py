# Problem 8
# Look at the following 5000 digit number:
# 82166370484403199890008895243450658541227588666881
# The four adjacent digits that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# Find the k adjacent digits in the n digit number that have the greatest product. What is the value of this product?

# Inputs
# 2
# 10 5
# 3675356291
# 10 5
# 2709360626

# Outputs
# 3150
# 0

t = input('') # Get number of tests
ns = []
for i in range(t):
    d,k = str(raw_input('')).split(' ') # Get d, k, and n
    n = raw_input()
    ns.append((int(d),int(k),n))

for n in ns:
    d = n[0]
    k = n[1]
    n = n[2]
    maxProduct = 0
    for i in range(d - k + 1):
        # Use a sliding window of k digits
        kDigits = n[i:i+k]
        product = 1
        # Multiply those digits together
        for digit in kDigits:
            product = product * int(digit)
        # Compare this window to our running max product
        maxProduct = max(maxProduct, product)
    print maxProduct