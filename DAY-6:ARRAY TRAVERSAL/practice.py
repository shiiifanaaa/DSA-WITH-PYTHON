
# DAY 6 - ARRAY TRAVERSAL

# --------------------------------------------------
# PROGRAM 1: Traverse and print all elements
# Explanation:
# Traversal means visiting each element one by one.
# The for loop accesses every element in the list.

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 2: Traverse using index
# Explanation:
# range(len(numbers)) generates valid list indices.
# We access elements using their index.

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print(numbers[i])

# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 3: Find the sum of array elements
# Explanation:
# Start total at zero.
# Add each element to total during traversal.

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Sum:", total)

# Output: 150
# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 4: Find the largest element
# Explanation:
# Assume the first element is the largest.
# Compare every element with maximum.
# Update maximum whenever a larger value is found.

numbers = [10, 45, 20, 60, 30]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Largest:", maximum)

# Output: 60
# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 5: Find the smallest element
# Explanation:
# Assume the first element is the smallest.
# Compare every element with minimum.
# Update minimum whenever a smaller value is found.

numbers = [10, 45, 20, 60, 30]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Smallest:", minimum)

# Output: 10
# Time Complexity: O(n)


# --------------------------------------------------
# PROGRAM 6: Count even and odd numbers
# Explanation:
# Use the modulo operator to check divisibility by 2.
# Maintain separate counters for even and odd numbers.

numbers = [10, 15, 20, 25, 30, 35]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)

# Output:
# Even Count: 3
# Odd Count: 3


# --------------------------------------------------
# PROGRAM 7: Search for an element
# Explanation:
# Linear search checks elements one by one.
# If the target matches an element, its position is printed.

numbers = [10, 20, 30, 40, 50]

target = 30
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if found == False:
    print("Element not found")

# Output: Element found at index: 2
# Time Complexity: O(n) worst case


# --------------------------------------------------
# PROGRAM 8: Reverse a list using traversal
# Explanation:
# Start from the last index and move backwards.
# Use a negative step in range().

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])

# Output:
# 50
# 40
# 30
# 20
# 10


# --------------------------------------------------
# PROGRAM 9: Calculate the average
# Explanation:
# First calculate the sum of all elements.
# Divide the sum by the total number of elements.

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average:", average)

# Output: Average: 30.0


# --------------------------------------------------
# PROGRAM 10: Count occurrences of a number
# Explanation:
# Traverse the list and compare every element
# with the target. Increase the counter when matched.

numbers = [10, 20, 10, 30, 10, 40]

target = 10
count = 0

for num in numbers:
    if num == target:
        count = count + 1

print("Occurrences:", count)

# Output: Occurrences: 3
