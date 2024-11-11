---
reading: '[PY4E: Tuples](https://www.py4e.com/html3/10-tuples)'
...

Lab Review
----------

[Lab 8](https://github.com/jncraton/sloc)

Tuples
======

Container Types
---------------

- Strings contain a sequence of characters
- Lists contain a sequence of values of any type
- Dictionaries contain values of any type indexed by key

Tuples
------

- Tuples contain a sequence of values
- Values may be any type

Tuple Creation
--------------

- Tuples are created as comma-separated values

Example
-------

```python
t = 1, 2

print(t)
```

Small Tuples
------------

- A one-item tuple can be created using a trailing comma `t = 1,`
- An empty tuple may be created using the `tuple` constructor or empty parens (`()`)

Example
-------

```python
single = "a",
print(single)

empty = tuple()
print(empty)

empty = ()
print(empty)
```

Tuple constructor
-----------------

- The `tuple` constructor can also be used to convert other types into tuples

Example
-------

```python
letters = tuple("Hello")

print(letters)
```

Tuple Features
--------------

- Indexing works like lists for the most part
- Assigning via index is not allowed (like strings)

Example
-------

```python
t = "a", "b", "c"

print(t[1])

t[1] = "x"
```

Immutability
------------

- The container itself is immutable
- Mutable values (such as lists) can still be modified

Example
-------

```python
t = ("A", [1, 2])

print(t)

t[1].append(3)

print(t)
```

Destructuring Assignment
------------------------

- A destructuring assignment can be used to assign multiple values at once
- The right hand side must be the same length as the left hand side

Example
-------

```python
a, b = (1, 2)

print(a)
print(b)
```

Example
-------

```python
word1, word2 = "Hello world".split()

print(word1)
print(word2)
```

Tuple Comparison
----------------

- Tuples are compared one element at a time (like strings)
- Once a larger element is found, that tuple is considered to larger
    - Future elements are not considered

Example
-------

```python
smaller = (1, 3, 1000)
larger = (1, 4, 0)

print(smaller < larger)
```

DSU Pattern
-----------

- Uses tuples for sorting items
- Decorate items using a sort key
- Sort items
- Undecorate the items by removing the sort key

Example
-------

```python
sentence = "The quick brown fox jumped over the lazy dog"

decorated = []

for word in sentence.split():
    decorated.append((len(word), word))

decorated.sort()

undecorated = []

for _, word in decorated:
    undecorated.append(word)

print(undecorated)
```
