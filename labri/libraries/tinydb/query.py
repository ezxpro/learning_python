from os import chdir, path
from tinydb import Query, TinyDB


# change  current path to script's dir
chdir(path.dirname(__file__)) 

db = TinyDB("db.json")

dbc = db.contains()
print(db.all())