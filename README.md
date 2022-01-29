# Password-hashing-using-MD5

This is my test take on using MD5 to hash passwords.

This program also acts as a wall to block content before a user logs in

A users data is hashed and stored in their respective files under ./Password Hasher/users/exampleuser.txt
_______________________
The program requires hashlib and linecache;

These are already imported in the program

Functions
--
  hash(inp)
  
    - returns a hexdecimal value of the input string
    
  login()
  
    - prompts the user for a username and password and will check the database for matching credentials
    
    - returns a boolean value
    
  signin()
  
    - prompts the user for a username and password and will add the credentials to the database
