#we have already used functions like print() and input()
#if we want to make our own function (custom or defined), we can define or create a template for it
#in python we call these defined functions

#lets take a look at how a functions works from an intro standpoint
#functions can be defined in several ways
#functions in math take a series of inputs, process/calculate, and then produces an output
#functions in programming - a series of statements that can be called with a keyword, CAN take input, process data, and return output into another variable function or be void

#the following are examples of ways you can use a function
#characteristic 1 - a function can just be a series of statements tied to a keyword you make
#there is no return value, we call this a void function
#it just runs a series of statements
#to define a function we just say def function_name()

#void function with just a series of statements
#all indented code below the function is part of the function block (code that runs when function is called)

# def happy_birthday():
#     print("Happy Birthday to You")
#     print("Happy Birthday to You")
#     print("Happy Birthday to You, Dear Person")
#     print("Happy Birthday to You")

# #call the function using its name - run the function
# happy_birthday()

# #function are repeatable
# happy_birthday()

#the power of functions become apparent when we us parameters
#we often use functions so we can pass data to it (or give it input data like in a math function)
#parameters - varaibles or named data that are passed to a function
#parameters are treated like placeholders for incoming data

#parameters are just an argument that we have not used yet and are defined when creating a function
#reminder - arguments are what we use when calling/running a function, parameters are placeholders for defined functions.  These terms are often interchangable

#print("Hello") - "Hello" is the argument or data we are passing to print
#syntax - def function_name(parameter)
#parameters are placed inside the parenthesis of a defined function
#passing data - give the function som outside data to process
#we can pass any data type we want to the function including lists and dicts
#in python we can also pass data from one function to another.  This is known as higher order functions or functions as first class citizens (chaining functions)

#change happy_birthday to instead of saying dear person, we use a parameter

def happy_birthday(name):
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday to You, Dear", name) #name was used as a placeholder to then be set in the body of the function when ran
    print("Happy Birthday to You")

myname = input("Give me your name ")

#your arguments variable name does not have to match your parameter name
happy_birthday(myname)
#we can use raw values as well as other values in our function call
happy_birthday("Tim")

#we can also use parameters in calculations
def double_number(mynumber):
    doubled_number = mynumber * 2
    print(doubled_number)

# #when using calcs, make sure it gets the right data type
my_number = float(input("Please enter your number to be doubled "))
double_number(my_number)
double_number(20)


