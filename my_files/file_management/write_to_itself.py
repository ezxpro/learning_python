import os

os.chdir(os.path.dirname(__file__))

f=open(__file__, 'a', encoding='utf-8')
f.write('\nprint(__file__)')
f.close()

#each time this program is run, a line is added that prints this scripts's path
print(__file__)
print(__file__)
print(__file__)