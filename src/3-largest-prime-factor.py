# Value Definitions
num_input = 600851475143
number = num_input
factors = []

# Prime Factor Loop
while number != 1:
    x = 2
    while number%x != 0:
        x += 1
    
    factors.append(x)
    number = number/x
    
# Output
print(max(factors))

