# DAY 4 - BIG O NOTATION

# --------------------------------------------------
# PROGRAM 1: O(1) - Access an element
# Explanation:
# Accessing an element using its index takes
# constant time in a Python list.

numbers = [10, 20, 30, 40, 50]

print(numbers[2])

# Output: 30
# Time Complexity: O(1)


# --------------------------------------------------
# PROGRAM 2: O(1) - Check the first element
# Explanation:
# Only one element is accessed regardless of list size.

numbers = [5, 10, 15, 20]

print(numbers[0])

# Output: 5
# Time Complexity: O(1)


# --------------------------------------------------
# PROGRAM 3: O(n) - Print all elements
# Explanation:
# Every element is visited exactly once.
# If there are n elements, the loop executes n times.

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 4: O(n) - Find a particular element
# Explanation:
# We check each element until the target is found.
# In the worst case, all n elements are checked.

numbers = [10, 20, 30, 40, 50]
target = 40

for num in numbers:
    if num == target:
        print("Element Found")
        break

# Time Complexity: O(n) worst case


# --------------------------------------------------
# PROGRAM 5: O(n^2) - Nested loops
# Explanation:
# The outer loop executes n times.
# The inner loop executes n times for each outer loop.
# Total operations = n * n.

n = 3

for i in range(n):
    for j in range(n):
        print(i, j)

# Time Complexity: O(n^2)


# --------------------------------------------------
# PROGRAM 6: O(n^2) - Print all pairs
# Explanation:
# Each element is paired with every other element,
# including itself in this example.

numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        print(i, j)

# Time Complexity: O(n^2)


# --------------------------------------------------
# PROGRAM 7: Compare complexity

# O(1): One operation
print("Hello")

# O(n): One loop
for i in range(5):
    print(i)

# O(n^2): Two nested loops
for i in range(3):
    for j in range(3):
        print(i, j)
