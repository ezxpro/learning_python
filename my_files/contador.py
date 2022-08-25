def fib(n):
    prev = 0
    curr = 1
    nxt = 0
    i = 1
    while(i <= n):
        prev = curr
        curr = nxt
        nxt = curr + prev
        #print(nxt)
        i = i + 1
    return nxt    
while(True):
    n = int(input("Type the nth term of the fibonnaci sequence to learn its value (or type or \"quit\" to exit:) "))
    print("The ",n,"th term of the fibonnaci sequence is: ", fib(n))
    if(n == "quit"):
        quit()
    
txt= input('')
    

# how to do fib:
# 1. start counting from 1
# 2. each iteration, get the current number and add it to the previous, store the value on next
# 3. after doing those operations, next becomes current
# 4. current becomes previous
# 5. rinse and repeat
