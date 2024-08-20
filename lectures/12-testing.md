Testing
=======

---

How do we know if software works?

---

> Software testing is the act of checking whether software satisfies expectations.

Testing
-------

- Determines correctness in some scenarios
- Will not find all bugs

---

```python
def square(n):
    return n*n
```

How do we know if this code works?

Test Cases
----------

- We can confirm known outputs
- `assert` is a simple tool for this
- `assert` will raise an exception if its input expression if `false`

assert
------

```python
assert(1==1) # Confirms that 1 is 1
assert(1==2) # Raises AssertionError
```

Square with Tests
-----------------

```python
def square(n):
    return n*n

assert(square(0) == 0)
assert(square(1) == 1)
assert(square(2) == 4)
assert(square(25) == 625)
```

Types of Tests
--------------

- Unit - Tests invididual parts of the system
- Integration - Tests components integrated from smaller components
- End-to-end - Tests an entire system

---

![Testing Pyramid](https://upload.wikimedia.org/wikipedia/commons/a/a4/Testing_Pyramid.png)

Testability
-----------

- In order to test code, it helps for it to be written with tests in mind
- Isolation of functionality is important
- 

Readability
-----------

- Code that is easier to test is often easy to read
- Breaking code at distinct test boundaries can simplify the architecture

Pure Functions
--------------

- No side effects
- No reliance on external state
- Always returns the same output given the same inputs

Pure Function
-------------

```python
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
```

Impure Function
---------------

```python
n = 2

def square():
  return n*n

n = 4
print(square())
```

Global State
------------

- Global state exists for the life a program
- Local state exists in a section of code
- Code that references global state can be more difficult to reason about

Local Variables
---------------

- Are only defined within a function
- Torn down when function terminates
- Useful for storing temporary data

Local Variable
--------------

```python
def is_freezing(temp, unit):
    if unit == 'C':
        temp_f = temp * 9/5 + 32
    else:
        temp_f = temp
        
    if temp_f < 32:
        return True
    else:
        return False
```
