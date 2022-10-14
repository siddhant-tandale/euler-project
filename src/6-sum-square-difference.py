num_input = 100
sum1 = 0
sum2 = ((num_input+1)*(num_input/2))**2

for number in range(1, num_input+1):
  number = number**2
  sum1 += number
  
print(sum2-sum1)
