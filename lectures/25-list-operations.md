# List Operations

## List + operator

- The `+` operator can be used to concatenate lists

## Example

```python
start = [1, 2]
end = [3, 4]
complete = start + end
print(complete)
```

## Appending

- The `+` operator may be used for appending
- Single items must be represented as a list of length 1

## Example

```python
mylist = [1,2,3]

# The following will raise an exception
mylist = mylist + 4

print(mylist)
```

## Exercise

Create a program that builds a list of 10 randomly generated numbers

## Solution

```python
import random

nums = []

for _ in range(10):
    nums += [random.randint(1,100)]

print(nums)
```

## List \* operator

- The `*` operator can be used to duplicate lists

## Example

```python
mylist = [1, 2, 3]
longlist = mylist * 20
print(longlist)
```

## Slicing

- Lists support slicing as used with strings
- Omitted values will be treated as the start and end of the list

## Example

```python
mylist = [1, 2, 3, 4, 5, 6]

print(mylist[1:4])
print(mylist[:4])
print(mylist[1:])
```

## Slices in assignment

- Slices can be used in the left hand side of an assignment

## Example

```python
mylist = [1, 2, 3, 4, 5, 6]

mylist[1:4] = [7, 8, 9]

print(mylist)
```

## Copying Lists

- Because lists are mutable, it can be useful to create copies
- The `copy` method can be used for this
- Slicing syntax (`[:]`) can also be used

## Example

```python
mylist = [1,2,3]
original = mylist.copy()

mylist = mylist + [4]

print(mylist, original)
```

## append

- The `append` method can be used to add an item to the end of a list
- If lists are passed to append, a nested list will be created

## Example

```python
mylist = [1,2,3]

mylist.append(4)

print(mylist)
```

## extend

- The `extend` method can add many elements to a list
- The argument passed in should be a list

## Example

```python
mylist = [1,2,3]

mylist.extend([4, 5, 6])

print(mylist)
```

## sort

- The `sort` method can be used to sort list elements in place
- The list will be modified by this operation
- `sort` always returns `None`

## Example

```python
mylist = [4, 1, 3, 2]

mylist.sort()

print(mylist)
```

## In-place modification

- It can be tempting to assign the result of sort back to the original list
- This is not desirable, as it will replace the value with `None`

## Example

```python
mylist = [4, 1, 3, 2]

mylist = mylist.sort()

print(mylist)
```

## Exercise

Create a Python program that prints the three largest numbers in a list

## Deleting Elements

- `pop` will remove and return an element at a position (or the last element by default)
- `del` can be used to remove the element without returning it (can use slices)
- `remove` will remove the element by value

## pop Example

```python
mylist = [1, 2, 3]

removed = mylist.pop(1)

print(mylist, removed)
```

## del Example

```python
mylist = [1, 2, 3]

del mylist[1]

print(mylist)
```

## remove Example

```python
mylist = [1, 2, 3]

mylist.remove(1)

print(mylist)
```

## Exercise

Create a Python program to remove all single-digit numbers from a list
