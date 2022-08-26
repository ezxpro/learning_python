my_list = list(range(10))
print("This is my list: \n" + str(my_list) + "\n")

my_list_2x = [2 * item for item in my_list]

print("\nThis is it after list comprehension 2x multi"+
"plication: \n" + str(my_list_2x) + "\n")