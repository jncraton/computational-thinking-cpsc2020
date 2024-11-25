---
reading: '[PY4E: Regex](https://www.py4e.com/html3/11-regex)'
...

Vacuum Lab Review
-----------------

Regular Expressions
===================

find
----

- The string `find` method can be used to get the location of one string in another

Example
-------

```python
sent = "Where is the word 'the'?"

print(sent.find("the"))
```

split
-----

- The string `split` method can be used to split strings

Example
-------

```python
ip = "10.75.123.76"

octets = ip.split(".")

print(octets)
```

Regular Expressions
-------------------

- Available in the `re` module
- Provide their own mini language for parsing strings
- Useful for somewhat advanced string processing tasks

search
------

- The re `search` method can be used to find a matching span in a string
- Will return `None` if no match

Example
-------

```python
import re

zips = "46012, 46013 46014. 46015"

if re.search("46013", zips):
    print("46013 is present")
```

Character Matching
------------------

- By default, regular expressions match characters literally
- Some special character can create more complex matches
- For example `.` will match any character

Example
-------

```python
import re

words = "cat dog fox pig"

if re.search(".ox", words):
    print("A word ending in ox was found")
```

Counting Characters
-------------------

- Count modifiers can be appended to character classes
- One more more can be matched using `+`
- Zero or more can be matched using `*`

match
-----

- Match will return `True` if a string matches from the beginning

Example
-------

```python
import re

words = "cats"

if re.match("cat", words):
    print("The strings match")
```

Lab 7
-----