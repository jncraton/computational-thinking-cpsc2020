---
reading: '[PY4E: Dictionaries](https://www.py4e.com/html3/09-dictionaries)'
...

Dictionaries
============

List
----

- Lists map numbers to values
- Lists are *dense*, meaning numbers from 0 up to the list length all map to a value

Dictionaries
------------

- Can also map numbers to values
- Can be *sparse* meaning they don't need to map all possible values
- Created using curly braces `{}`

Example
-------

```python
values = {}

values[0] = "a"
values[2] = "b"

print(values[2])
```

Hashable Types
--------------

- An object is hashable if it has a hash value which never changes during its lifetime and can be compared to other objects
- Hashable objects which compare equal must have the same hash value
- Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally

Dictionary Keys
---------------

- Integers may be used as keys
- Strings may be used as keys
- Any other hashable type may be used as a key

Example
-------

```python
values = {}

values["a"] = 1
values["b"] = 2

print(values["a"])
```

Exercise
--------

Create a program that builds a dictionary that maps the days of the week to the time you need to wake up on these days.

Printing Dictionaries
---------------------

- Dictionaries can be printed directly
- They will show value mapping between curly braces `{}`

Example
-------

```python
values = {}

values["a"] = 1
values["b"] = 2

print(values)
```

Instantiating Dictionaries with Values
--------------------------------------

- The output format from the previous example can be used to create new lists directly

Example
-------

```python
values = {"a": 1, "b": 2}

print(values)
```

Whitespace
----------

- Whitespace may be used inside dictionary declarations
- New lines may be used to organize declarations

Example
-------

```python
poketypes = {
    "Charmander": "fire",
    "Squirtle": "water",
    "Bulbasaur": "grass",
}

print(f"Squirtle is {poketypes['Squirtle']} type")
```

in
----

- The `in` operator can be used
- `in` will return True if the key exist in the dictionary

Example
-------

```python
hrs = {
    "Bonds": 762,
    "Aaron": 755,
    "Ruth": 714,
}

print("Pujols" in hrs)
print("Aaron" in hrs)
print(762 in hrs)
```

Exercise
--------

Create a program that can count the number of occurrences of each word in a text

```python
text = """In the beginning was the Word, and the Word was with God, and the Word was God."""
```

Solution
--------

<!--

```python
text = """In the beginning was the Word, and the Word was with God, and the Word was God."""

counts = {}

for word in text.split():
    word = word.strip(",.")
    
    if not word in counts:
        counts[word] = 0
        
    counts[word] += 1

print(counts)
```

-->
