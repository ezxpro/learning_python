from secrets import randbelow

my_number = randbelow(700)

if (my_number % 2 == 0):
    print("my numberis pair")
else:
    print("my number is odd")

print("Now, let's check the range to which this" +
"number belongs")

if(my_number < 120):
    print("It's less than 120")
elif( my_number < 350 ):
    print("it's between 120 and 350")
else:
    print("it's equal or greater than 350.")

print(f"My number is: {my_number}")

    
