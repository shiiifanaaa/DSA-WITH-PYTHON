
# Day 04 - Big O Notation

## 1. What is Big O Notation?

Big O notation describes the upper-bound growth rate of an algorithm's time or space requirements as input size increases.

It helps us understand how an algorithm performs for larger inputs.

## 2. Common Big O Complexities

### O(1) - Constant Time

The execution time remains constant regardless of input size.

Example:

numbers = [10, 20, 30, 40]
print(numbers[0])

### O(n) - Linear Time

Execution grows proportionally with input size.

Example:

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

### O(n²) - Quadratic Time

Execution grows proportionally to the square of input size.

Example:

for i in range(n):
    for j in range(n):
        print(i, j)

## 3. Comparison

| Complexity | Meaning | Example |
|---|---|---|
| O(1) | Constant | Accessing an element |
| O(n) | Linear | Traversing a list |
| O(n²) | Quadratic | Nested loops |

## 4. Practice Questions

1. Accessing the first element of a list.
   Answer: O(1)

2. Printing every element in a list.
   Answer: O(n)

3. Using two nested loops.
   Answer: O(n²)

## 5. Key Takeaways

- O(1) does not depend on input size.
- O(n) grows linearly.
- O(n²) grows quadratically.
- Lower growth rates are generally preferable for large inputs.


