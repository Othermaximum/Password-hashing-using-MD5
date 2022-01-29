# TODO
# problem: hash are dependent on being on the same lines from each txt
# problem: if someone uses the same username as one already in use, it will overwrite old file
# make better system to check if user matches password (different files per user???(this might be useful for additional user data)) < i like this idea



import hashlib #MD5 hash library 
import linecache #line reading library

#hash function returns a hexdecimal hashed version of the input
def hash(inp):
    result = hashlib.md5(inp.encode())
    outp = result.hexdigest()
    return outp

#newacc function creates new file that stores user data (hashed username and password)
def newacc(user,passw):
    fileobj = open(f'users/{user}.txt','a')
    L = hash(user),'\n', hash(passw),'\n' #more lines added here/new data/user data
    fileobj.writelines(L) 
    fileobj.close()

def login():
    
    user = input("Username : ")
    passw = input("Passowrd : ")

    open(f'users/{user}.txt','r')

    if linecache.getline(f'users/{user}.txt',1) == hash(user): #linecache inserts invisible line
        print("g")
    else:
        print(user)
        print(linecache.getline(f'users/{user}.txt',1))
        print(hash(user))


    




"""
#login function matches inputted hashed username and password with what is in the database. will return boolean output depending on credentials
def login(): #needs to be fixed to work with new database system
    user = (input("Username : ")

    ushash = hash(user)
    

    ufile = open(f'users/{user}.txt','r')

    ruser = ufile.read()

    pfile = "null"

    if ushash not in ruser:
       print("Not a valid username")
    else:
        passw = hash(input("Password : "))
    
        pfile = open(f'users/{user}.txt','r')
    
        rpass = pfile.read()
    
        if passw in rpass:
            with open(f'users/{user}.txt') as ufile:
                for num, line in enumerate(ufile, 1):
                    if ushash in line:
                        u = num 

            with open(f'users/{user}.txt') as pfile:
                for num, line in enumerate(pfile, 1):
                    if passw in line:
                        p = num

            if p == u:
                print("Correct Credentials")
        else:
            print("Incorrect Credentials")   




   
    return p == u


    ufile.close()
    pfile.close()
"""

#login script to login or create account aswell as inputs
z = input("Log in (l) or create a new account (c) : ").lower()

if z == "c":
    print("Create a new account...\n")
    newacc(input("Username : "), input("\nPassword : "))
else:
    if z == "l":
        print(login())
    else:
        print("Not a valid response")