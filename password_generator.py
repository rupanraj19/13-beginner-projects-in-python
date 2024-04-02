# ask user if they want to generate password or not
# if yes, ask for password length
# Generate password
# print password
# If no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_+")

def generate_password():
    password_length = int(input("Enter password length: "))
    
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate a password(y/n): ")
if option == "y":
    generate_password()
else:
    exit()