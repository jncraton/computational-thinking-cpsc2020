Nested Conditional Execution
============================

Nesting Conditionals
--------------------

- We can nest blocks of code
- Conditional execution can be nested to create more complex control flow

Example
-------

```python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```

---

![Nested Control Flow Diagram](https://www.py4e.com/images/nested.svg){height=540px}

Exit
----

- `exit` can be used to immediately terminate a program.

