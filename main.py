from string import *
from random import randint

print(r"""
______             _____            
| ___ \           |  __ \           
| |_/ /_ _ ___ ___| |  \/ ___ _ __  
|  __/ _` / __/ __| | __ / _ \ '_ \ 
| | | (_| \__ \__ \ |_\ \  __/ | | |
\_|  \__,_|___/___/\____/\___|_| |_| v1.1
                                    
Made by sunnystew on GitHub

""")

password = "0"


for i in range(7):
    password += printable[randint(0,93)]

print("Your random password is:")
print(password)

while True:
    again = input("\nAgain (y/n)? ")
    if again.lower() == "y":
        password = "0"
        for i in range(7):    
                password += printable[randint(0,93)] 
        print("\nYour random password is:")
        print(password)
    else:
        exit()
