Tuples
======

Dictionary Items
----------------

- `items` can be used to get keys and values from a dictionary

Example
-------

```python
runtimes = {
    "The Fellowship of the Ring": 178, 
    "The Two Towers": 179,
    "The Return of the King": 201,
}

for kv_tuple in runtimes.items():
    print(kv_tuple)
```

Destructuring and for
---------------------

- Destructuring can be used to assign multiple variables in a `for` loop

```python
runtimes = {
    "The Fellowship of the Ring": 178, 
    "The Two Towers": 179,
    "The Return of the King": 201,
}

for movie, runtime in runtimes.items():
    print(f"{movie} is {runtime} minutes")
```

enumerate
---------

- [enumerate](https://docs.python.org/3/library/functions.html#enumerate) can be used to add a count to iterable items
- The return value from enumerate is an iterable of (count, value) tuples

Example
-------

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(list(enumerate(alphabet)))
```

Enumeration Loops
-----------------

- Enumeration can be used to avoid manual loops counters in certain loops

Example
-------

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in enumerate(alphabet):
    print(letter)
```

Exercise
--------

Use `enumerate` to print only the letters with an even-numbered index in a string.

<!--

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i, letter in enumerate(alphabet):
    if i % 2 == 0:
        print(letter)
```

-->

Modifying Lists Items
--------------------

- Enumeration can be helpful if we need a reference to list items during iteration

Example
-------

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]

for i, num in enumerate(nums):
    # Multiply every other value by 10
    if i % 2 == 0:
        nums[i] *= 10
        
print(nums)
```

Iterating multiple lists
------------------------

- It can be helpful to iterate multiple lists at the same time
- This can be accomplished with an index

Example
-------

```python
names = ["Jordan", "Pam", "John"]
ages = ["19", "24", "23"]

for i, name in enumerate(names):
    age = ages[i]
    
    print(f"{name} is {age}")
```

zip
---

- [zip](https://docs.python.org/3/library/functions.html#zip) can be used to directly match items from two iterables
- A new iterable is created providing tuples of items from the supplied iterators

Example
-------

```python
names = ["Jordan", "Pam", "John"]
ages = ["19", "24", "23"]

for pair in zip(names, ages):
    print(pair)
```

Example
-------

```python
names = ["Jordan", "Pam", "John"]
ages = ["19", "24", "23"]

for name, age in zip(names, ages):
     print(f"{name} is {age}")
```

Exercise
--------

Use zip to create a list of each pair of letters in a string. For example, the string "abcd" should produce the following list:

```python
[('a', 'b'), ('b', 'c'), ('c', 'd')]
```

<!--

alphabet = "abcd"

pairs = []

for pair in zip(alphabet, alphabet[1:]):
    pairs.append(pair)
    
print(pairs)

-->