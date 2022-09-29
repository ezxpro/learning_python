from hashlib import new


my_string = "My dog is alive and well. His name is totó"
my_string.split(".")
#print(my_string)


def clean_word(word):
    return word.replace(".", "").lower()

new_list = [clean_word(word) for word in my_string.split()]
print(new_list)