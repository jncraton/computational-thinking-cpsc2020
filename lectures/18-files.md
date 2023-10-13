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
