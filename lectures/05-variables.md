---
reading: '[PY4E: Variables](https://www.py4e.com/html3/02-variables)'
...

Variables
=========

Definition
----------

A variable is a named container for a value

Statements
----------

- A statement is a unit of code that the Python interpreter can execute
- Example: `print("Hello, world")`

Assignment Statement
--------------------

- Creates or rebinds a variable
- Gives the variable a value

```python
myvar = 42
```

Variables
---------

- A variable is a named container for a value
- Useful for organizing data flow
- Provide human-readable names for values
- Allow values to be reused

Example
-------

```python
>>> base = 5
>>> height = 6
>>> area = (1 / 2) * base * height
>>> area
15.0
```

Variable Names
--------------

- Should document what the variable is used for
- May include letters and numbers
- Should be lowercase
- May not begin with a number

Reserved Words
--------------

Reserved words may not be used as variable names

    and     continue  finally  is        raise
    as      def       for      lambda    return
    assert  del       from     None      True
    async   elif      global   nonlocal  try
    await   else      if       not       while
    break   except    import   or        with
    class   False     in       pass      yield

Input Statement
---------------

- `input(prompt=None)`
- Accepts user input as an `str` (string)
- `prompt` will be shown to user if provided
- [Documentation for input](https://docs.python.org/3/library/functions.html#input)

input Example
-------------

```python
user_msg = input("I'm an AI assistant. How may I help you?")

print("It sounds like you'd like help with the following:")
print(user_msg)
print("As an AI assistant, I'm not able to help with that.")
```

int
---

- `int` converts strings to integers

Examples
--------

```python
>>> '12'
'12'
>>> int("12")
12
>>> int("Hello world!")
...ValueError...
>>> int("12.0")
...ValueError...
```

Comments
--------

- Can be inserted into code as notes for human readers
- Ignored by Python interpreter
- Begin with `#` symbol

Example Program
---------------

```python
# Gather user inputs
base = input("Base:")
height = input("Height:")

# Calculate area result
area = (1 / 2) * int(base) * int(height)

# Display result
print("Area of the triange:")
print(area)
```
