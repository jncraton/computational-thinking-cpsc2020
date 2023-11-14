Regular Expressions
===================

Search
------

- We have seen that regular expressions can be used for search using `match` or `search`

Example
-------

```python
import re

num = "1387562"

if re.search("7", num):
    print("Number includes a 7")
```

Data Extraction
---------------

- Regular expressions can be used to extract many matches
- The `findall` function can be used for this purpose

Example
-------

```python
import re

message = "My number is 7655551234 and his is 7655556789"

numbers = re.findall("765.......", message)

for number in numbers:
    print(number)
```

Metacharacters
--------------

- Certain characters, such as `.` are not matched literally
- The full list of metachars is:

`. ^ $ * + ? { } [ ] \ | ( )`

Character classes
-----------------

- We can search for groups of characters to match against a single character using `[]`
- We can use "`-`" to indicate a range of characters

Example
-------

```python
import re

message = "Hi, alice@example.com. My email is bob@example.com"

emails = re.findall("[a-z]+@[a-z]+.com", message)

for email in emails:
    print(email)
```

Common Classes
--------------

- `\d` - any decimal digit
- `\s` - any whitespace
- `\S` - any non-whitespace
- `\w` - any alphanumeric

Example
-------

```python
import re

text = "What is 123 + 456?"

nums = re.findall("\d+", text)

print(nums)
```

Fuzzy matching
--------------

- We can use more permissive expressions to capture values in mutliple formats

Example
-------

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

Substitutions
-------------

- `sub` can be used to perform regex replacements

Example
-------

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
