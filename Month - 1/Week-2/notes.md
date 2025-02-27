# Python Programming by JS Technova


### Week 2: Functions and Object-Oriented Programming (OOP) in Python

**Syllabus**
- Defining and Calling Functions
- Function Arguments and Return Values
- Lambda Functions
- Modules and Packages
- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors, self and super()
- Hands-on: Create a Python class for real-world objects (e.g., Student,Vehicle).


## Notes

## What is Function
A function in Python is a reusable block of code that performs a specific task. It helps in modularizing code, improving readability, and reducing redundancy.

```python
def function_name(parameters):  
    """Docstring (optional): Describes the function"""  
    # Function body  
    return value  # (Optional)  

```
**Steps to Create a Function**
- Define the function using the def keyword.
- Provide a function name that follows Python naming conventions.
- Pass parameters (if required) inside parentheses.
- Write the function body with the required logic.
- Return a value using the return statement (optional).
- Call the function using its name with arguments (if needed).

**Example Function**
```python
def greet(name):  
    """This function prints a greeting message."""  
    return f"Hello, {name}!"  

print(greet("Suham"))  # Output: Hello, Suham!

# function with 3 parameters
def printItems(item1, item2, item3):
    print(item1, item2, item3)
#calling the function
printItems("c", item3 = "a", item2="b",)



# setting default values of function arguments
def printItems(item1, item2 = "b", item3 = "c"):
    print(item1, item2, item3)
printItems("a", item3= "d")

```
---
### Types of functions
There are basically three types of functions.
- Built in
- User Defined
- Library functions
- Lambda (Anonymous) Functions

**1. Built in functions:** These are predefined functions in Python.
```python
print(), input(), len(), int(), str()
```


**2. User-defined Functions:** These are functions created by users to perform specific tasks.
```python
def greet(name):
    return f"Hello, {name}!"    
print(greet("Suham"))  
```

**3. Lambda (Anonymous) Functions:** These are small, one-line functions without a name, created using the lambda keyword.
```python
square = lambda x: x ** 2
print(square(5))  
```

**4. Library Functions:** These function are defined inside libraries. To use these functions we need to import them first. They may be user defined or come built in with python interpreter.

```python
import math  #importing module
print( math.sqrt(4) )  # sqrt is function inside math module/library
```

### Scope of variables

# Scope of Variables in Python

The **scope** of a variable in Python determines where that variable can be accessed or modified within a program.

## Types of Variable Scope

### 1. **Local Scope**
- Variables declared inside a function are **local** to that function.
- They cannot be accessed outside the function.

**Example:**
```python
def my_function():
    x = 10  # Local variable
    print(x)  # Accessible within the function

my_function()
# print(x)  # Error: x is not defined outside the function
```

### 1. **Global Scope**
- Variables declared outside functions or classes have global scope.
- They can be accessed anywhere in the program.
- To modify a global variable inside a function, use the global keyword.

**Example**
```python
marks = 80 #global variable
def re_evaluation():
    marks = 90
re_evaluation()
print(marks) # output 80

#to modify global variable
def re_evaluation2():
    global marks
    marks = 90
re_evaluation2()
print(marks) # output 90
```


steps to upload codes: 
    -> initializaation ( git init )
    -> add repo link (git remote add <nickname> <git url> )
    -> add files ( git add filename/foldername  OR  git add .  adds all files and folders )
    -> commit the chnages  ( git commit -m "message" )
    -> push the code to github ( git push <nickname> <branch_name> )


steps to download codes: 
    -> initialization ( git init )
    -> add repo link (git remote add <nickname> <git url> )
    -> git pull <nickname> <branch_name>


