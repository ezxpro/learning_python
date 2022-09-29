from os import chdir, path

chdir(path.dirname(__file__))

f = open("file_xc.txt", "a", encoding = "utf-8")

f.write("\n\nBiggest test of all time (now it worked)\n" + 
"These last 2 lines were appended later") 
f.close()