# Python Programming by JS Technova

### Week 1: Introduction to Python Programming

**Syllabus**
- Week 1: Introduction to Python Programming
- Introduction to Python
- Installing Python and Setting Up the Development Environment
- Writing and Executing Python Scripts
- Python Syntax and Indentation
- Data Types and Variables
- Operators (Arithmetic, Relational, Logical, etc.)
- Control Statements (if-else, loops: for, while)
- Input/Output in Python



# Introduction to Programming Language

## What is a Programming Language?
A programming language is a formal set of instructions that allows humans to communicate with computers to develop software applications, websites, and systems. It provides a structured way to write commands that a computer can execute.

## Types of Programming Languages
Programming languages can be classified based on their level of abstraction and paradigm:

### 1. Low-Level Languages:
- **Machine Language (Binary Code):** Directly understood by the computer (0s and 1s).
- **Assembly Language:** Uses symbolic representations (mnemonics) for machine instructions.

### 2. High-Level Languages:
- More human-readable and easier to write.
- Examples: C, Java, Python, JavaScript, etc.

## Programming Paradigms
Programming languages follow different paradigms or styles of programming:

### 1. Procedural Programming (C, Pascal)
- Code is organized into procedures or functions.
- Follows a step-by-step approach.

### 2. Object-Oriented Programming (OOP) (Java, Python, C++)
- Uses objects and classes to model real-world entities.
- Encourages modularity and reusability.

### 3. Functional Programming (Haskell, Lisp)
- Based on mathematical functions.
- Focuses on immutability and pure functions.

### 4. Scripting Languages (JavaScript, Python, Bash)
- Used for automating tasks and web development.

---

# Introduction to Python Programming

## What is Python?
Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library.

### It is used for:
- **Web Development:** Django, Pyramid, Bottle, Tornado, Flask, web2py
- **GUI Development:** tkinter, PyGObject, PyQt, PySide, Kivy, wxPython, DearPyGui
- **Scientific and Numeric:** SciPy, Pandas, IPython
- **Software Development:** Buildbot, Trac, Roundup
- **System Administration:** Ansible, Salt, OpenStack, xonsh

## Why Python?
- Works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc.).
- Its syntax is quite similar to the English language.
- Python allows developers to write programs with fewer lines than some other languages.
- Python runs on an interpreter system, allowing quick prototyping.
- Python supports procedural, object-oriented, and functional programming styles.

### Two major versions of Python:
- **Python 3.x:** The current version under active development.
- **Python 2.x:** The legacy version, receiving only security updates until 2020.
- **Python 3.13** is the latest stable release.

---

## Installing Python and Setting Up the Development Environment
- Download Python from the official website: [python.org](https://www.python.org/).
- Install Python and ensure it's added to the system PATH.
- Use an IDE like PyCharm, VS Code, or Jupyter Notebook.
- Verify installation using the command:
  ```sh
  python --version
  ```

## Writing and Executing Python Scripts
- Python scripts are saved with a `.py` extension.
- Run scripts using the command:
  ```sh
  python script.py
  ```
- Scripts can be executed in an IDE, terminal, or Python's built-in IDLE.

### Interactive Execution (REPL - Read, Evaluate, Print, Loop):
- Execute Python commands one by one in an interactive environment like the Python shell or Jupyter Notebook.
- Useful for quick testing and debugging.

### Script-Based Execution:
- Write Python code in a file with a `.py` extension and run it as a complete program.

---

## Python Syntax and Indentation:
Python uses indentation (whitespace) instead of curly braces `{}`.

```python
def fn():
    print("hello")
```
- Indentation refers to the spaces at the beginning of a code line.
- Proper indentation is crucial for code execution.
- Typically, four spaces are used per indentation level.

---

## Python Variables

## What is a Variable?
A variable is a named storage location in a program that holds a value. The value of a variable can change during the execution of the program. It acts like a container to hold/store a piece of data.

### Features of Variables:
- Stores data that can be used later.
- Can hold different types of data (numbers, text, etc.).
- Has a name (identifier) to reference it.

### Rules for Naming Variables:
- A variable name must start with a letter or an underscore (`_`).
- A variable name cannot start with a number.
- A variable name can only contain alphanumeric characters and underscores (`A-z`, `0-9`, and `_`).
- Variable names are case-sensitive (`age`, `Age`, and `AGE` are different variables).
- A variable name cannot be a Python keyword.

---

## Keywords in Python
Python keywords are reserved words that have special meanings and serve specific purposes in the language syntax.

### List of Python Keywords:
```
True, False, None, and, or, not, is, if, else, elif, for, while, 
break, continue, pass, try, except, finally, raise, assert, 
def, return, lambda, yield, class, import, from, in, as, del, 
global, with, nonlocal, async, await
```
You can also run this command in Python Shell to get the keywords:

```python
import keyword
print("The list of keywords is : ")
print(keyword.kwlist)
```

---

## Python Data Types
Python is dynamically typed, meaning you don’t need to declare variable types explicitly.

### Built-in Data Types:
- **Text Type:** `str`
- **Numeric Types:** `int`, `float`, `complex`
- **Sequence Types:** `list`, `tuple`, `range`
- **Mapping Type:** `dict`
- **Set Types:** `set`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`
- **None Type:** `None`

---

## Operators in Python
Operators are used to perform operations on variables and values.

### Types of Operators:
- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `%`, `//`, `**`
- **Assignment Operators:** `=`, `+=`, `-=`, `/=`
- **Comparison Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators:** `and`, `or`, `not`
- **Identity Operators:** `is`, `is not`
- **Membership Operators:** `in`, `not in`
- **Bitwise Operators:** `&` (AND), `|` (OR), `^` (XOR), `~` (NOT)

---

### Control Statements (if-else, loops: for, while)
- **if-else:** Used for conditional execution.
- **for loop:** Iterates over sequences like lists and strings.
- **while loop:** Repeats execution while a condition is true.
- **Break and continue:** Alters loop flow.

---

### Lists in Python

**Features of Python Lists**
✅ Ordered → Elements maintain their insertion order.
✅ Mutable → Can modify, add, or remove elements.
✅ Heterogeneous → Can store different data types.
✅ Allows Duplicates → Multiple occurrences allowed.
✅ Indexing & Slicing → Supports accessing elements using indices.

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
```

## Ways to Create a List

1. **Using Square Brackets (`[]`)**:
```python
    my_list = [1, 2, 3, 4, 5]
```
2. **Using list() Constructor:**
```python
    my_list = list((1, 2, 3, 4, 5))
```
3. **Using range() with list()**:
```python
    my_list = list(range(1, 6))
```

### List Methods
Python lists provide several built-in methods for manipulation:

**Method	Description**
```python
append(x) #Adds an element x at the end of the list.
extend(iterable)  #Extends the list by adding elements from an iterable.
insert(i, x) #Inserts x at index i.
remove(x) #Removes the first occurrence of x.
pop(i)  #Removes and returns the element at index i (default: last).
clear()	#Removes all elements from the list.
index(x, start, end)	#Returns the index of x (within optional range).
count(x) #Returns the number of times x appears in the list.
sort(key=None, reverse=False)	#Sorts the list in ascending order (or by key).
reverse()	#Reverses the order of elements.
copy()	#Returns a shallow copy of the list.

```

**Eample and usage**
```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # [1, 2, 3, 4, 5, 6]
my_list.remove(3)  # [1, 2, 4, 5, 6]
print(my_list.index(4))  # 2
my_list.sort(reverse=True)  # [6, 5, 4, 2, 1]
```