# Value Definitions
max_num = 20
numbers = list(range(2, max_num+1))
answer = 1
lcm_dict = {}

# Loop to make a dictionary
for i in range(1, max_num+1):
    lcm_dict[i] = 0

# Main Loop
for number in numbers:

    # Loop to find prime factors
    factors = []
    while number != 1:
        x = 2
        while number%x != 0:
            x += 1
    
        factors.append(x)
        number = number/x
    
    # Loop to count and replace the number of occurences
    for i in range(2, max_num+1):
        count = factors.count(i)
        lcm_dict[i] = max(lcm_dict[i], count)

# Loop to multiply all numbers and get the answer
for i in range(1, max_num+1):
    answer *= i**lcm_dict[i]

print(f'\n{answer}')
