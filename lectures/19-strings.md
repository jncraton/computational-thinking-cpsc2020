---
reading: '[PY4E: Strings](https://www.py4e.com/html3/06-strings)'
...

## Group Advising

- For first year majors
- October 15th @ 6pm in 346

# Strings

## Definition

- A string is a sequence of characters
- String literals can be created using single or double quotes

## Valid Strings

```python
"Hello, world"
'Hello, world'
""
''
"a"
'b'
```

## Accessing Items

- A string is a sequence
- Items in the sequence can be accessed using square brackets `[]`

## Example

```python
>>> name = "Jordan"
>>> name[0]
'J'
>>> name[2]
'r'
```

---

![Indexing starts from 0](https://www.py4e.com/images/string.svg){height=540px}

## Immutability

- Strings in Python are immutable
- This means they cannot be changed

## Example

```python
>>> word = "cat"
>>> word[0]
'c'
>>> word[0] = "b"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## Creating a New String

- If we need to change a string we must create a new modified version
- This can be accomplished using string expressions

---

```python
>>> word = "cat"
>>> word = "b" + word[1] + word[2]
>>> word
'bat'
```

## Looping

- Strings are iterable
- We can easily loop over the characters in a string using `for`

## Example

```python
dna = "GGTGTACGGC"

guanine_count = 0

for base in dna:
    if base == 'G':
        guanine_count += 1

print("Guanine bases:", guanine_count)
```

## in

- The `in` operator can be used with strings
- An `in` expression will return true if the value on the left is contained within the value on the right

## Example

```python
>>> "a" in "cat"
True
>>> "b" in "cat"
False
>>> "bat" in "batman"
True
>>> "ant" in "batman"
False
```

## String comparison

- Comparison operators are defined for strings
- `==` checks for equality as expected
- `<` and `>` are a little more complicated

## Example

```python
>>> "cat" == "cat"
True
>>> "cat" == "bat"
False
>>> "bat" == "batman"
False
```

## Alphabetical order

- Generally, comparison operators can be used to confirm whether strings are in alphabetical order
- All uppercase letters come before all lowercase letter

## Example

```python
>>> "bat" < "cat"
True
>>> "cat" > "bat"
True
>>> "bat" < "Cat"
False
>>> "1" < "2"
True
>>> "12" < "102"
False
```

---

Create a program to print every other letter in a string

---

Create a program to find a word in a string and print the position of the word

## Solution

```python
sentence = "the quick brown fox jumped over the lazy dog"
word = "fox"

for sent_idx in range(0, len(sentence)):
    for word_idx in range(len(word)):
        if sentence[sent_idx + word_idx] != word[word_idx]:
            break
    else:
        print(sent_idx)
```
