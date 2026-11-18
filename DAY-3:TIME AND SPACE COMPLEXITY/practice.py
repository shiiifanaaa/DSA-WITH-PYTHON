
# DAY 3 - TIME AND SPACE COMPLEXITY

# --------------------------------------------------
# PROGRAM 1: Single statement - O(1)
# Explanation:
# A fixed number of operations are performed.
# Execution does not depend on input size.

number = 10

print(number)

# Time Complexity: O(1)


# --------------------------------------------------
# PROGRAM 2: Single loop - O(n)
# Explanation:
# The loop executes n times.
# If n increases, the number of operations increases.

n = 5

for i in range(n):
    print(i)

# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 3: Nested loop - O(n^2)
# Explanation:
# The outer loop executes n times.
# For each outer iteration, the inner loop executes n times.
# Total iterations = n * n.

n = 3

for i in range(n):
    for j in range(n):
        print(i, j)

# Time Complexity: O(n^2)


# --------------------------------------------------
# PROGRAM 4: Two separate loops - O(n)
# Explanation:
# Both loops execute n times.
# Total operations = n + n = 2n.
# Big O ignores constant factors.
# Therefore, complexity is O(n), not O(2n).

n = 5

for i in range(n):
    print(i)

for j in range(n):
    print(j)

# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 5: Constant space - O(1)
# Explanation:
# Only a fixed number of variables are used.
# Memory usage does not grow with input size.

a = 10
b = 20
total = a + b

print(total)

# Space Complexity: O(1)


# --------------------------------------------------
# PROGRAM 6: Linear space - O(n)
# Explanation:
# A list stores n elements.
# As the number of elements increases,
# the memory required also increases.

n = 5

numbers = []

for i in range(n):
    numbers.append(i)

print(numbers)

# Space Complexity: O(n)


# --------------------------------------------------
# PROGRAM 7: Loop with constant number of iterations
# Explanation:
# The loop always executes 5 times.
# It does not depend on n.

for i in range(5):
    print(i)

# Time Complexity: O(1)
