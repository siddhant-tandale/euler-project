# Value Definitions
term = 10001
number = 1
counter = 1

# Main Loop
while counter <= term:
    prime = True
    
    # Prime Number Loop
    for x in range(3, int((number**(1/2)) + 1)):
        if number % x == 0: 
            prime = False
            break
        
    if prime:
        counter += 1

    number += 2

#Output
number -= 2
print(number)

