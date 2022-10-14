from os import chdir, path
from tinydb import Query, TinyDB


# change  current path to script's dir
chdir(path.dirname(__file__)) 


def create_db_entry():
    #db_entry = {}
    print("This is a routine to create entries for a TinyDB database.\n"+
          "Type 'key' value and then its definition when prompted." +
          "Each key will be associated with the corresponding " +
          "definition, binding them in a pair. Then, after you exit " +
          "the prompt, all pairs will become entries in a TinyDB database"  
         )
    while(True):
        keep_prompting = input("Do you wanna insert a new key/definition entry?\n"
         + "yes|no\n" + "answer: "
        )
        if keep_prompting.lower() == "no":
            break
        elif keep_prompting.lower() == "yes":
            key = input("Type the name of the key: \n")
            definition = (input("Type the definition for this key: \n"))
            if key.isnumeric():
                key = int(key)
            if definition.isnumeric():
                definition = int(definition)
            #db.update(key : definition)
        else:
            print("error! You must type either yes or no")
    return key, definition


# sets up a database, if file is not present, creates it
db = TinyDB('db.json') 


# inserts entries in the database. Expects dicts as input
db.insert(create_db_entry())


