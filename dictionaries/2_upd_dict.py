#Here we'll do:
# 1. initialize dictionary
# 2. Add a couple of key & value pairs to the dictionary
# 3. Print out the dictionary
# 4. Update the dictionary
# 5. Print it out again

# initialization
d = {}

# add some key value pairs
d[1] = 10
d['hello'] = 'world' # notice how position doesn't matter
d['list'] = [1,2,3,4]

# print the dictionary out
print(d)

# update the key '1'
d[1] = 100

# print the dictionary out, once again
print(d)