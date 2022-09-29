my_list = list(range(10))
print("Created a list " + str(my_list))

# append data to lists (item goes in the end)
my_list.append(10)
print("Append value 10 to the list" + str(my_list))


# to add data to any position, use insert(index, item)
my_list.insert(0, -1)
print("using insert() function to" + 
" add negative numbers at index 0")

# insert negative integers down to -10 
for i in range(2, 10):
    my_list.insert(0, i - (i * 2))
    #interesting to notice that range() doesn't
    # pick the last index specified
print("Insert negative numbers down to -10")

# Removing an item, just need to pass the value
my_list.remove(5) 
print("use remove() to remove value '5'")
# it only removes one instance of that value though

# pop() is the opposed of append, it "pops" last item off
my_list.pop()
print("Pop element from the list")

print("Now pop all elements from the list: ")
while(len(my_list)):
    my_list.pop()

print(my_list)

