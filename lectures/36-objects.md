Objects
=======

What is an object?
------------------

- Any data with state (attributes or value) and defined behavior (methods)

Common Objects
---------------

- `str`
- `int`
- `list`
- `range`

State
-----

- Objects are containers for state and behavior
- They may have a value
- They may have attributes

Functions
---------

- Functions are containers for behavior
- They do not typically also store state

Attribute and Method Access
---------------------------

- Attributes and methods are accessed using "`.`"

Attribute Example
-----------------

```python
r = range(1, 10, 2)

print(r.start)
print(r.stop)
print(r.step)
```

Methods
-------

- A function that is a member of an object
- When called as an attribute of an object, the function can operate on the object state

Method Example
--------------

```python
l = [3, 1, 4, 2, 5]

l.sort()
```

Class
-----

- A template for creating user-defined objects
- Class definitions normally contain method definitions which operate on instances of the class
- Class names are written in camel case by convention

Example
-------

```python
class Character:
    hp = 100

alice = Character()
print(alice.hp)
```

Method
------

- Function defined in the class body become attributes
- When called as attributes, these have access to the object instance

Example
-------

```python
class Vehicle:
    speed = 0
    
    def accelerate(self):
        self.speed += 1
        
car = Vehicle()
car.accelerate()
print(car.speed)
```

Constructor
-----------

- A special method may be called when creating a new object from a class
- This is called the constructor

Example
-------

```python
class Length:
    def __init__(self, meters):
        self.meters = meters
        self.feet = meters * 3.2808
        
l = Length(2)
print(l.feet)
```

self
----

- The first argument passed to a method will be a reference to the object instance
- `self` is chosen as the name for this parameter by convention
