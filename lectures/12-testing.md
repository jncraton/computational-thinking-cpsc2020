# Important Dates

## Exam 1

- February 20th
- In-class Canvas exam
- May use a single-page, hand-written note sheet

# Testing

---

How do we know if software works?

---

> Software testing is the act of checking whether software satisfies expectations.

## Testing

- Determines correctness in some scenarios
- Will not find all bugs

---

```python
def square(n):
    return n*n
```

How do we know if this code works?

## Test Cases

- We can confirm known outputs
- `assert` is a simple tool for this
- `assert` will raise an exception if its input expression if `false`

## assert

```python
assert(1==1) # Confirms that 1 is 1
assert(1==2) # Raises AssertionError
```

## Square with Tests

```python
def square(n):
    return n*n

assert(square(0) == 0)
assert(square(1) == 1)
assert(square(2) == 4)
assert(square(25) == 625)
```

## Types of Tests

- Unit - Tests individual parts of the system
- Integration - Tests components integrated from smaller components
- End-to-end - Tests an entire system

---

![Testing Pyramid](https://upload.wikimedia.org/wikipedia/commons/a/a4/Testing_Pyramid.png)

# Lab Feedback
