Formatted String Literals
-------------------------

format
------

- The textbook uses the `format` method on strings
- It is antiquated and has largely been superceded by [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) since Python 3.6.
- You will not be required to use or understand the `format` method in this class

f-strings
---------

- Proivde simple string formatting
- Python expressions can be included within strings
- An `f` should be used before the opening quote of the string literal

Example
-------

```python
>>> f"The answer is {7*6}"
```

Example
-------

```python
name = input("What is you name?")
  
print(f"Hello, {name}")
```

Format Specifiers
-----------------

- Can be added after an expression to adjust formatting
- This can be used for rounding or other purposes such as alignment

Example
-------

```python
num = 1

for pokemon in ["Charmander", "Charmeleon", "Charizard"]:
    print(f"{pokemon:12} {num}")
    num += 1
```

Example
-------

```python
import random

for _ in range(10):
    print(f"{random.random():.2f}")
```