#tuples are similar to lists, but they are immutable..think of it as a list of constants
#immutable means cant change after creating
#you use them we needing multiple values in a 'category' but do not what them changed or modified
#great for fixed choices
#the only way to 'change' a tuple is to make a new one and set old data to the new tuple

#to give another example of immutability - strings are technically immutable
#you either have to replace the whole string, and not individual characters
# name = "zach"
# name = "jach"    this is valid
# name[0] = "j"   cannot do

#tuples us () as the way to store items , tuplename = (items)
#almost everything else is similar to how we use lists
states = ("IN","IL","KY")

for state in states:
    print(state)

#search 
looking_for = input("Give me the abbreviation of the state your are looking for ")
found = looking_for in states
print(found)

#still grab individual items by index
print(states[0])

#only other things we can do is create tuples from other tuples
states2 = ("NY","FL","TX")
states3 = states + states2

#debug
print(states3)