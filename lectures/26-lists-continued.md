Lists
=====

List functions
--------------

- Many built-in functions can operate on lists
- Examples include `len`, `max`, `min`, and `sum`

Example
-------

```python
mylist = [1, 2, 3, 4]

print(f"Number of values: {len(mylist)}")
print(f"Sum of values: {sum(mylist)}")
print(f"Smallest value: {min(mylist)}")
print(f"Largest value: {max(mylist)}")
```

Numeric lists
-------------

- Some functions will only work properly on lists with numeric elements
- `sum` won't work properly with strings, for example

Example
-------

```python
mylist = ["a", "b", "c"]

print(sum(mylist))
```

List constructor
----------------

- The `list` constructor can be used to create a list from a string

Example
-------

```python
items = list("abcdef")

print(type(items))
print(items)
```

Lists and Strings
-----------------

- A list is a sequence of arbitrary values
- A string is different data type that represents a sequence of characters
- They cannot always be used interchangeably

Example
-------

```python
items = "abc"

for letter in items:
    print(letter)
```

Example
-------

```python
items = ["a", "b", "c"]

items.split()
```

Objects and values
------------------

- Two values can hold the same contents without pointing to the same object
- Consider the following assignment:

```python
a = 'banana'
b = 'banana'
```

---

![Possible assignment results](https://www.py4e.com/images/list1.svg){height=540px}

is
----

- The `is` operator can be used to test if two values are the same object

Example
-------

```python
a = 'banana'
b = 'banana'

print(a is b)
```

Lists
-----

- Because lists are mutable, a new list is a new object
- Two lists with the same values may not be the same object

Example
-------

```python
a = list('banana')
b = list('banana')

print(a is b)
```

List equivalence
----------------

- We can also use `==` to compare lists
- This will perform a deep compare to check if the two lists have identical values

Example
-------

```python
a = list('banana')
b = list('banana')

print(a == b)
```

Exercise
--------

Write a Python function that will return `True` if and only if the two lists contain the same items but are not the same list.

```python
def equal_but_not_same(a, b):
    

a = [1, 2]

assert(equal_but_not_same([1, 2], [1, 2]) == True)
assert(equal_but_not_same(a, [1, 2]) == True)
assert(equal_but_not_same([1], [2]) == False)
assert(equal_but_not_same(a, a) == False)
```

Multiple References
-------------------

- Multiple variable can point to the same object

Example
-------

```
a = [1, 2, 3]
b = a

print(a is b)
```

Aliasing
--------

- An object with more than one reference to it is aliased
- Care must be taken when aliasing mutable objects
- A modification to one will affect the other

Example
-------

```python
scores = [100, 85, 75, 87]

letter_grades = scores

for i in range(len(scores)):
    if scores[i] >= 90:
        letter_grades[i] = 'A'
    elif scores[i] >= 80:
        letter_grades[i] = 'B'
    elif scores[i] >= 70:
        letter_grades[i] = 'C'

print(letter_grades)
print(scores)
```

Lists as arguments
------------------

- If a list is passed to a function, it will be aliased
- A modification inside the list will be seen by the caller

Example
-------

```python
def square_all(numbers):
    """ Return a list with the squares of all numbers"""
    
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]
        
    return numbers

mynums = [1, 2, 3, 4]

print(mynums)
print(square_all(mynums))
print(mynums)
```

Exercise
--------

Adjust the following program so that first_half does not modify the list it is passed

```python
mylist = list(range(10))

def first_half(values):
    """ Returns the first half of a list of values """
    for i in range(len(values) // 2):
        values.pop(-1)

    return values

print(first_half(mylist))
print(mylist)
```
