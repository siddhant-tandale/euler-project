# Value Definitions
num_input = 100
sum1 = 0

# Calculation of sum of all numbes squared
sum2 = ((num_input+1)*(num_input/2))**2

# Loop to calcualte and add the square of each number
for number in range(1, num_input+1):
  number = number**2
  sum1 += number

# Output
print(sum2-sum1)
