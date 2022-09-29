import os
#import sys
os.chdir(os.path.dirname(__file__))# gets around Python's messy working directory shit
# EXPLANATION: not sure why, but working directory will change depending on the weather,
#  that line gets absolute file path at runtime

# print(os.getcwd())

f = open('file.txt', 'r', encoding='utf-8') # the 'r' attribute is synonymous with "rt"

print("Printing just the 1st line:\n\n" + f.readline())

print("All remaining lines (as a list object): \n")
print(f.readlines())