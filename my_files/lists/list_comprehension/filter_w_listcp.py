my_list = list(range(100))


filtered_list = [item for item in my_list if item % 2 == 0 and item <= 20]

print(filtered_list)