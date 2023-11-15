Regular Expressions
===================

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

Extraction
----------

- Parens `()` can be used to indicate which portion of an expression to extract

Example
-------

```python
import re

text = "1234515a5"

print(re.findall("(.)5", text))
```

Exact counts
------------

- Brackets `{}` can be used to specify an exact count on the preceding character class

Example
-------

```python
import re

text = "46012 765 46013"

zips = re.findall("\d{5}", text)

print(zips)
```

Example
-------

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