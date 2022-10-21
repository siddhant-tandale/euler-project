# Value Definitions
numbers = range(0, 1000)
sum_number = 0

# Sum Loop
for number in numbers:
    if number%3 == 0 or number%5 == 0:
        sum_number += number

# Output   
print(sum_number)

