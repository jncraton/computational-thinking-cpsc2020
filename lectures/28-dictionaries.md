# Iterating over Dictionaries

## Iterating over Keys

- The native method to iterate over a dictionary using for will iterate over keys

## Example

```python
d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key)
```

## Iterating over Values

- It is sometimes useful to access just values from a dictionary
- The `values` method can be used to get values as an iterable
- Alternatively, we can access values by their key

## Example

```python
d = {"a": 1, "b": 2, "c": 3}

for value in d.values():
    print(value)
```

## Example

```python
d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(d[key])
```

## Working Problems

- Professional developers will frequently be asked to solve simple programming tasks in interviews
- Example problems
  - [Kattis](https://open.kattis.com/)
  - [LeetCode](https://leetcode.com/problemset/all/)
  - [Project Euler](https://projecteuler.net/archives)
