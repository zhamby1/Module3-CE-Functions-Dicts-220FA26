#functions can also return values into another variable or fucntion
#these are called return functions
#to use a return function, we just use the keyword return and then the value we wish to return
#note that python still allows for multiple return of values..would not recommend
def add_total(num1,num2):
    sum = num1 + num2
    return sum

#in a return function we need a variable or other function to return into 
total = add_total(5,10)
print(total)
#in python we can also return into a function
print(add_total(7,6))

#another cool use of this in python is for using the vlaues in other functions for arguments in functions
#i.e. chaining functions together
#terminating function / outer function
def add_tax(total):
    tax = total * 0.06
    total_with_tax = total + tax
    print(total_with_tax)

add_tax(add_total(10,20))

#return statement also has an additional use in that it can exit a function when used
#this can be good with if statments and exiting the function before data is processed

def tell_age(name, age):
    if age <= 0:
        print("You cannot be negative years old")
        return
    else:
        name_and_age = f"Your name is {name} and your age is {age}"
        return name_and_age


nage = tell_age("Zach", 41)
print(nage)