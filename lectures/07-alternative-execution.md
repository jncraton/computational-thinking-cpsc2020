Alternative Execution
=====================

Else
----

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

Chained Conditionals
--------------------

- We may want more than two branches of execution
- We can chain mulitple conditionals to acheive this

Chained Conditionals
--------------------

```python
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```

---

![elif control flow diagram](https://www.py4e.com/images/elif.svg){height=540px}

Improved printing
-----------------

- The print function will accept multiple items to print
- Items must be separated by commas

Print Example
-------------

```python
print("Hello world!")
print("A few numbers: ", 1, 2, 3)
```

Printing a name
---------------

```python
name = input("What is your name?")
print("Hello", name)
```

Basic string operations
-----------------------

- Concatenation can be performed using the `+` operator
- Duplication can be performed using the `*` operator
