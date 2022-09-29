# list comprehension is a way of creating multidimensional arrays
# without having to write multiple 'for' loops. 
my_list = [[f'Number {i}' for i in range(5)] for x in range(2)]

print(my_list)

# basically, the list resulting from the inner square brackets 
# becomes an element of the outer list 
