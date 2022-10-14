num_input = 600851475143
number = num_input
factors = []

while number != 1:
  x = 2
  while number%x != 0:
    x += 1

  factors.append(x)
  number = number/x


print(f'The largest prime factor of {num_input} is {max(factors)}')