import os

# here i'll test the open() function with the "x" (exclusive creation) attribute
# this should only allow me to write to file if it doesn't exist yet
os.chdir(os.path.dirname(__file__))# get absolute path to the file

#first time, should write only if file doesn't exist
f = open("file_xc.txt", "x", encoding = "utf-8")

f.write("This is just a test\n")
f.write("Hope you like my test\n")
f.write("Lovely 3rd line for you\n")
f.close()

# second time, this wil throw an error
f = open("file_xc.txt", "x", encoding = "utf-8")
f.write("Biggest test of all time") 
f.close()