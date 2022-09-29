import sys
from termcolor import colored, cprint
from colorama import init, deinit
from random import shuffle
init() # initialize colorama

# ALGORITH:
# 1 Create 2 lists with name of available colors (like 'red', 'blue')
# 2 use random.shuffle on both
# 3 iterate through one of the shuffle lists with for i in list
# 4 if list_a[i] != listb[i] >>> pass current color of each list to cprint
# 5 the second argument (background color) of cprint uses the 'on_red' format
# instead of 'red', so I need to concatenate 'on_'+'red' to get the color I need.
 
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

backgrounds = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

shuffle(colors)
shuffle(backgrounds)

texto = input("Digite um texto da sua preferência: \n")

l = 0
for i in range(len(colors)):
	for k in range(len(backgrounds)):
		if(colors[i] != backgrounds[k]):
			bg = 'on_'+backgrounds[k]
			cprint(texto, colors[i], bg)


	


deinit()
# Not using attributes for now, so I'm commenting those out:
#lst_attrs = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']