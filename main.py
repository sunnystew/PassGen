from string import *
from random import randint

print(r"""
______             _____            
| ___ \           |  __ \           
| |_/ /_ _ ___ ___| |  \/ ___ _ __  
|  __/ _` / __/ __| | __ / _ \ '_ \ 
| | | (_| \__ \__ \ |_\ \  __/ | | |
\_|  \__,_|___/___/\____/\___|_| |_| v1.0
                                    
Made by sunnystew on GitHub

""")
password = printable[randint(0,93)]
for i in range(7):
	password += printable[randint(0,93)]
print("Your random password is:")
print(password)