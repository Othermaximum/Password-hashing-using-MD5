# Password-hashing-using-MD5

This is my test take on using MD5 to hash passwords.\n
This program also acts as a wall to block content before a user logs in\n
A users data is hashed and stored in their respective files under ./Password Hasher/users/exampleuser.txt\n

The program requires hashlib and linecache\n
These are already imported in the program\n

Functions\n
  hash(inp)\n
    returns a hexdecimal value of the input string\n
  login()\n
    prompts the user for a username and password and will check the database for matching credentials\n
    returns a boolean value\n
  signin()\n
    prompts the user for a username and password and will add the credentials to the database\n
