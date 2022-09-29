# Simple operations on dictionary = creation, measuring length
# searching for presence or absense of an element
from tkinter import N


neighbors = {'John': 'Mason', 'Alex': 'Nurse', 'Linda':'Professor'}

# print dictionary length and its keys
print("Length of dictionary is = " + str(len(neighbors)) )
print("Dictionary entries are:")
for i in neighbors:
    print(i)

# print key definitions
print('\nTheir respective professions are:')
for i in neighbors:
    print(neighbors[i])

print("\n\n")

# delete last key  from dictionary

del(neighbors['Alex'])

#print new length and dictionary key values
print("New length is = " + str(len(neighbors)) )

# print new dictionary length and its keys
for i in neighbors:
    print(i)

# print key definitions
print('\nTheir respective professions are:')
for i in neighbors:
    print(neighbors[i])

#search key in dictionary
print("Is \"Margareth\" a neighbor?") 
print('Margareth' in neighbors)#returns false
print("Is \"John\" a neighbor?") 
print('John' in neighbors)#returns false
# the bottom line in the above example is:
# it appears this looks for a substring

#search definition in dictionary
for i in neighbors:
    if('Mason' in neighbors[i]):
        print(i + " is a mason")