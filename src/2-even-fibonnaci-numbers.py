number1 = 0
number2 = 1
sum_number = 0

while number2 < 4000000:
    number1, number2 = number2, number1+number2
    if number2%2 == 0:
        sum_number += number2

print(sum_number)
