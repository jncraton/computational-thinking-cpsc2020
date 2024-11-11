List Comprehensions
===================

Creating Lists
--------------

- We frequently want to create a list from another list
- This can be accomplished using a `for` loop

Example
-------

```python
nums = [2, 5, 9]

squares = []

for num in nums:
    squares.append(num * num)
    
print(squares)
```

Map
---

- The task of building one iterable from another is common
- A special function called `map` is provided to simplify this task
- `map` takes a function and applies it to all items in an iterable return a new iterable

Example
-------

```python
nums = [2, 5, 9]

def square(n):
    return n * n

squares = map(square, nums)

print(list(squares))
```

Lambda Functions
----------------

- It can sometimes be helpful to create small, inline functions
- The `lambda` keyword can be used to facilitate this

Example
-------

```python
double = lambda x: x * 2

print(double(4))
```

Map and Lambda
--------------

- `lambda` and `map` can be combined to quickly perform operations on entire lists

Example
-------

```python
nums = [2, 5, 9]
squares = map(lambda n: n*n, nums)
print(list(squares))
```

List Comprehensions
-------------------

- The pattern of creating one list from another is very common
- Python introduces special syntax to simplify these operations
- This is referred to as a list comprehension

Example
-------

```python
nums = [2, 5, 9]
squares = [n*n for n in nums]
print(squares)
```

Filtering
---------

- Filtering can be applied to list comprehensions using an `if` clause

Example
-------

```python
nums = list(range(10))
print(nums)
big_squares = [n*n for n in nums if n > 5]
print(big_squares)
```
