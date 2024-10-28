---
reading: '[Functions](https://www.py4e.com/html3/04-functions)'
...

Functions
=========

---

A function is a named sequence of statements that performs a computation

Calling Functions
-----------------

- We've already done this
- Use the function name followed by parens containing arguments to pass

Example
-------

- `int` is a function
- It takes one argument and returns a value

```python
num = int("42")
```

Return value
------------

- The name for the value returned from a function

Built-in function
-----------------

- Python includes many functions that we may have use for

min and max
-----------

- `min` and `max` return the minimum and maximum of their arguments

```python
>>> min(1, 3)
1
>>> max(12, 4)
12
```

Iterables
---------

- `min` and `max` can also operate on iterables such as strings

```python
>>> min("abc")
'a'
>>> max("green")
'r'
```

len
---

- `len` can be used to return the length of a value

```python
>>> len("Hello")
5
>>> len("Blue")
4
>>> len("")
0
```

Type conversions
----------------

- `int`, `float`, and `str` can be used to convert types

```python
>>> int("1")
1
>>> float("1.5")
1.5
>>> str(1.5)
'1.5'
```

Modules
=======

math
----

- The math module can be used to access various math functions
- `import math` can be used to create the math object used to access the module
- A module is a file containing Python definitions and statements

Dot notation
------------

- Modules contain functions and variables
- These can be accessed using the `.` character

```python
import math

print(math.pi)
```

Example
-------

```python
import math

dist = input("Distance to building:")
height = input("Building height:")

angle_rad = math.atan(float(height) / float(dist))
angle_deg = angle_rad * 180 / math.pi

print("Angle to top:", angle_deg)
```

help
----

- `help` can be used to provide information about an object
- `help(math)` provides information about available math functions

random
------

- The random module provides access to pseudorandom numbers
- These numbers will appear random, but are generated deterministically
- They should not be used in cryptography

Example
-------

```python
import random

# Print random number between 0.0 and 1.0
print(random.random())
```

randint
-------

- `randint` returns a random integer between bounds

```python
# Returns a number between 1 and 10 inclusive
random.randint(1, 10)
```

choice
------

- `choice` select one item from an iterable

```python
# Pick a, b, or c
random.choice("abc")
```
