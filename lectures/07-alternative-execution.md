Alternative Execution
=====================

Else
----

- We may want to run something else when the `if` check fails
- This can be accomplished using `else`

Example
-------

```python
if x % 2 == 0 :
    print('x is even')
else :
    print('x is odd')
```

---

![else control flow diagram](https://www.py4e.com/images/if-else.svg){height=540px}

Example
-------

```python
small_num = input("Enter a number:")
big_num = input("Enter a bigger number:")

if small_num < big_num:
    print("You entered the numbers correctly")
else:
    print("Your second number is too small")
```

Chained Conditionals
--------------------

- We may want more than two branches of execution
- We can chain multiple conditionals to achieve this

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
- Comparison can be performed using standard comparison operators

Example
-------

```python
word1 = input("Enter a word:")
word2 = input("Enter another word:")

if word1 < word2:
    print(word1, "comes before", word2, "alphabetically")
elif word1 > word2:
    print(word1, "comes after", word2, "alphabetically")
else:
    print(word1, "and", word2, "are the same word")
```
