#  os.path.join() joins one or more path components intelligently. 
#  This method concatenates various path components with exactly one
#  directory separator (‘/’) following each non-empty part except
#  the last path component. If the last path component to be joined
#  is empty then a directory separator (‘/’) is put at the end.

import os

# Path
path = '/home'

# Join various path components
print(os.path.join(path, "User/Desktop", "file.txt"))

path = "User/Documents"

# Join various path components
print(os.path.join(path, "/home", "file.txt"))

# In above example '/home'
# represents an absolute path
# so all previous components i.e User / Documents
# are thrown away and joining continues
# from the absolute path component i.e / home.

path = "/User"

print(os.path.join(path, "Downloads", "file.txt", "/home"))

# In above example '/User' and '/home'
# both represents an absolute path
# but '/home' is the last value
# so all previous components before '/home'
# will be discarded and joining will
# continue from '/home'

path = "/home"

print(os.path.join(path, "User/Public/", "Documents", ""))

# In above example the last
# path component is empty
# so a directory separator ('/')
# will be put at the end
# along with the concatenated value