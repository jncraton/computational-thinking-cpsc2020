Variables
=========

Definition
----------

A variable is a name that refers to a value

Statements
----------

- A statement is a unit of code that the Python interpreter can execute
- Example: `print("Hello, world")`

Assignment Statement
--------------------

- Creates a new variable
- Gives the variable a value

```python
myvar = 42
```

Variables
---------

- Names bound to values
- Useful for organizing data flow
- Provide human-readable names for values

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

Reseverd words may not be used as variable names

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

Example
-------

```python
user_msg = input("I'm an AI assistant. How may I help you?")

print("It sounds like you'd like help with the following:")
print(user_msg)
print("As an AI assistant I'm not able to help with that.")
```

Comments
--------

- Can be inserted into code as notes for human readers
- Ignored by Python interpretter
- Begin with `#` symbol

Example
-------

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

int
---

- `int` converts strings to integers

Examples
--------

>>> '12'
'12'
>>> int("12")
12
>>> int("Hello world!")
...ValueError...
>>> int("12.0")
...ValueError...
