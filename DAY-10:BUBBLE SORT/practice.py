
# DAY 10 - BUBBLE SORT

# 1. Basic Bubble Sort (Ascending Order)

numbers = [5, 3, 8, 2, 1]

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):

        if numbers[j] > numbers[j+1]:

            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("1. Ascending order:", numbers)


# 2. Bubble Sort (Descending Order)

numbers = [10, 40, 20, 50, 30]

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):

        if numbers[j] < numbers[j+1]:

            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("2. Descending order:", numbers)


# 3. Bubble Sort with User Input

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):

        if numbers[j] > numbers[j+1]:

            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("3. Sorted list:", numbers)


# 4. Display the List After Every Pass

numbers = [7, 4, 9, 2, 1]

n = len(numbers)

for i in range(n):

    for j in range(0, n-i-1):

        if numbers[j] > numbers[j+1]:

            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print("After pass", i+1, ":", numbers)


# 5. Optimized Bubble Sort

numbers = [1, 2, 3, 5, 4]

n = len(numbers)

for i in range(n):

    swapped = False

    for j in range(0, n-i-1):

        if numbers[j] > numbers[j+1]:

            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

            swapped = True

    if not swapped:
        break

print("5. Optimized sorted list:", numbers)


# 6. Count the Number of Swaps

numbers = [5, 4, 3, 2, 1]

n = len(numbers)

swaps = 0

for i in range(n):

    for j in range(0, n-i-1):

        if numbers[j] > numbers[j+1]:

            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

            swaps += 1

print("6. Sorted list:", numbers)
print("Total swaps:", swaps)


# 7. Sort a List of Strings

names = ["Shifana", "Anu", "Zara", "Meera"]

n = len(names)

for i in range(n):

    for j in range(0, n-i-1):

        if names[j].lower() > names[j+1].lower():

            names[j], names[j+1] = names[j+1], names[j]

print("7. Sorted names:", names)
