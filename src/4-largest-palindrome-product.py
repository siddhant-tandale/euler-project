# Value Definitions
palin_num = 0

# Main Loop
for number1 in range(999, 100, -1):

    # First Number Calculation
    for number2 in range(number1, 100, -1):
        product = number1*number2
        prod_str = str(product) 
        
        # Second Number Calculation
        palindrome = True
        for i in range(len(prod_str)):
            if prod_str[i] != prod_str[-(i+1)]:
                palindrome = False
                break

        if palindrome and product > palin_num:
            palin_num = product

# Output
print(palin_num)

