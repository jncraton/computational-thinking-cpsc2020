---

Trivia Night
------------

- October 9th @ 6pm in 346
- Prizes for the top 3 teams
- 3 member teams
- Teams that represent 3 unique majors get a bonus
- Teams that represent 3 different cohorts get a bonus

Definite Iteration
==================

Definite Iteration
------------------

- We frequently want to iterate a fixed number of times
- We may want to iterate over a fixed number of items
- Definite iteration provides a tools for this

for
---

- The `for` keyword provides definite iteration
- It will iterate over all items in the supplied iterable

Print characters in a word
--------------------------

Solution
--------

```python
word = "hello"

for letter in word:
    print(letter)
```

Count letters in a word
-----------------------

Solution
--------

```python
word = "hello"
count = 0

for letter in word:
    count += 1

print(count)
```

Sum of digits in a number
-------------------------

Solution
--------

```python
num = input("Enter a number:")

total = 0

for digit in num:
    total = total + int(digit)
    
print("The digits sum to", total)
```

Word counter
------------

Solution
--------

```python
text = input("Enter text to count words:")

words = 1

for character in text:
    if character == " ":
        words = words + 1

print(words)
```

break and continue
------------------

- `break` and `continue` can be used with for as expected

Lists
-----

- A list is a sequence of values
- Lists are defined using square brackets (`[` and `]`)
- Lists can be iterated using `for`

List example
------------

```python
mylist = [1, 2, 3]

for i in mylist:
    print(i)
```

Lists
-----

- Lists are covered in much more detail in chapter 8

range
-----

- `range` is a function that returns value for use in iteration
- It can provide a quick way to create a definite loop when combined with `for`

range example
-------------

```python
for i in range(10):
    print(i)
```

range parameters
----------------

- start - Where to start counting from
- stop - When to stop counting (exclusive)
- step - Number to count by (1 by default)

range parameter example
-----------------------

```python
# Count to 30 by 3
for i in range(0, 31, 3):
    print(i)
```

else
----

- `for` supports an else clause
- It will be executed if the loop is not interrupted

else example
------------

```python
user_color = input("Enter a color:")

for color in ['red', 'green', 'blue']:
    if user_color == color:
        break
else:
    print("You didn't enter an allowed color")
    exit()
    
print("You entered a correct color")
```
