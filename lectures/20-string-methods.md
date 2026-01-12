# String Methods

## Methods

- Methods are functions that operate on a known piece of data
- Most operators are shortcuts to object methods

## Example

```python
>>> 1 + 2
3
>>> (1).__add__(2)
3
```

## dir

- `dir` can be used to list methods available on an object

## Example

```python
>>> dir(1)
['__abs__', '__add__', ...]
>>> dir("")
['__add__', ...]
```

## upper and lower

- `upper` can be used to uppercase a string
- `lower` can be used to lowercase it

## Example

```python
>>> a = "Hello, world!"
>>> a.lower()
'hello, world!'
>>> a.upper()
'HELLO, WORLD!'
```

---

How could we compare strings ignoring case?

## Solution

```python
color = input("Enter a color:")

if color.lower() == "red":
    print("Roses are red")
elif color.lower() == "blue":
    print("Violets are blue")
else:
    print("Unknown color")
```

## find

- `find` can be used to get the position of a substring
- Returns the index of the start of the substring
- Returns -1 if substring is not found

## Example

```python
>>> a = "Hello, world!"
>>> a.find("world")
7
```

## strip

- `strip` returns a copy of the string with leading and trailing whitespace removed

## Example

```python
>>> text = "    Hello, world!          "
>>> text.strip()
'Hello, world'
```

## startswith

- `startswith` will return True if the string begins with the supplied prefix

## Example

```python
>>> text = "Hello, world!"
>>> text.startswith("Hello")
True
>>> text.startswith("world")
False
```

## count

- `count` will count the number of non-overlapping substrings in some text

## Example

```python
>>> sentence = "The quick brown fox jumped over the lazy dog"
>>> sentence.count("o")
4
```

## Slicing

- String indexing in Python supports returning substrings as well as individual characters
- A colon (`:`) is used to separate the start and end index

## Example

```python
>>> alphabet = "abcdefghijklmnopqrstuvwxyz"
>>> alphabet[2:4]
'cd'
>>> alphabet[0:5]
'abcde'
>>> alphabet[2:2]
''
>>> alphabet[2:3]
'c'
```

## Negative Indexes

- In Python, it is legal for an index to be negative
- A negative index will index from the end of the object

## Example

```python
>>> text = "Hello, world!"
>>> text[-1]
'!'
>>> text[-2]
'd'
```

## Inferred indices

- If a start index is left out, it is assumed to be zero
- If an end index is left out, it is assumed to be negative 1

## Example

```python
>>> text = "Hello, world"
>>> text[2:]
'llo, world!'
>>> text[:-2]
'Hello, worl'
```

## Formatted String Literals

## format

- [Prior editions](https://github.com/csev/py4e/pull/424) of the textbook used the `format` method on strings
- It is antiquated and has largely been superseded by [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) since Python 3.6.
- You will not be required to use or understand the `format` method in this class

## f-strings

- Provide simple string formatting
- Python expressions can be included within strings
- An `f` should be used before the opening quote of the string literal

## Example

```python
>>> f"The answer is {7*6}"
```

## Example

```python
name = input("What is you name?")

print(f"Hello, {name}")
```

## Format Specifiers

- Can be added after an expression to adjust formatting
- This can be used for rounding or other purposes such as alignment

## Example

```python
num = 1

for pokemon in ["Charmander", "Charmeleon", "Charizard"]:
    print(f"{pokemon:12} {num}")
    num += 1
```

## Example

```python
import random

for _ in range(10):
    print(f"{random.random():.2f}")
```

---

Create a program that will capitalize the first word in a provided sentence.

## Solution

```python
sentence = "hello world"

sentence = sentence[0].upper() + sentence[1:]

print(sentence)
```

---

Create a program that will search a string for a word and display the word along with the 5 characters before and 5 characters after it.

## Solution

```python
sentence = "the quick brown fox jumped over the lazy dog"
word = "fox"

index = sentence.find(word)

print(sentence[index - 5: index + len(word) + 5])
```
