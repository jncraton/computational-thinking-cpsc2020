Dictionaries
============

List
----

- Lists map numbers to values
- Lists are *dense*, meaning number from 0 up to the list lenght all map to a value

Dictionaries
------------

- Can also map numbers to values
- Can be *sparse* meaning they don't need to map all possible values
- Created using curly braces `{}`

Example
-------

```python
values = {}

values[0] = "a"
values[2] = "b"

print(values[2])
```

Hashable Types
--------------

- An object is hashable if it has a hash value which never changes during its lifetime and can be compared to other objects
- Hashable objects which compare equal must have the same hash value
- Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally

Dictionary Keys
---------------

- Integers may be used as keys
- Strings may be used as keys
- Any other hashable type may be used as a key