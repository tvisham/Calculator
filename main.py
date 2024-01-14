input1 = int(input("Number 1: "))
input2 = int(input("Number 2: "))
operator = input("Operator? (add, subtract, multiply, divide) ")
running = True

def samenumbersfunction(): 
    input2 = int(input("Number 2: "))
    operator = input("Operator? (add, subtract, multiply, divide) ")  
    if operator == "add":
        result = result + input2
    elif operator == "subtract":
        result = result - input2
    elif operator == "multiply":
        result = result * input2
    elif operator == "divide":
        if input2 == 0:
            print ("You can not divide a number by zero")
        else: 
            result = result / input2
    print (result)

while running == True: 
    global result
    if operator == "add":
        result = input1 + input2
    elif operator == "subtract":
        result = input1 - input2
    elif operator == "multiply":
        result = input1 * input2
    elif operator == "divide":
        if input2 == 0:
            print ("You can not divide a number by zero")
        else: 
            result = input1 / input2
    print(result)
    keeprunning = input ("Would you like to keep playing? (y/n) ")
    if keeprunning == "y":
        running = True
        samenumbers = input("Do you want to use the same sum? (y/n) ")
        if samenumbers == "y":  
            samenumbersfunction()   
        if samenumbers == "n":
           input1 = int(input("Number 1: "))
           input2 = int(input("Number 2: "))
           operator = input("Operator? (add, subtract, multiply, divide) ")  
    elif keeprunning == "n":
        running = False
