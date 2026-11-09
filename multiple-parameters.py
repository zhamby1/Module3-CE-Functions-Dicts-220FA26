#multiple parameters are often the norm in python
#multiple parameters are just separated out by a comma
#lets make a function that can add two numbers together
def add_numbers(num1,num2):
    sum = num1 + num2
    print(sum)

add_numbers(10,20)

#multiple parameters...order matters
def subtract_numbers(num1,num2):
    difference = num1 - num2
    print(difference)

#different results
subtract_numbers(10,5)
subtract_numbers(5,10)