
# DAY 11 - SELECTION SORT


# 1. Basic Selection Sort (Ascending Order)

numbers = [64, 25, 12, 22, 11]

n = len(numbers)

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if numbers[j] < numbers[min_index]:

            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("1. Ascending order:", numbers)


# 2. Selection Sort (Descending Order)

numbers = [10, 40, 20, 50, 30]

n = len(numbers)

for i in range(n):

    max_index = i

    for j in range(i+1, n):

        if numbers[j] > numbers[max_index]:

            max_index = j

    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

print("2. Descending order:", numbers)


# 3. Selection Sort with User Input

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(numbers)

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if numbers[j] < numbers[min_index]:

            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("3. Sorted list:", numbers)


# 4. Display List After Every Pass

numbers = [7, 4, 9, 2, 1]

n = len(numbers)

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if numbers[j] < numbers[min_index]:

            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print("After pass", i+1, ":", numbers)


# 5. Count the Number of Swaps

numbers = [5, 4, 3, 2, 1]

n = len(numbers)

swaps = 0

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if numbers[j] < numbers[min_index]:

            min_index = j

    if min_index != i:

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

        swaps += 1

print("5. Sorted list:", numbers)
print("Total swaps:", swaps)


# 6. Sort a List of Names Alphabetically

names = ["Shifana", "Anu", "Zara", "Meera"]

n = len(names)

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if names[j].lower() < names[min_index].lower():

            min_index = j

    names[i], names[min_index] = names[min_index], names[i]

print("6. Sorted names:", names)


# 7. Find the Smallest and Largest Elements Using Selection Sort

numbers = [45, 12, 78, 23, 9]

n = len(numbers)

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if numbers[j] < numbers[min_index]:

            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("7. Smallest element:", numbers[0])
print("Largest element:", numbers[-1])
