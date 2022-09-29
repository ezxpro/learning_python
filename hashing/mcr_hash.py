import hashlib
import os

BKP_PATH = "Z:\\Setembro\\"
BUF_SIZE = 8388608

file_list = os.listdir(BKP_PATH)
file_list.sort() 

if 'backup_running' in file_list: # checks if backup folder is locked, quits if True
    print("A backup is currently running.\nExiting program...")
    quit()

last_file = file_list[len(file_list)-1] 
#l = len(last_file)

if '.mrimg.sha1' in last_file:
    print("Last backup is already hashed.\nExiting program...")
    quit()    
elif '.mrimg' in last_file: # generates and stores digest
    print("Hashing "+ last_file + ". Please wait...")
    sha1 = hashlib.sha1()
    with open(BKP_PATH + last_file, 'rb') as f: 
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    print("Hash generation succeeded.")
    digest = sha1.hexdigest()
    print("Hash is: " + digest + 
    "\nSaving it to " + last_file + ".sha1")

    h = open(BKP_PATH + last_file + '.sha1', 'w', encoding = "utf-8")
    h.write(digest + " *" + last_file)
    h.close()
'''
Just checked and there's more than one unverified backup.
I should:
1. organize this code into functions and;
2. Make it create a list of all unverified backups at launch
Something like this should do:
    for i in file_list:
        if i + ".sha1" not in file_list:
            (...) 
'''