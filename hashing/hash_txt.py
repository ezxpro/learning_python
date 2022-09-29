from ast import arg
from asyncio.windows_utils import BUFSIZE
from hashlib import sha1
from sys import argv
from xml.dom.minidom import TypeInfo 

BUF_SIZE = 65536

sha1 = sha1()
file = argv[1]
#if type(file) is not bytes:
#    file = file.encode(encoding = 'utf-8', errors = )

with open(file) as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data.encode(encoding = 'utf-8', errors = 'strict'))

print("SHA1: {0}".format(sha1.hexdigest()))