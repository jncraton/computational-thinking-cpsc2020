Statements
==========

Statements
----------

- A statement is a unit of code that the Python interpreter can execute

Examples
--------

- `print("Hello, world")`
- `input("What is your name?")`
- `a = 42`

More operations
---------------

Integer division
----------------

- `//` performs integer division
- `%` is the modulus operator and computes the remainder after division

Basic string operations
-----------------------

- Concatenation can be performed using the `+` operator
- Duplication can be performed using the `*` operator

Comments
--------

Debugging
---------

Conditional Execution
=====================

Control Flow
------------

- By default, the Python interpreter runs the next instruction in our program
- In order to create more complex programs, it is helpful to choose which instruction runs next
- This is modification of the control plane of program execution

if statement
------------

- Optionally runs a block of code

```python
if x > 0 :
    print('x is positive')
```

---

![`if` control flow diagram](https://www.py4e.com/images/if.svg){height=540px}

Compond Statements
------------------

- Statements may be grouped together into blocks
- Blocks of statements should be indented using 4 spaces

Example
-------

```python
if False == True:
    print("This will not print")
    print("This will also not print")

print("This will print")
```

Alternative Execution
---------------------

- We may want to run something else when the `if` check fails
- This can be accomplished using `else`

Example
-------

```python
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
```

---

![else control flow diagram](https://www.py4e.com/images/if-else.svg){height=540px}