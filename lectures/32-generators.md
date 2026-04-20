# Generator Expressions

## List Comprehensions

- List comprehensions can be used to quickly build a new list from an existing list

## Example

```python
nums = list(range(10))
odds = [n for n in nums if n % 2 == 1]

print(odds)
```

## Generator Expressions

- The expression inside a list comprehension is known as a generator expression
- These can be used in other contexts

## Example

```python
nums = list(range(10))
odds = (n for n in nums if n % 2 == 1)

print(odds)
```

## Generators

- A `generator` object is an iterable that can only be iterated once
- The object cannot be index like a list
- Value are created just in time for their use

## Example

```python
squares = (n*n for n in range(2, 5))

print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
```

## for

- Generator expressions can be iterated using `for`

## Example

```python
words = "lorem ipsum dolor sit amet".split()

first_letters = (w[0] for w in words)

for letter in first_letters:
    print(letter)
```

## Creating Dictionaries

- We can create dictionaries from pairs of values using the `dict` constructor
- This technique can be combined with generator expressions

## Example

```python
words = ["apple", "boy", "carrot"]

letter_words = dict((w[0], w) for w in words)

print(letter_words)
```

## Dictionary Comprehension

- Dictionaries can be quickly created using specialized [dictionary comprehension](https://peps.python.org/pep-0274/) syntax

## Example

```python
words = ["apple", "boy", "carrot"]

letter_words = {w[0]: w for w in words}

print(letter_words)
```

## Custom Generators

- The `yield` keyword can be used to emit values from generators
- Custom generators look like functions but maintain their state between yielding values

## Example

```python
def myrange(start, stop, step):
    i = start

    while i < stop:
        yield i
        i += step

for i in myrange(1, 10, 2):
    print(i)
```

## Exercise

Create a generator that will yield every odd number that is not divisible by 5.
