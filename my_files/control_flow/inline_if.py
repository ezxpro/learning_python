from secrets import randbelow

my_number = randbelow(700)

print("too small" if my_number < 300 else  f"great enough, number is {my_number}") 
print("Now, let's do the opposite!")

# assign this to a variable using a ternary operator
result = f"small enough, number is {my_number}" if my_number < 300 else "too great"
print(result)