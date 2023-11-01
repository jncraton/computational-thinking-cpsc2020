Tuples
======

Container Types
---------------

- Strings contain a sequence of characters
- Lists contain a sequence of values of any time
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

Tuple Comparison
----------------

- Tuples are compared one element at a time (like strings)
- Once a larger element is found, that tuple is considered to larger
    - Future elements are not considered
