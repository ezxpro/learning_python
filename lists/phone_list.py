from random import shuffle
from secrets import randbelow, choice
from string import ascii_letters
# I'll create a phone list to store 20 numbers
# they'll be in the format xxx-xxx-xxxx. I'll 
# use an RNG to generate the numbers then I'll 
# add some gibberish text to the list and shuffle it

# FUNCTION DEFINITIONS
def p_list_gen(n):
    '''Generates a list of n phone numbers in the xxx-xxx-xxxx format'''
    a, b, c = 0, 0, 0 # the three parts of my phone number, 
    i = 0
    p_list = []
    while i < n:
        a = randbelow(1000)
        b = randbelow(1000)
        c = randbelow(10000)
        if a > 99 and b > 99 and c > 999:
            p_list.append(f'{a}-{b}-{c}')
            i = i + 1
    del i, a, b, c, n
    return p_list

def gen_rand_str():
    '''generates a random string of letters with up to 20 letters'''
    str = ""
    size = randbelow(20)
    for i in range(size):
        str += choice(ascii_letters)
    return str

# MY CODE STARTS HERE
phone_list = p_list_gen(20)

# now let's add some gibberish to the list, then shuffle it
for i in range(20):
    phone_list.append(gen_rand_str())

shuffle(phone_list)




found = []
'''for i in phone_list:
    if text in i:
        found.append(i)
'''