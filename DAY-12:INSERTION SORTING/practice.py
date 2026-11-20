
# DAY 12 - INSERTION SORT


# 1. Basic Insertion Sort (Ascending Order)

numbers = [5, 3, 8, 4, 2]

n = len(numbers)

for i in range(1, n):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] > key:

        numbers[j+1] = numbers[j]

        j -= 1

    numbers[j+1] = key

print("1. Ascending order:", numbers)


# 2. Insertion Sort (Descending Order)

numbers = [10, 40, 20, 50, 30]

n = len(numbers)

for i in range(1, n):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] < key:

        numbers[j+1] = numbers[j]

        j -= 1

    numbers[j+1] = key

print("2. Descending order:", numbers)


# 3. Insertion Sort with User Input

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(numbers)

for i in range(1, n):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] > key:

        numbers[j+1] = numbers[j]

        j -= 1

    numbers[j+1] = key

print("3. Sorted list:", numbers)


# 4. Display List After Every Pass

numbers = [7, 4, 9, 2, 1]

n = len(numbers)

for i in range(1, n):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] > key:

        numbers[j+1] = numbers[j]

        j -= 1

    numbers[j+1] = key

    print("After pass", i, ":", numbers)


# 5. Count the Number of Shifts

numbers = [5, 4, 3, 2, 1]

n = len(numbers)

shifts = 0

for i in range(1, n):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] > key:

        numbers[j+1] = numbers[j]

        j -= 1

        shifts += 1

    numbers[j+1] = key

print("5. Sorted list:", numbers)
print("Total shifts:", shifts)


# 6. Sort a List of Names Alphabetically

names = ["Shifana", "Anu", "Zara", "Meera"]

n = len(names)

for i in range(1, n):

    key = names[i]

    j = i - 1

    while j >= 0 and names[j].lower() > key.lower():

        names[j+1] = names[j]

        j -= 1

    names[j+1] = key

print("6. Sorted names:", names)


# 7. Sort a Nearly Sorted List

numbers = [10, 20, 15, 30, 25, 40]

n = len(numbers)

for i in range(1, n):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] > key:

        numbers[j+1] = numbers[j]

        j -= 1

    numbers[j+1] = key

print("7. Sorted nearly sorted list:", numbers)
