---
reading: '[PY4E: Iteration](https://www.py4e.com/html3/05-iterations)'
...

# Midterm Survey

# Iteration

## Assignment

- Variables can be assigned values

```python
x = 1
y = 1 + 2
```

## Updating Variables

- Sometimes we want to update the values in variables
- We can set variables to expressions that include those variables

```python
x = x + 1
```

## Increment and Decrement

- Increment is increase by 1
- Decrement is decrease by 1

```python
x = x + 1 # Increment
x = x - 1 # Decrement
```

## Augmented Assignment

We can shorten common reassignment using [augmented assignment](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements):

```python
x += 1 # Increment
x -= 1 # Decrement
```

## Recursion

- Functions can be use to create repetition in our programs

## Example

```python
def count_to_10_from(n):
    if n > 10:
        return

    print(n)
    count_to_10_from(n + 1)

count_to_10_from(0)
```

## while

- Repetition in programs is a common task
- We introduce `while` to perform operations multiple times

## Example

```python
while True:
    answer = input("What is the capital of France?")

    if answer == "Paris":
        print("That's correct!")
        exit()
    else:
        print("Not quite. Try again.")
```

## Indefinite iteration

- We do not specify how many times a `while` loop will execute in advance
- This makes iteration indefinite

## Controlling Iteration

- `while` accepts a conditional that will stop iteration when false
- This can be used to control how many times we iterate

## Counting

```python
i = 0

while i <= 10:
    print(i)
    i += 1
```

## Infinite Loop

- We must be careful to avoid looping forever
- A loop that never stops is called an infinite loop
- This is a common type of bug

## Infinite Loop

```python
i = 0

while True:
    print(i)
```

## break

- `break` can be used to terminate iteration
- Control moves to after the loop body

## Example

```python
i = 0

while True:
    if i > 10:
        break
    print(i)
    i = i + 1
```

## continue

- `continue` can be reused to skip the remainder of an iteration
- Control will return to the conditional on the while statement

## Example

```python
while True:
    num = input("Enter a number:")

    try:
        square = int(num) ** 2
    except ValueError:
        print("Invalid number")
        continue

    print(square)
```
