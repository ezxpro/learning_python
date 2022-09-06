from secrets import randbelow

# I'll create a phone list to store 20 numbers
# they'll be in the format xxx-xxx-xxxx
# I'll use an RNG to generate the numbers


a, b, c = 0, 0, 0 # the three parts of my phone number, 

def p_list_gen(n):
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


print(len(p_list_gen(2)))

def p_list_add_gibberish(list, ):
    list.
found = []
'''for i in phone_list:
    if text in i:
        found.append(i)
'''