CONspiracy 2023
===============

---

No class this Friday

CONspiracy 2023
---------------

- Annual CSSCD Cybersecruity Conference
- This Friday from 8am to 5pm at Flagship Enterprise Center
- [Reigstration is open](https://www.eventbrite.com/e/conspiracy-2023-tickets-658586288317?aff=ebdssbdestsearch&from=d725b5452fe411ee903172bdca9f6a1d) and covered for AU CS/Cyber/DS students
- Use promo code VOL2320 for free registration

---

![Conference Registration (AU promo code: VOL2320)](media/conspiracy-2023.png){height=540px}


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
except:
    print("File not found")
```

User Selected Files
-------------------

- File name need not be hardcoded
- Names can be entered by a user
- This makes proper error handling more important

Example
-------

```python
filename = input("Select a file to read:")

try:
    handle = open(filename)
except:
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

Find all words in a file with no vowels

Solution
--------

```python
try:
    handle = open("words.txt")
except:
    print("File not found")
    exit(1)

for word in handle:
    for vowel in "aeiouy":
        if vowel in word:
            break
    else:
        print(word)
```

Count all `if`, `elif`, and `else` keywords in a program

Key Ideas
---------

- Reading files creates new surface for errors
- `try` and `except` can be used to deal with exceptions
- Filenames can be entered by users or come from other dynamic sources