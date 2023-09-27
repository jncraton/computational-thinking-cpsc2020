Loop Patterns
=============

Construction
------------

- Initialize variable before the loop starts
- Perform computation on each loop item
- Examine variable after the loop completes

Counting
--------

Solution
--------

```python
count = 0

for i in [1, 3, 6, 10, 15, 21]:
    count = count + 1
    
print(count)
```

Sum
---

Solution
--------

```python
total = 0

for num in [1, 3, 6, 10, 15, 21]:
    total = total + num
    
print(total)
```

Counting and Summing
--------------------

- Helpful pattern to understand
- Can be easily replaced by `len` and `sum` in simple cases

Mean
----

Solution
--------

```python
total = 0
count = 0

for num in [1, 3, 6, 10, 15, 21]:
    total = total + num
    count = count + 1
    
mean = total / count

print("Total:", total, "Count:", count, "Mean:", mean)
```

---

Could we compute the mean without using a loop?

Solution
--------

```python
nums = [1, 3, 6, 10, 15, 21]

mean = sum(nums) / len(nums)

print("Mean:", mean)
```

Maximum and Minimum
-------------------

- Sometimes we want to compare one value to others
- Examples include finding a max or a min

Max
---

Solution
--------

```python
import math

nums = [1, 4, 7, 12, 3]
largest = -math.inf

for num in nums:
    if num > largest:
        largest = num

print(largest)
```

Min
---

Solution
--------

```python
import math

nums = [1, 4, 7, 12, 3]
smallest = math.inf

for num in nums:
    if num < smallest:
        smallest = num

print(smallest)
```

min function
------------

Solution
--------

```python
import math

def min(nums):
    smallest = -math.inf
    
    for num in nums:
        if num < smallest:
            smallest = num
            
    return num
```

Linear Search
-------------

- Sometimes we want to find a specifical value
- This can be accoplished by checking items one by one

Check if a word has no vowels
-----------------------------

Solution
--------

```python
word = input("Enter a word with no vowels:")
valid_word = True

for letter in word:
    for vowel in 'aeiou':
        if letter == vowel:
            valid_word = False
        
if valid_word:
    print("That's correct")
else:
    print("Your word included a vowel.")     
```
