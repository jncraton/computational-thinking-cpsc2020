Lab Notes
=========

Assignment
----------

- Used to store values for later use


```python
a = 4
name = input("What is your name")
```

Converting to Integers
----------------------

- `int` can be used to convert values into integers

```python
>>> "42"
'42'
>>> int("42")
42
```

`type`
------

- `type` can be used check the type of a value


```python
>>> type("Hello")
<class 'str'>
>>> type(1)
<class 'int'>
```

Storing converted values
------------------------

- `int` does not modify value in place
- Results must be stored or used

```python
answer = "42"
int(answer) # Has no meaningful side effects
answer_num = int(answer) # Stores answer as int
```

Getting Help
------------

- Reach out if you need help on a lab
- Others students can be a great source of help
- Learn to know when you are using other resources as a crutch

Conditional Execution
=====================

Control Flow
------------

- By default, the Python interpreter runs the next instruction in our program
- In order to create more complex programs, it is helpful to choose which instruction runs next
- This is modification of the control plane of program execution

if statement
------------

- Conditionally runs a block of code
- A Boolean expression (the *condition*) follows the if statement
- The `if` statement is terminated by a `:`

```python
if i == 0:
```

Example
-------

```python
if x > 0:
    print('x is positive')
```

---

![`if` control flow diagram](https://www.py4e.com/images/if.svg){height=540px}

Compound Statements
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

New Operations
==============

Integer division
----------------

- `//` performs integer division
- `%` is the modulo operator and computes the remainder after division

Division Example
----------------

```python
>>> 11 / 4
2.75
>>> 11 // 4
2
```

Modulo Example
--------------

```python
>>> 11 % 4
3
>>> 12 % 4
0
>>> 0 % 4
0
>>> 3 % 2
1
```

---

Why would we want a modulo operation?

---

Even or Odd
-----------

```python
number = int(input("Enter a number:"))

if number % 2 == 0:
    print("Your number is even")

if number % 2 == 1:
    print("Your number is odd")

```