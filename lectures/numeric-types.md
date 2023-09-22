Numeric Types
=============

---

Numeric types are used to represent numbers in various forms

Python
------

Python includes three built-in numeric types:

- Integer
- Float
- Complex

Integer
-------

- Hold positive, negative and zero whole values
- Maps to the set of integers in mathematics
- Can hold arbitrarily large values

0, 100, -20, 1776

Float
-----

- Supports fractional values
- Has limited precision
- Includes special values for infinity and invalid results

0.0, 3.14159, -2.1, inf, NaN

Precision
---------

Scientific Notation
-------------------

- Numbers are represented as a fraction component multiplied by a base raised to a power

$6.02 \times 10^{23}$

Floating Point
--------------

- Uses representation related to floating point
- Fraction component has limited precision
- This causes many values to be represented imperfectly

```python
>>> 0.1 + 0.2
0.30000000000000004
```

Complex
-------

- Represents complex numbers
- Holds a real and imaginary component

```python
>>> (1 + 2j) + (3 + 1j)
(4+3j)
```

Type Conversion
---------------

- Types are converted to appropriate matching types before performing numeric operations
- If any operands are floats, the result will be a float

```python
>>> 1 + 1
2
>>> 1 + 1.0
2.0
>>> 1.5 + 3
4.5
```

Advanded Numeric Operations
---------------------------

- `**` - Power
- `//` - Floor division
- `%` - Modulus

Power
-----

- Raises a value to a power

```python
>>> 2 ** 3
8
>>> 4 ** -1
0.25
```

Floor Division
--------------

- Yields whole part of quotient
- Also called integer division

```python
>>> 8 // 2
4
>>> 9 // 2
4
```

Modulus
-------

- Yields the remainder from division

```python
>>> 8 % 2
0
>>> 9 % 2
1
```
