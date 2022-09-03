message = 'Python is fun'

# convert string to bytes
byte_message = bytes(message, 'utf-8')
for i in byte_message:
    print(i)