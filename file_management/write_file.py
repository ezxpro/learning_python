import os

os.chdir(os.path.dirname(__file__))# get absolute path to the file
f = open("file.txt", "w", encoding = "utf-8") # 'w' attribute truncates (deletes) the file if it already exists

f.write("This is just a test\n")
f.write("Hope you like my test\n")
f.write("Lovely 3rd line for you\n")
f.close()