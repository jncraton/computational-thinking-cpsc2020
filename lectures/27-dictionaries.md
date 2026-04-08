---
reading: '[PY4E: Dictionaries](https://www.py4e.com/html3/09-dictionaries)'
...

# Vulnerability Research

---

[Ignore TCP SACK packets with invalid sequence numbers](https://github.com/openbsd/src/commit/0e8206e596add74fef1653b4472de6b3723c435f)

---

[nfsd: fix heap overflow in NFSv4.0 LOCK replay cache](https://github.com/torvalds/linux/commit/5133b61aaf437e5f25b1b396b14242a6bb0508e2)

---

What do these fixes have in common?

---

> I’ve found more bugs in the last couple of weeks than I found in the rest of my life combined. [...] For OpenBSD, we found a bug that’s been present for 27 years, where I can send a couple of pieces of data to any OpenBSD server and crash it.

[Nicholas Carlini (Anthropic)](https://www.youtube.com/watch?v=INGOC6-LLv0)

---

> Mythos Preview has already found thousands of high-severity vulnerabilities, including some in every major operating system and web browser. Given the rate of AI progress, it will not be long before such capabilities proliferate, potentially beyond actors who are committed to deploying them safely.

[Project Glasswing](https://www.anthropic.com/glasswing)

---

> I think we’re living in the last fleeting moments where there’s any uncertainty that AI agents will supplant most human vulnerability research. Enjoy it, if that’s your thing, while you can. It’s not going to last.

[Thomas Ptacek](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/)

# Dictionaries

## List

- Lists map numbers to values
- Lists are _dense_, meaning numbers from 0 up to the list length all map to a value

## Dictionaries

- Can also map numbers to values
- Can be _sparse_ meaning they don't need to map all possible values
- Created using curly braces `{}`

## Example

```python
values = {}

values[0] = "a"
values[2] = "b"

print(values[2])
```

## Hashable Types

- An object is hashable if it has a hash value which never changes during its lifetime and can be compared to other objects
- Hashable objects which compare equal must have the same hash value
- Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally

## Dictionary Keys

- Integers may be used as keys
- Strings may be used as keys
- Any other hashable type may be used as a key

## Example

```python
values = {}

values["a"] = 1
values["b"] = 2

print(values["a"])
```

## Exercise

Create a program that builds a dictionary that maps the days of the week to the time you need to wake up on these days.

## Printing Dictionaries

- Dictionaries can be printed directly
- They will show value mapping between curly braces `{}`

## Example

```python
values = {}

values["a"] = 1
values["b"] = 2

print(values)
```

## Instantiating Dictionaries with Values

- The output format from the previous example can be used to create new lists directly

## Example

```python
values = {"a": 1, "b": 2}

print(values)
```

## Whitespace

- Whitespace may be used inside dictionary declarations
- New lines may be used to organize declarations

## Example

```python
poketypes = {
    "Charmander": "fire",
    "Squirtle": "water",
    "Bulbasaur": "grass",
}

print(f"Squirtle is {poketypes['Squirtle']} type")
```

## in

- The `in` operator can be used
- `in` will return True if the key exist in the dictionary

## Example

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

## Exercise

Create a program that can count the number of occurrences of each word in a text

```python
text = """
  In the beginning was the Word,
  and the Word was with God,
  and the Word was God.
"""
```

## Solution

<!--

```python
text = """
  In the beginning was the Word,
  and the Word was with God,
  and the Word was God.
"""

counts = {}

for word in text.split():
    word = word.strip(",.")

    if not word in counts:
        counts[word] = 0

    counts[word] += 1

print(counts)
```

-->
