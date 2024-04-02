# define the function needed : add, sub, mul , div
# print options to the user 
# ask for values
# call the functions
# while loop to continue the program until the user request to exit

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print ("A. Add")
    print ("B. Sub")
    print ("C. Mul")
    print ("D. Divide")
    print ("E. Exit")

    choice = input("Enter your choice: ").lower()

    if choice == "a":
        print("Add")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = add(a, b)
        print(f"Answer is {c} \n")
    elif choice == "b":
        print("Sub")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = sub(a, b)
        print(f"Answer is {c} \n")
    elif choice == "c":
        print("Mul")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = mul(a, b)
        print(f"Answer is {c} \n")
    elif choice == "d":
        print("Divide")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = div(a, b)
        print(f"Answer is {c} \n")
    elif choice == 'e':
        print("Exit")
        quit()


