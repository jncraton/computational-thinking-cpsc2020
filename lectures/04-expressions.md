---
reading: '[Variables](https://www.py4e.com/html3/02-variables)'
...

Expressions
===========

Definition
----------

> An expression is a syntactic entity in a programming language that may be evaluated to determine its value. 
> 
> [Wikipedia](https://en.wikipedia.org/wiki/Expression_(computer_science))

Syntax
------

- Rules that define the combinations of symbols that are considered to be correctly structured
- There are certain symbols that can be combined in certain ways to produce correct expressions

Evaluation
----------

- Transformation of expression syntax to the value of the expression
- Form of computation

Example
-------

```python
1 + 1
```

Evaluation in Python
--------------------

- Expressions in programs are evaluated automatically
- Single expressions can be quickly evaluated using the [Shell](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)

---

![Thonny Shell](media/thonny-expression.png)

Literals
--------

- Basic components of expressions
- Evaluation yields on object of a given type

Binary Arithmetic Operators
---------------------------

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

Arithmetic Examples
-------------------

```python
>>> 3.4 + 1.1
4.5
>>> 4 - 3
1
>>> 6 * 3
18
>>> 12 / 4
3.0
```

Value
-----

- Result object yielded by an expression
- Has a type such as integer or string of characters
- Examples:
  - `"Hello, World!"` (string)
  - `7` (integer)

Types
-----

- Set of allowed values for an object
- Built-in examples include numbers and strings

Numbers
-------

- Numeric values

```python
2, 3.4, -1, 0
```

Strings
-------

- An ordered collection of characters
- Delineated by single or double quotes

```python
"Hello, world!", "1", ""
```

Order of Operations
-------------------

Follows conventions from algebra

1. Parenthetic subexpressions
2. Exponentiation
3. Multiplication and division
4. Addition and subtraction

Examples
--------

```python
>>> 2 * 3 + 1
7
>>> 1 + 4 / 2
3.0
>>> 2 * (3 + 1)
8
```

Comparison Operations
---------------------

- Always return `True` or `False`

| Operator | Name |
|----------|------|
| `<` | Less than |
| `>` | Greater than |
| `<=` |  Less than or equal |
| `>=` | Greater than or equal |
| `==` | Equal |
| `!=` | Not equal |

Examples
--------

```python
>>> 2 < 3
True
>>> 2 <= 3
True
>>> 2 == 3
False
>>> 2 != 3
True
```

Logical Operations
------------------

- Always return `True` or `False` when operating on `True` and `False` values
- Examples include:
  - `not`
  - `and`
  - `or`

And Truth Table
---------------

 A | B | Q
---|---|---
 F | F | F
 F | T | F
 T | F | F
 T | T | T

Or Truth Table
--------------

 A | B | Q
---|---|---
 F | F | F
 F | T | T
 T | F | T
 T | T | T

Examples
--------

```python
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> False or False
False
```

---

What is the truth table for the following expression?

```python
not ((not A) and (not B))
```

Order of Operations
-------------------

Follows conventions from algebra

1. Parenthetic subexpressions
2. Exponentiation
3. Multiplication and division
4. Addition and subtraction
5. Comparison
6. Logical operations

Official Documentation
----------------------

[Expressions in Python](https://docs.python.org/3/reference/expressions.html)