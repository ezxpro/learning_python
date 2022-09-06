from secrets import randbelow

phone_list = []
j = 0
#for i in range(20):
area, prefix, suffix = 0, 0, 0
a = area <= 99
b = prefix <= 99
c = suffix <= 999


while a and b and c:
    j = j + 1
    print(f'booleans {a} {b} {c}')
    area = randbelow(1000)
    print(f"we are in subloop {j}")
    prefix = randbelow(1000)
    suffix = randbelow(10000)
    print(f'\n area = {area}\n prefix = {prefix}\n suffix = {suffix}\n')
    lixo = input("digite algo para continuar: ")
    phone_list.append(f'{area}-{prefix}-{suffix}')  
#now append number to list
    
del i

'''for i in phone_list:
    print(i)'''