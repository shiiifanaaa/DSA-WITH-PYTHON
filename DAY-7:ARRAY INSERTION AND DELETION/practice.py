
# DAY 1 - ARRAY INSERTION AND DELETION
# Topic: Insertion, Deletion and Finding Position


# 1. INSERT AN ELEMENT AT THE BEGINNING

numbers = [20, 30, 40, 50]

# Insert 10 at index 0
numbers.insert(0, 10)

print("1. After insertion at beginning:", numbers)


# 2. INSERT AN ELEMENT AT THE END

numbers = [10, 20, 30, 40]

# Append 50 at the end
numbers.append(50)

print("2. After insertion at end:", numbers)


# 3. INSERT AN ELEMENT AT A PARTICULAR POSITION

numbers = [10, 20, 40, 50]

# Insert 30 at index 2
numbers.insert(2, 30)

print("3. After insertion at index 2:", numbers)


# 4. DELETE AN ELEMENT BY VALUE

numbers = [10, 20, 30, 40, 50]

# Remove the value 30
numbers.remove(30)

print("4. After removing 30:", numbers)


# 5. DELETE AN ELEMENT BY INDEX

numbers = [10, 20, 30, 40, 50]

# Remove the element at index 2
removed = numbers.pop(2)

print("5. Removed element:", removed)
print("Updated list:", numbers)


# 6. DELETE THE LAST ELEMENT

numbers = [10, 20, 30, 40, 50]

# pop() without an index removes the last element
numbers.pop()

print("6. After deleting last element:", numbers)


# 7. FIND THE POSITION OF AN ELEMENT

numbers = [10, 20, 30, 40, 50]

target = 40

if target in numbers:

    position = numbers.index(target)

    print("7. Element found at index:", position)

else:

    print("7. Element not found")


# 8. COUNT HOW MANY TIMES AN ELEMENT APPEARS

numbers = [10, 20, 10, 30, 10, 40]

target = 10

count = numbers.count(target)

print("8. Number of occurrences:", count)


# 9. DELETE AN ELEMENT ONLY IF IT EXISTS

numbers = [10, 20, 30, 40, 50]

target = 30

if target in numbers:

    numbers.remove(target)

    print("9. Updated list:", numbers)

else:

    print("9. Element not present")


# 10. FIND THE INDEX OF A PARTICULAR ELEMENT

numbers = [5, 10, 15, 20, 25]

target = 15

for i in range(len(numbers)):

    if numbers[i] == target:

        print("10. Target found at index:", i)

        break


