from termcolor import colored
from colorama import init, deinit
import sys

init()

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

for i in colors:
    print(colored("---RAINBOW---", i))

deinit()