groceries = ["bananas","apples","bread"]

#sorting - asc or desc and we use .sort
groceries.sort()
print(groceries)
groceries.sort(reverse=True)
print(groceries)

#print the length or how many elements/items are in a list we can the len function
print(len(groceries))

#when using a normal for in loop we can preview a change in the data but not actually change whats inside
test_scores = [90,85,95,67,32,80]
#I want to add 5 pts to each test score
for test_score in test_scores:
    test_score = test_score + 5
    print(test_score)

#but you can see the actual values did not change inside of the lest
print(test_scores)

#there are two solutions if you want to modify multiple data values in a list
#one way is to create a new list and append the new data values to it

test_scores_updated = []
for test_score in test_scores:
    test_score = test_score + 5
    test_scores_updated.append(test_score)

print(test_scores_updated)

#you can modify the original list, but to do this we need to use an iterator value or a loop variable
#the reason we have to do this is we need to directly access the index to change the value of an item in a list
#this is similar to how a traditional for loop works in other languages to update data
for i in range(len(test_scores)):
    test_scores[i] = test_scores[i] + 5

print(test_scores)