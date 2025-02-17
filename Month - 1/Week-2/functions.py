
list1 = [10, 0, 46, 87, 50]
list2 = [10, 0, 46, 87, 50]
list3 = [10, 0, 46, 87, 50]
list4 = [10, 0, 46, 87, 50]

# DRY -> Do not Repeat yourself

# for i in list1:
#     print(i)


# for i in list2:
#     print(i)


# for i in list3:
#     print(i)

# for i in list4:
#     print(i)



# def priintList(lists):
#     for i in lists:
#         print(i)

# priintList(list1)
# priintList(list2)
# priintList(list3)
# priintList(list4)


# func
# Syntax
# def function_name(argument):
#     # body
#     return  return_value  # optional


# Steps to create/run func in python

# Step 1 - function definition
# def printName( name ):
#     print(name)

# # step 2: function call
# printName("Ram")
# printName("Shyam")


# def printItems(item1, item2, item3):
#     print(item1, item2, item3)

# printItems("c", item3 = "a", item2="b",)


# setting default values of functions
# def printItems(item1, item2 = "b", item3 = "c"):
#     print(item1, item2, item3)
# printItems("a", item3= "d")


def add(a, b):
    print(a+b)
 
def subtract(a, b):
    print(a-b)

def multiply(a, b):
    print(a*b)

def divide(a, b):
    print(a/b)

def modulus(a, b):
    print(a%b)

def exponential(a, b):
    print(a**b)


def mainApp():
    while True:
        num1 = int(input("Enter number 1"))
        num2 = int(input("Enter number 2"))
        operation = input("Enter opration: [+,-,*,/,%,**, q ]")

        if operation == '+':
            add(num1, num2)
        elif operation == '-':
            subtract(num1, num2)
        
        elif operation == '*':
            multiply(num1, num2)
        
        elif operation == '/':
            divide(num1, num2)
        
        elif operation == '%':
            modulus(num1, num2)
        
        elif operation == '**':
            exponential(num1, num2)
        elif operation == 'q' or operation == 'Q':
            break
        else:
            print("Invalid input given.")


mainApp()