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
