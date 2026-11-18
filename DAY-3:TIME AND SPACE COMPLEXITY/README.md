
# Day 03 - Time and Space Complexity

## 1. What is Time Complexity?

Time complexity describes how the execution time of an algorithm grows as the input size increases.

It does not measure exact seconds. It describes the growth in the number of operations.

## 2. What is Space Complexity?

Space complexity describes how much memory an algorithm requires as the input size increases.

It includes memory used by variables and additional data structures.

## 3. Input Size

Input size is the amount of data given to an algorithm.

Example:

numbers = [10, 20, 30, 40, 50]

Here, input size n = 5.

## 4. Examples of Time Complexity

### Example 1: Single Statement

a = 10
print(a)

Time Complexity: O(1)

Reason: The number of operations does not depend on input size.

### Example 2: Single Loop

for i in range(n):
    print(i)

Time Complexity: O(n)

Reason: The loop executes n times.

### Example 3: Nested Loop

for i in range(n):
    for j in range(n):
        print(i, j)

Time Complexity: O(n²)

Reason: The inner loop executes n times for every outer loop iteration.

## 5. Examples of Space Complexity

### Example 1

a = 10
b = 20

Space Complexity: O(1)

Reason: Only a fixed number of variables are used.

### Example 2

numbers = [1, 2, 3, 4, 5]

Space Complexity: O(n)

Reason: Memory usage grows with the number of elements.

## 6. DSA Practice Questions

1. Identify the time complexity of a single print statement.
   Answer: O(1)

2. Identify the complexity of a loop running n times.
   Answer: O(n)

3. Identify the complexity of two nested loops running n times each.
   Answer: O(n²)

## 7. Key Takeaways

- Time complexity measures growth in execution operations.
- Space complexity measures memory requirements.
- Input size is represented by n.
- Complexity helps compare algorithms.
