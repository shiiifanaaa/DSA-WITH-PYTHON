
# DAY 8 - LINEAR SEARCH

# 1. Search for an element in a list

numbers = [10, 20, 30, 40, 50]

target = 30

found = False

for i in range(len(numbers)):

    if numbers[i] == target:

        print("1. Element found at index:", i)

        found = True

        break

if not found:
    print("1. Element not found")


# 2. Search when the target is absent

target = 90

found = False

for i in range(len(numbers)):

    if numbers[i] == target:

        print("2. Element found at index:", i)

        found = True

        break

if not found:
    print("2. Target is not present")


# 3. Count how many times an element appears

values = [5, 2, 5, 8, 5, 10, 2]

target = 5

count = 0

for value in values:

    if value == target:

        count += 1

print("3. Number of occurrences:", count)


# 4. Find all indexes where target appears

target = 2

indexes = []

for i in range(len(values)):

    if values[i] == target:

        indexes.append(i)

print("4. Indexes of target:", indexes)


# 5. Find the first index without using index()

target = 8

position = -1

for i in range(len(values)):

    if values[i] == target:

        position = i

        break

if position != -1:

    print("5. First index:", position)

else:

    print("5. Target not found")

