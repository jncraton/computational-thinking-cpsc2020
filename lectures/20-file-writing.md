File Writing
============

File Handles
------------

- Provide an interface to work with an open file
- Common operations include reading, writing, and closing

Reading
-------

- Open a file with default file mode (read)
- Use the read method to move text content from the file to a string

Example
-------

```python
pyfile = open("example.py")

source = pyfile.read()

print(source)
```

Writing
-------

- Open a file with mode set to "w"
- Use the write method to write to the file

Example
-------

```python
outfile = open("myfile.txt", "w")

outfile.write("Hello, world")

outfile.close()
```

Closing
-------

- Files must be properly closed to ensure all data is correctly written

Example
-------

```python
outfile = open("myfile.txt", "w")

outfile.write("Hello, world")
```

Truncation
----------

- When a file is opened for writing, it is truncated by default
- This means all existing content will be destroyed

Appending
---------

- Files can be opened for appending using the "a" flag

Example
-------

```python
outfile = open("myfile.txt", "a")

outfile.write("Hello, world")

outfile.close()
```

Closing Files
-------------

- It is important to close files when we finish using them
- It can be easy to forget to do this
- `with` can be used to automatically close a file

Example
-------

```python
with open("myfile.txt", "w") as outfile:
    outfile.write("Hello, world")
```

with
----

- The `with` statement can be used with all [context manager types](https://docs.python.org/3/library/stdtypes.html#context-manager-types)
- File handles are one use, but there are money others
- `with` always closes the file, even when exceptions are raised

Example
-------

Write all primes up to 10,000 to a file