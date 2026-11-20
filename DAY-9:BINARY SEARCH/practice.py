
# DAY 9 - BINARY SEARCH

# IMPORTANT:
# Binary search works only with sorted lists.


# 1. Search for an element in a sorted list

numbers = [10, 20, 30, 40, 50, 60, 70]

target = 60

low = 0

high = len(numbers) - 1

position = -1

while low <= high:

    mid = (low + high) // 2

    print("Checking index:", mid)
    print("Checking value:", numbers[mid])

    if numbers[mid] == target:

        position = mid

        break

    elif target < numbers[mid]:

        high = mid - 1

    else:

        low = mid + 1

if position != -1:

    print("1. Element found at index:", position)

else:

    print("1. Element not found")


# 2. Search for a target that is absent

target = 25

low = 0

high = len(numbers) - 1

position = -1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:

        position = mid

        break

    elif target < numbers[mid]:

        high = mid - 1

    else:

        low = mid + 1

if position != -1:

    print("2. Target found at index:", position)

else:

    print("2. Target not found")


# 3. Compare linear and binary search

target = 70

# Linear search

linear_checks = 0

for i in range(len(numbers)):

    linear_checks += 1

    if numbers[i] == target:

        break


# Binary search

binary_checks = 0

low = 0

high = len(numbers) - 1

while low <= high:

    binary_checks += 1

    mid = (low + high) // 2

    if numbers[mid] == target:

        break

    elif target < numbers[mid]:

        high = mid - 1

    else:

        low = mid + 1


print("3. Linear search checks:", linear_checks)

print("Binary search checks:", binary_checks)

