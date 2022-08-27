my_set = {"a", "b", "c"}

# I can also pass any iterable object to the set() constructor
my_set = set(list(range(10)))

# a nifty trick is to convert use this to deduplicate list elements
my_list = [1, 2, 3, 3, 3, 4, 5, 6, 7, 7]

my_list = list(set(my_list))
print(my_list)