#for additional dictionary methods/functions - https://www.youtube.com/watch?v=MZZSMaEAC2g

#dictionaries are key-value pairs that associate a name(key) with a value
#python treats dictionaries like objects or maps
#objects are containers that have properties(characteristics) that describe an item or an object (singular)
#objects have properties that when assigned a value describe that part of the object

#Person - name,age
#Car - make,model,year

#maps are usually similar to associative in arrays in that they have a list of things that have something in common, but use key names instead of index
#like a dictionary - terms and definitions

#dictionaries in python are flexible because we can describe them as objects or list a list of terms and definitions (map)
#the syntax for both is the same, we just differ on its use

#first lets use a dictionary like an associative array / map (keys will be names of people)
#so lets make a dictionary with a list of people and their bank balances

#syntax for dict -  name_of_dict = {"key" : value}
bank_customers = {
    "Alice" : 500.00,
    "Tim" : 100.00,
    "Zach" : 300.00
}

# #we can grab individual items out of a dictionary by using a key instead of index
# print(bank_customers["Alice"])

# #if we want to display all items in a dict we can still use a for in loop
# #we instead say name_that_represents_key in dict_name
# for name in bank_customers:
#     print(name, ":", bank_customers[name])

# #we can also use dict like objects and describe properties about one item
# #often times we organize it this way so we can use keys as fields with values
# #this is an example of organizing a dict like an object
# person_zach = {
#     "name" : "Zach",
#     "age" : 41,
#     "city" : "Indy"
# }

# for detail in person_zach:
#     print(detail, ":", person_zach[detail])

#dict are mutable and can be changed
#if you want to add data all you have to is add a new keyname with a value
#keys must be always be unique
#name_of_dict[new_key_name] = value
bank_customers["Jimmy"] = 1000.00
#debug
print(bank_customers)

#modify an existing - use key name that is already established = value
bank_customers["Zach"] = 8000.00
print(bank_customers)

#we can also search or 'get' a single value using the get function with a key name
alice_balance = bank_customers.get("Alice")
print(alice_balance)

#delete items from diction with del keyword
del bank_customers["Alice"]
print(bank_customers)

#we can also do a traditional serach liek with our lists using the in keyword
#we will be searching by keynames
key = "Jonas"
if key in bank_customers:
    print(key, "is in the dictionary")
else:
    print("Customer not found")

#maybe we want to search for a key and a value

find_name = "Tim"
find_value = 100.00

#we have a loop
#for name_represent key, name_represents_value in dictionary_name.items()
for name,balance in bank_customers.items():
    if name == find_name and balance == find_value:
        print("Found name and value")
        break
    else:
        print("Not Found")