# Value Definitions
number1 = 0
number2 = 1
sum_number = 0

# While loop to calculate different fibonacci numbers and their total sum
while number2 < 4000000:
    number1, number2 = number2, number1+number2
    if number2%2 == 0:
        sum_number += number2

#Output
print(sum_number)
