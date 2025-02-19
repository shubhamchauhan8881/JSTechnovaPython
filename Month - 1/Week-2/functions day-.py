import math

print( math.sqrt(4) )


# def function_name(args):
#     print(args)
    
# x = lambda: print("hello from lambda")
# x()

# lambda with parameters

# printName = lambda name:print(name)
# printName("Ram")


# funtion Syntax:
def fn_name(name):
    print(name)
    print()
    print()


# x = 50
# x is variable

# sum = lambda a, b: print(a)
    
# x is still a variable
# print(sum(50, 60))

# Function with return

# def sum(a, b):
#     print(a+b)
#     return a+b

# x = sum(10, 90)

# print(x)





def add(a, b):
    return a+b
 
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

def modulus(a, b):
    return a%b

def exponential(a, b):
    return a**b

def mainApp():
    while True:
        num1 = int(input("Enter number 1"))
        num2 = int(input("Enter number 2"))
        operation = input("Enter opration: [+,-,*,/,%,**, q ]")
        res = 0

        if operation == '+':
            res = add(num1, num2)
        elif operation == '-':
            res = subtract(num1, num2)
        
        elif operation == '*':
            res = multiply(num1, num2)
        
        elif operation == '/':
            res = divide(num1, num2)
        
        elif operation == '%':
            res = modulus(num1, num2)
        
        elif operation == '**':
            res = exponential(num1, num2)
        elif operation == 'q' or operation == 'Q':
            break
        else:
            print("Invalid input given.")
        print(res)




# Scope of variables

# Global variable
x = 40

def myfun():
    # local variable
    b = 40

myRes = 80

def Re_evaluation():
    global myRes
    myRes = 90

Re_evaluation()

print(myRes)

