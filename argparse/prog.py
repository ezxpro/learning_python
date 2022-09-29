import argparse

### CONCEPTS ###
# POSITIONAL ARGUMENT: argument that's interpreted according 
# to its position: e.g "cp SRC DEST", both args are positional

# this here does nothing, just allows you print an empty help page
parser = argparse.ArgumentParser()
#parser.parse_args()

# add positional arguments
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)