List Operations
===============

List + operator
---------------

- The `+` operator can be used to concatenate lists

Example
-------

```python
start = [1, 2]
end = [3, 4]
complete = start + end
print(complete)
```

Appending
---------

- The `+` operator may be used for appending
- Single items must be represented as a list of length 1

Example
-------

```python
mylist = [1,2,3]

# The following will raise an exception
mylist = mylist + 4

print(mylist)
```

List * operator
---------------

- The `*` operator can be used to duplicate lists

Example
-------

```python
mylist = [1, 2, 3]
longlist = mylist * 20
print(longlist)
```

Slicing
-------

- Lists support slicing as used with strings
- Omitted values will be treated as the start and end of the list

Example
-------

```python
mylist = [1, 2, 3, 4, 5, 6]

print(mylist[1:4])
print(mylist[:4])
print(mylist[1:])
```

Slices in assignment
--------------------

- Slices can be used in the left hand side of an assignment

Example
-------

```python
mylist = [1, 2, 3, 4, 5, 6]

mylist[1:4] = [7, 8, 9]

print(mylist)
```
