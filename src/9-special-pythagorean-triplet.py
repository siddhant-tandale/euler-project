# Value Definitions
sum = 1000

# Main Loop 
for a in range(1, sum-2):
    for b in range(1, sum-a-1):
        c = sum - a - b
        if a**2+b**2==c**2:
            break
    if a**2+b**2==c**2:
        break

# Output
print(a*b*c)

