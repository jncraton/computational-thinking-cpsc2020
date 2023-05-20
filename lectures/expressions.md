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

Value
-----

- Result object yielded by an expression

Example
-------

```python
1 + 1
```

Atoms
-----

- Most basic elements of expressions
- Examples
  - Literals
  - Identifiers

Literals
--------

- Basic components of expressions
- Evaluation yields on object of a given type

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

Binary Arithmetic Operators
---------------------------

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

Order of Operations
-------------------

Follows conventions from algebra

1. Parenthetic subexpressions
2. Exponentiation
3. Multiplication and Division
4. Addition and Subtraction

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

Official Documentation
----------------------

[Expressions in Python](https://docs.python.org/3/reference/expressions.html)