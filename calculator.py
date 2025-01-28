import os
clear = lambda:os.system('cls')
clear()
print("\n---Calculator---\n")
while True:
    print("Type 'q' To Quit")
    a = input("Enter 1st number: ")
    if a.lower() == "q":
        print("Thank You")
        break
    a = float(a)
    
    b = input("Enter the 2nd number: ")
    if b.lower() == "q":
        print("Thank You")
        break
    b = float(b)
    
    operation = input("Choose The Operation (+, -, *, /): ")
    if operation.lower == "q":
        print("Thank You")
        break
    
  
    if operation == "+":
        clear() 
        result = a + b
        print(f"{a} + {b} = {result}\n")
    elif operation == "-":
        clear()   
        result = a - b
        print(f"{a} - {b} = {result}\n")
    elif operation == "*": 
        clear()  
        result = a * b
        print(f"{a} * {b} = {result}\n")
    elif operation == "/": 
        clear()  
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}\n")
        else:
            print("Error! Division by 0 is not allowed.\n")
    else:  
        print("Invalid Operation!\n")