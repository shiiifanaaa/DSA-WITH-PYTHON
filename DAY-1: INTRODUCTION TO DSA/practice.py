
# DAY 1 - INTRODUCTION TO DSA
# Topic: Basic Problem Solving and Algorithms

# --------------------------------------------------
# PROGRAM 1: Find the sum of two numbers
# Explanation:
# An algorithm is a step-by-step procedure to solve
# a problem. Here, we add two numbers using +.

a = 15
b = 25

total = a + b

print("Sum:", total)

# Output: Sum: 40


# --------------------------------------------------
# PROGRAM 2: Find the largest of two numbers
# Explanation:
# We use an if-else condition to compare two numbers.
# If a is greater, print a; otherwise, print b.

a = 25
b = 40

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

# Output: Largest: 40


# --------------------------------------------------
# PROGRAM 3: Find the smallest of two numbers
# Explanation:
# Compare two numbers using the less-than operator.

a = 12
b = 8

if a < b:
    print("Smallest:", a)
else:
    print("Smallest:", b)

# Output: Smallest: 8


# --------------------------------------------------
# PROGRAM 4: Check whether a number is even or odd
# Explanation:
# A number is even if it is divisible by 2.
# The modulo operator (%) gives the remainder.
# If remainder is 0, the number is even.

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output: Odd


# --------------------------------------------------
# PROGRAM 5: Find the sum of three numbers
# Explanation:
# Add three numbers and store the result in total.

a = 10
b = 20
c = 30

total = a + b + c

print("Total:", total)

# Output: Total: 60


# --------------------------------------------------
# PROGRAM 6: Swap two numbers
# Explanation:
# Swapping means exchanging the values of two variables.
# Python allows swapping without using a third variable.

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# Output:
# a = 20
# b = 10
