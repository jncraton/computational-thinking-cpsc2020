---
reading: '[PY4E: Lists](https://www.py4e.com/html3/08-lists)'
...

Lab Review
==========

Lists
=====

list
----

- A list object is a sequence of values
- Values may be of any type
- Values may have different types

Creating a list
---------------

- Lists can be created using square brackets enclosing expressions separated by commas
- `[1, 2, 3]`
- `["a", "b", "c"]`

Example
-------

```python
mylist = [1, 2, 3]
```

Empty lists
-----------

- An empty list is a valid data structure
- This is created using square brackets with nothing inside: `[]`
- Empty lists evaluate to False in Boolean expressions

Example
-------

```python
if []:
    print("This won't print")
```

Falsy Values
------------

- Most Python values evaluate as True in a Boolean expression
- Exceptions include empty containers and 0-valued numerics
- [More info](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

Mutability
----------

- Unlike strings, lists are mutable
- We can change an item inside a list

Example
-------

```python
mylist = [1, 2, 3]

mylist[0] = 7

print(mylist)
```

Mapping
-------

- One way to reason about a list is as a mapping from numbers to elements
- Language of one value "mapping to" another is also useful in later data structures

Indices
-------

- Any integer may be an index
- Indices outside the list will raise an `IndexError`
- Negative numbers index from the back

Example
-------

```python
mylist = [1, 2, 3]

mylist[-4] = 7
```

in operator
-----------

- The `in` operator is supported on lists
- It will return True if a given value is found in the list

Example
-------

```python
mylist = [1,2,3]

if 2 in mylist:
    print("The list has a 2")
```

List Traversal
--------------

- A list is an iterable datatype
- We can use for to iterate over the items in a list

Example
-------

```python
mylist = [1,2,3]

for i in mylist:
    print(i)
```

Writing List Elements
---------------------

- `for` is useful for reading, but doesn't allow modification directly
- If we need to write, we need access to an index
- This can be achieved using `len` and `range`

Example
-------

```python
mylist = [1,2,3]

for i in range(len(mylist)):
    mylist[i] *= mylist[i]
    
print(mylist)
```

Exercise
--------

Create a Python program that will add 1 to every element in a list.

Nested Lists
------------

- Lists can be used as list values
- Nested lists only count as 1 element when computing `len`

Example
-------

```python
mylist = [1, 2, [3, 4, 5], 6]

print(len(mylist))
```

Exercise
--------

Create a Python program that will count all individual elements in nested lists.
