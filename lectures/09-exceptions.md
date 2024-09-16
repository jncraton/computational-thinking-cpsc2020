Announcements
=============

Cyber Team
----------

The Anderson Cyber Team would like to invite you to join our kickoff on September 18th at 7 PM in Decker 346. We will be serving ice cream and will be playing Wii bowling! At this gathering you can learn more about ACT and enjoy some free ice cream. Please bring yourself and your friends, we would love to see you there!

Major Declaration
-----------------

- [Declare your major](https://andersoncentral.etrieve.cloud/#/form/37) if you know what you planning to study
- If you aren't sure, you may still want to declare your most likely choice
- This allows you to access major-specific course planning and get an academic advisor in your area

Lab Questions
=============

---

Pokemon Nesting Example

Exceptions
==========

Failure
-------

- Code can fail for a variety of reasons
- Some errors can be caught before the program is run
- Others must be handled during runtime

Example
-------

```python
>>> speed = input("What is the air velocity of an unladen swallow?")
What is the air velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10:
```

Exceptions
----------

- Raised when error occurs during runtime
- Immediately ends the program with an error message*

Example
-------

```python
num = input("Enter a number between 1 and 10")

square = int(num) * int(num)

print("The square of your number is:", square)
```

Catching Exceptions
-------------------

- It is possible to continue execution after an exception is raised
- This requires us to catch the exception from a `try` block

Example
-------

```python
try:
    int("red")
except:
    print("Please enter a valid number")
```

Processing Exceptions
---------------------

- Report the error to the user
- Try again
- Do something else

Try again
---------

```python
entry = input("Enter a number between 1 and 10")

try:
    num = int(entry)
except:
    entry = input("That's not a number. Try again:")
    num = int(entry)

square = num * num
print("The square of your number is:", square)
```

Do something else
-----------------

```python
entry = input("Enter a number between 1 and 10")

try:
    num = int(entry)
except:
    print("That's not a number. Let's just use 5.")
    num = 5

square = num * num
print("The square of your number is:", square)
```

Catching all exceptions
-----------------------

- By default, all exceptions are caught by except
- This can cause problems
- We'll talk about addressing this later

Example
-------

```python
dividend = input("Enter dividend:")
divisor = input("Enter divisor:")

try:
    print("The quotient is", int(dividend) / int(divisor))
except:
    print("You did not enter numbers.")
```

Ignoring Exceptions
-------------------

- We should almost never ignore exceptions
- It is possible to ignore them using `pass`

Pass
----

```python
entry = input("Enter a number between 1 and 10")

try:
    num = int(entry)
except:
    pass

square = num * num
print("The square of your number is:", square)
```

Pass keyword
------------

- The `pass` keyword is valid in many places
- It is not explicitly related to exceptions
- It simply indicates that while a statement is expected, we don't have anything to do

Example
-------

```python
i = 1

if i == 2:
    pass
else:
    print("i is not 2")
```
