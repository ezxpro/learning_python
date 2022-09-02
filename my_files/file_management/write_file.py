import os

os.chdir(os.path.dirname(__file__))# get absolute path to the file
f = open("file.txt", "w", encoding = "utf-8")

f.write("This is just a test\n")
f.write("Hope you like my test")
f.close()