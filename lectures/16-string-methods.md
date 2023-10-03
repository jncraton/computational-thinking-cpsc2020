RavenEdge Career Fair
---------------------

- 1-3pm Wednesday in the fieldhouse of KWC
- Required for all CS/Cyber/DS majors
- Not explicitly required for this course (because it is open to non-majors)
- No class Wednesday

Upcoming Exam
-------------

- Last new content before exam is today
- You are allowed 1 page of handwritten notes for the exam
- Paper and pencil are also allowed for working problems if desired

String Methods
==============

Methods
-------

- Methods are functions that operate on a known piece of data
- Most operators are shortcuts to object methods

Example
-------

```python
>>> 1 + 2
3
>>> (1).__add__(2)
3
```

dir
---

- `dir` can be used to list methods available on an object

Example
-------

```python
>>> dir(1)
['__abs__', '__add__', ...]
>>> dir("")
['__add__', ...]
```

upper and lower
---------------

- `upper` can be used to uppercase a string
- `lower` can be used to lowercase it

Example
-------

```python
>>> a = "Hello, world!"
>>> a.lower()
'hello, world!'
>>> a.upper()
'HELLO, WORLD!'
```

---

How could we compare strings ignoring case?

Solution
--------

```python
color = input("Enter a color:")

if color.lower() == "red":
    print("Roses are red")
elif color.lower() == "blue":
    print("Violets are blue")
else:
    print("Unknown color")
```

find
----

strip
-----

startswith
----------

count
-----

Slicing
-------

Negative Indexes
----------------