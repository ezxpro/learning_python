from secrets import randbelow

phone_list = []
j = 0

area, prefix, suffix = 0, 0, 0

for i in range(20):
    while True:
        j = j + 1
        area = randbelow(1000)
        prefix = randbelow(1000)
        suffix = randbelow(10000)
        if area > 99 and prefix > 99 and suffix > 999:
            phone_list.append(f'{area}-{prefix}-{suffix}')
            break
        

for i in phone_list:
    print(i)