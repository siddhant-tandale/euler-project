max_num = 20
numbers = list(range(2, max_num+1))
answer = 1
lcm_dict = {}

for i in range(1, max_num+1):
    lcm_dict[i] = 0


for number in numbers:

    factors = []
    while number != 1:
        x = 2
        while number%x != 0:
            x += 1
    
        factors.append(x)
        number = number/x
        
    key = 1
    count = 1
    for f in factors:
        if key != f:
            lcm_dict[key] = max(lcm_dict[key], count)
            key = f
            count = 1
        else:
            count += 1

    lcm_dict[key] = max(lcm_dict[key], count)

for i in range(1, max_num+1):
    answer *= i**lcm_dict[i]

print(answer)

