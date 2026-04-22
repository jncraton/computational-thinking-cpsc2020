# DFAs

## Chomsky Hierarchy

Grammar Automaton (Computer)

---

Unrestricted Turing Machines
Context Free Pushdown Automata
Regular Finite State Automata

## Regular Languages

- Are insufficient to parse most programming languages
- Can be processed by a simple finite automaton

## Deterministic Finite Automaton (DFA)

- Finite set of states $Q$
- Finite set of input symbols called the alphabet $\Sigma$
- Transition function $\delta : Q \times \Sigma \rightarrow Q$
- Initial or start state $q_0 \in Q$
- Set of accept states $F \subseteq Q$

## Drawing DFAs

- States are nodes on the graph
- Start state indicated by arrow
- Accept states indicated by double border
- Transitions indicated as labeled arrows

---

![DFA to accept string containing an even number of zeroes](https://upload.wikimedia.org/wikipedia/commons/9/9d/DFAexample.svg){height=540px}

# Regular Expressions

## Counting Characters

- Count modifiers can be appended to character classes
- One more more can be matched using `+`
- Zero or more can be matched using `*`

## Exercise

Create a single, concise regular expression to match a string with 0 or more `a`'s followed by at least 1 `b` followed by at least 1 `c`. Examples:

- `abc`
- `bc`
- `aabbcc`

These should not match:

- `acb`
- `ac`

## match

- Match will return `True` if a string matches from the beginning

## Example

```python
import re

words = "cats"

if re.match("cat", words):
    print("The strings match")
```

## Search

- We have seen that regular expressions can be used for search using `match` or `search`

## Example

```python
import re

num = "1387562"

if re.search("7", num):
    print("Number includes a 7")
```

## Data Extraction

- Regular expressions can be used to extract many matches
- The `findall` function can be used for this purpose

## Example

```python
import re

message = "My number is 7655551234 and his is 7655556789"

numbers = re.findall("765.......", message)

for number in numbers:
    print(number)
```

## Metacharacters

- Certain characters, such as `.` are not matched literally
- The full list of metachars is:

`. ^ $ * + ? { } [ ] \ | ( )`

## Character classes

- We can search for groups of characters to match against a single character using `[]`
- We can use "`-`" to indicate a range of characters

## Example

```python
import re

message = "Hi, alice@example.com. My email is bob@example.com"

emails = re.findall("[a-z]+@[a-z]+.com", message)

for email in emails:
    print(email)
```

## Common Classes

- `\d` - any decimal digit
- `\s` - any whitespace
- `\S` - any non-whitespace
- `\w` - any alphanumeric

## Example

```python
import re

text = "What is 123 + 456?"

nums = re.findall("\d+", text)

print(nums)
```

## Fuzzy matching

- We can use more permissive expressions to capture values in multiple formats

## Example

```python
import re

phone_nums = """
(765) 555 1234
317-555-6789
76555551357
"""

matches = re.findall("[\d\(\)\- ]+", phone_nums)

print(matches)
```

## Substitutions

- `sub` can be used to perform regex replacements

## Example

```python
import re

phone_nums = """
(765) 555 1234
317-555-6789
76555551357
"""

matches = re.findall("[\d\(\)\- ]+", phone_nums)

cleaned = [re.sub("[ \-\(\)]", "", m) for m in matches]

print(cleaned)
```

## Extraction

- Parens `()` can be used to indicate which portion of an expression to extract

## Example

```python
import re

text = "1234515a5"

print(re.findall("(.)5", text))
```

## Exact counts

- Brackets `{}` can be used to specify an exact count on the preceding character class

## Example

```python
import re

text = "46012 765 46013"

zips = re.findall("\d{5}", text)

print(zips)
```

## Example

```python
import re

addresses = """
Anderson, IN
Chicago, IL
Indianapolis, IN
"""

cities = re.findall("(.*), [A-Z]{2}", addresses)

print(cities)
```

## Match Objects

- `search` returns a match object on success
- Groups can be extracted from the match

## Example

```python
import re

text = "a1 b2 c3"

match = re.search("b(\d)", text)

print(match.groups())
print(match.group(1))
```

## Group 0

- Match group `0` is always the full match

## Example

```python
import re

text = "cat dog bat"

match = re.search("b([a-z])t", text)

print(match.group(0))
```

## More RE Information

- [RE How-to](https://docs.python.org/3/howto/regex.html)
- [Py4E Chapter](https://www.py4e.com/html3/11-regex)
