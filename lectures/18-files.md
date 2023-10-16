Lab Questions
=============

Files
=====

---

![Basic Computer Architecture](https://www.py4e.com/images/arch.png)

Storage
-------

- Instructions are executed by the CPU
- Values used so far live in main memory

Persistence
-----------

- Main memory is cleared when unpowered
- Long-term storage must use secondary memory

Files
-----

- Files are the abstraction used for long-term storage
- Files are typically organized in a hierarchy
- Files typically have human-readable names

Opening Files
-------------

- The `open` function may be used to open a file
- It requires a filename as a parameter
- It returns a file handle 

---

![File Handle](https://www.py4e.com/images/handle.png)

Read Example
------------

```python
file_handle = open("myfile.txt")

contents = file_handle.read()

print(contents)
```

Closing Files
-------------

- When we are finished with a file, we should close it to free resources in our programs

Close Example
-------------

```python
file_handle = open("myfile.txt")

contents = file_handle.read()

file_handle.close()

print(contents)
```

Reading Closed File
-------------------

```python
file_handle = open("myfile.txt")

file_handle.close()

contents = file_handle.read() # Raises Exception
```

Lines
-----

- Plain text may be separated into lines for easier consumtion
- Lines are separated by a special character called a newline
- We can create a newline character in Python using a `\n` escape sequence

Example
-------

```python
print("Line 1\nLine 2")
```

Reading Lines
-------------

- It may be helpful to read a file one line at a time
- Paragraphs may be represented this way in documents
- Data formats may use lines to separate records

Reading Lines
-------------

- The `readline` method will return the next line as a string value
- The `readlines` method will return an interable of all lines
- The file handle can be iterated directly to operate on lines

Example
-------

```python
handle = open("example.py")

first_line = handle.readline()

print(first_line)
```

Example
-------

```python
handle = open("example.py")

for line in handle:
    print(line, end='')
```

Key Ideas
---------

- Main memory is volatile and files provide non-volatile storage
- We can use the `open` function to get a file handle
- We can use `read` to load a string from a file