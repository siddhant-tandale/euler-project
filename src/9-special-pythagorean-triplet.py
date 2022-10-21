# Main Loop 
for a in range(1, 998):
    for b in range(1, 1000-a-1):
        c = 1000 - a - b
        if a**2+b**2==c**2:
            break
    if a**2+b**2==c**2:
        break

# Output
print(a*b*c)

