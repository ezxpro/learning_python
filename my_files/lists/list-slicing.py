my_list = []

for i in range(10):
    my_list.append("bla bla bla " + str(i))

print("Simple slicing [0:5]")
print(my_list[0:5]) #prints index 0 until 4 (gets elements < than final step)

print("Omitting Initial part picks index 0 as start [:5]")
print(my_list[:5]) # omitting initial gets index 0 as start

print("Omitting end picks all elements remaining [0:]")
print(my_list[0:]) # end picks all items till end of the my_list

print("Changing step size to pick only pair indexes [::2)")
print(my_list[::2])

print("Same but now pick only odd indexes [::1)")
print(my_list[::1])

print("negative step goes backwards through the my_list [::-1)")
print(my_list[::-1])

# populate my_list with the output of range()
my_list = list(range(100))
