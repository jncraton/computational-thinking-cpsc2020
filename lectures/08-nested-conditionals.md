Nested Conditional Execution
============================

Review
------

- `if` conditionally executes code
- `elif` conditionally executes alternative code
- `else` executes if no other conditions are met

Nesting Conditionals
--------------------

- We can nest blocks of code
- Conditional execution can be nested to create more complex control flow

Example
-------

```python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```

---

![Nested Control Flow Diagram](https://www.py4e.com/images/nested.svg){height=540px}

---

[Disney Princess Quiz](https://news.disney.com/quiz-which-disney-princess-are-you)

Star Wars Quiz
--------------

```python
age = int(input("How old are you?"))
color = input("What is your favorite color?")

if age < 21:
    if color == 'red':
        print("You are Darth Maul")
    else:
        print("You are Obi-wan Kenobi")
else:
    if color == 'red':
        print("You are Darth Vader")
    else:
        print("You are Luke Skywalker")
```

Exit
----

- `exit` can be used to immediately terminate a program.

Exit Example
------------

```python
dividend = int(input("Enter value for divdend:"))
divisor = int(input("Enter value for divisor:"))

if divisor == 0:
    print("Can't divide by zero")
    exit()

quotient = dividend // divisor
remainder = dividend % divisor

print("Quotient:", quotient)
print("Remainder:", remainder)
```

Summary of knowledge so far
---------------------------

- `input` and `print` statements
- Arithmetic expressions (`2 + 3`)
- Comparison operators (`2 <= 3`)
- Assignment statements (`a=3`)
- Conditional execution (`if`, `elif`, `else`)
