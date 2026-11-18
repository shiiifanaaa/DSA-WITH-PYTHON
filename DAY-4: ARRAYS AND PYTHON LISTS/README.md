
# Day 05 - Arrays and Python Lists

## 1. What is an Array?

An array is a data structure used to store multiple elements.

Elements are accessed using their index.

In Python, lists are commonly used for array-like operations.

## 2. Creating a List

numbers = [10, 20, 30, 40, 50]

print(numbers)

Output:
[10, 20, 30, 40, 50]

## 3. Indexing

Indexing is used to access individual elements.

Python uses zero-based indexing.

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])

Output:
10
30
50

## 4. Updating Elements

numbers = [10, 20, 30, 40]

numbers[1] = 25

print(numbers)

Output:
[10, 25, 30, 40]

## 5. Inserting Elements

### append()

Adds an element at the end.

numbers = [10, 20, 30]
numbers.append(40)

Output:
[10, 20, 30, 40]

### insert()

Adds an element at a particular index.

numbers = [10, 20, 30]
numbers.insert(1, 15)

Output:
[10, 15, 20, 30]

## 6. Deleting Elements

### remove()

Removes an element by value.

numbers = [10, 20, 30]
numbers.remove(20)

Output:
[10, 30]

### pop()

Removes an element by index. If no index is given, removes the last element.

numbers = [10, 20, 30]
numbers.pop()

Output:
[10, 20]

## 7. DSA Practice Questions

1. Create a list containing five numbers.
2. Access the first and last elements.
3. Update the second element.
4. Insert a new element.
5. Delete an element.

## 8. Key Takeaways

- Python lists store multiple elements.
- Indexing starts from zero.
- Lists are mutable.
- append(), insert(), remove() and pop() are common operations.
