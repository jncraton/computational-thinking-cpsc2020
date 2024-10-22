File Exceptions
===============

Errors in Programs
------------------

- Sources of errors in programs are numerous
- One common source of errors are incorrect assumptions about the environment in which the program is running

Missing Files
-------------

- An attempt to open a file for reading that does not exist will raise an exception

Example
-------

```python
handle = open("missing.txt")
```

Handling Exceptions
-------------------

- We can use `try` and `except` to handle these errors

Example
-------

```python
try:
    handle = open("missing.txt")
except FileNotFoundError:
    print("File not found")
```

User Selected Files
-------------------

- File name need not be hard-coded
- Names can be entered by a user
- This makes proper error handling more important

Example
-------

```python
filename = input("Select a file to read:")

try:
    handle = open(filename)
except FileNotFoundError:
    print(f"Error opening {filename}")
    exit(1)
    
contents = handle.read()

print(contents)
```

Handling Multiple Exceptions
----------------------------

- File reading may fail due to missing files
- File reading may fail due to invalid access rights
- These can be handled using separate `except` blocks

Example
-------

```python
filename = input("Select a file to read:")

try:
    handle = open(filename)
except FileNotFoundError:
    print(f"File '{filename}' does not exist")
    exit(1)
except PermissionError:
    print(f"File '{filename}' is not readable")
    exit(1)
    
contents = handle.read()

print(contents)
```

Exercise
---------

- `print` all capitalized words in a user-selected file.
- Show an appropriate error message if the file is not found.

<!--
Solution
--------

```python
filename = input("Filename:")

try:
    handle = open(filename)
except FileNotFoundError:
    print("File not found")
    exit(1)

contents = handle.read()

for word in contents.split():
    for vowel in "aeiou":
        if vowel in word:
            break
    else:
        print(word)
```
-->


Excercise
---------

Count all `if`, `elif`, and `else` keywords in a program

<!--

Solution
--------

```python
filename = input("Filename:")

try:
    handle = open(filename)
except FileNotFoundError:
    print("File not found")
    exit(1)

contents = handle.read()

count_if = 0
count_elif = 0
count_else = 0

for word in contents.split():
    if word == "if":
        count_if += 1
    elif word == "elif":
        count_elif += 1
    elif word == "else":
        count_else += 1
        
print(f"if: {count_if}")
print(f"elif: {count_elif}")
print(f"else: {count_else}")
```
-->

Key Ideas
---------

- Reading files creates new surface for errors
- `try` and `except` can be used to deal with exceptions
- Filenames can be entered by users or come from other dynamic sources