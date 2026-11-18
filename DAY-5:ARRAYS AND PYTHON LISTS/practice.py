
# DAY 5 - ARRAYS AND PYTHON LISTS

# --------------------------------------------------
# PROGRAM 1: Create a list
# Explanation:
# A list stores multiple elements in a single variable.

numbers = [10, 20, 30, 40, 50]

print(numbers)


# --------------------------------------------------
# PROGRAM 2: Access list elements
# Explanation:
# Indexing starts from 0.
# Negative indexing starts from the end.
# -1 represents the last element.

numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])
print("Third:", numbers[2])
print("Last:", numbers[-1])


# --------------------------------------------------
# PROGRAM 3: Update an element
# Explanation:
# Lists are mutable, meaning their elements can be changed.
# We use the index to update an element.

numbers = [10, 20, 30, 40]

numbers[1] = 25

print(numbers)


# --------------------------------------------------
# PROGRAM 4: Insert an element
# Explanation:
# insert(index, value) adds an element at a specific position.
# Existing elements shift to the right.

numbers = [10, 20, 30, 40]

numbers.insert(2, 25)

print(numbers)


# --------------------------------------------------
# PROGRAM 5: Append an element
# Explanation:
# append() adds a new element at the end of a list.

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# --------------------------------------------------
# PROGRAM 6: Remove an element
# Explanation:
# remove() deletes the first matching value.

numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)


# --------------------------------------------------
# PROGRAM 7: Pop an element
# Explanation:
# pop() removes the last element by default.
# It can also remove an element using its index.

numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)

numbers.pop(1)

print(numbers)


# --------------------------------------------------
# PROGRAM 8: Find the length of a list
# Explanation:
# len() returns the total number of elements.

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))


# --------------------------------------------------
# PROGRAM 9: Check whether an element exists
# Explanation:
# The 'in' operator checks whether a value exists.
# It returns True or False.

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)


# --------------------------------------------------
# PROGRAM 10: List slicing
# Explanation:
# Slicing extracts a portion of a list.
# The ending index is excluded.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
