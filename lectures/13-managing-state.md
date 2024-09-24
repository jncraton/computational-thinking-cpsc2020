Managing State
==============

Testability
-----------

- In order to test code, it helps for it to be written with tests in mind
- Isolation of functionality is important

Readability
-----------

- Code that is easier to test is often easy to read
- Breaking code at distinct test boundaries can simplify the architecture

Pure Functions
--------------

- No side effects
- No reliance on external state
- Always return the same output given the same inputs

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

Global Variable
---------------

- Defined over the entire scope
- Torn down only on program termination
- Useful for storing global data

Global Variable
---------------

```
def get_tip(price):
    return int(percentage) / 100 * float(price)

percentage = input("Tip percentage: ")
price = input("Meal price: ")

print("Tip:", get_tip(price))
```

-----

How would we test get_tip?

State
-----

- Managing state is critical for creating readable code
- Testability is enhance when we limit external state
