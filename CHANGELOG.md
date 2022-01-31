# Changelog

## Latest version:
**1.1.3**

### Version 1.0.0

    -Literally created the thing
    -Features include:
    -3 new functions
        hash(inp)
            hashes the input string into hexdecimal
        login()
            accesses the database and matches credentials
        signin()
            adds a new user to the database
    -basic script to prompt the terminal to sign up or log in
    
### Version 1.1.0

    -Modifying database to have seperate .txt files store user data
    -Old match line by line system removed due to confusion and lack of upgradability
    
    bugs
    -linecache inserts extra line when comparing to input password
    
SV 1.1.1
    
    New login system created
    linecache bug fixed with .rstrip('\n')
    
SV 1.1.2

    defined a new function
    readuserdata(user,data)
    will take user and data (line number) and returns a string of that line number

SV 1.1.3
    
    defined a new non-functional function
    modifyuserdata(user,data)
    plan to add more in the future
    
SV 1.1.4
    
    unhashed the username



