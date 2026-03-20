---
reading: '[PY4E: Files](https://www.py4e.com/html3/07-files)'
...

# Files

---

![Basic Computer Architecture](https://www.py4e.com/images/arch.png)

## Storage

- Instructions are executed by the CPU
- Values and variables as discussed so far live in main memory

## Persistence

- Main memory is cleared when unpowered
- Long-term storage must use secondary memory

---

![DRAM](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Pair32mbEDO-DRAMdimms.jpg/503px-Pair32mbEDO-DRAMdimms.jpg)

---

![Laptop HDD](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Laptop-hard-drive-exposed.jpg/627px-Laptop-hard-drive-exposed.jpg)

---

![HDD in Operation](https://upload.wikimedia.org/wikipedia/commons/c/cf/HDD_Startup_and_Shutdown.webm){height=540px}

---

![SATA SSD](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/2023_Dysk_SSD_Patriot_P210_2TB.jpg/622px-2023_Dysk_SSD_Patriot_P210_2TB.jpg)

---

![mSATA SSD](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Intel_525_mSATA_SSD.jpg/305px-Intel_525_mSATA_SSD.jpg)

---

![NVMe SSD](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/SSD_Samsung_960_PRO_512GB_-_front_and_back_-_2018-05-27.jpg/320px-SSD_Samsung_960_PRO_512GB_-_front_and_back_-_2018-05-27.jpg)

## Files

- Files are the abstraction used for long-term storage
- Files are typically organized in a hierarchy
- Files typically have human-readable names

## Opening Files

- The `open` function may be used to open a file
- It requires a filename as a parameter
- It returns a file handle

---

![File Handle](https://www.py4e.com/images/handle.png)

## Read Example

```python
file_handle = open("myfile.txt")

contents = file_handle.read()

print(contents)
```

## Closing Files

- When we are finished with a file, we should close it to free resources in our programs

## Close Example

```python
file_handle = open("myfile.txt")

contents = file_handle.read()

file_handle.close()

print(contents)
```

## Reading Closed File

```python
file_handle = open("myfile.txt")

file_handle.close()

contents = file_handle.read() # Raises Exception
```

## Lines

- Plain text may be separated into lines for easier consumption
- Lines are separated by a special character called a newline
- We can create a newline character in Python using a `\n` escape sequence

## Example

```python
print("Line 1\nLine 2")
```

## Reading Lines

- It may be helpful to read a file one line at a time
- Paragraphs may be represented this way in documents
- Data formats may use lines to separate records

## Reading Lines

- The `readline` method will return the next line as a string value
- The `readlines` method will return an iterable of all lines
- The file handle can be iterated directly to operate on lines

## Example

```python
handle = open("example.py")

first_line = handle.readline()

print(first_line)
```

## Example

```python
handle = open("example.py")

for line in handle:
    print(line, end='')
```

## Exercise

1. Create a plain text file with numbers on each line
2. Create a Python program that prints the sum of the numbers in the file

## Solution

```python
handle = open("myfile.txt")

total = 0
for line in handle:
    total += int(line)

print(total)
```

## Survey Example

## Key Ideas

- Main memory is volatile and files provide non-volatile storage
- We can use the `open` function to get a file handle
- We can use `read` to load a string from a file
