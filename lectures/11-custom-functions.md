Creating Functions
==================

Function definition
-------------------

- Specifies the name of a new function 
- Specifies the sequence of statements that execute when the function is called
- The function can be reused throughout the program

Example
-------

```python
def print_twice(value):
    print(value)
    print(value)
```

Void functions
--------------

- Void functions do not return a value
- They may still do useful work
- `print` is an example of a void function

Fruitful functions
------------------

- Fruitful functions return a value
- This value can be used later in your programs
- `input` is an example of a fruitful function

Example
-------

```python
def square(n):
    return n*n

print(square(2))
print(square(7))
```

Flow of Execution
-----------------

- Programs generally run from top to bottom
- Function definitions are not executed
- Functions run only when called

---

Functions may call other functions

Example
-------

```python
def square(n):
    return n*n

def cube(n):
    return n * square(n)

print(cube(2))
```

Parameters and arguments
------------------------

- Arguments are the values passed to a functions
- Parameters are the variable names used inside the function

---

No lab this Friday (September 22)
