
# Day 06 - Array Traversal

## 1. What is Array Traversal?

Array traversal means visiting each element of an array or list one by one.

It is commonly used for searching, calculating sums and finding maximum or minimum values.

## 2. Traversing an Array

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

Output:
10
20
30
40
50

Time Complexity: O(n)

## 3. Finding the Sum

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total = total + num

print(total)

Output:
100

Time Complexity: O(n)

## 4. Finding the Maximum Element

numbers = [10, 45, 20, 60, 30]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)

Output:
60

Time Complexity: O(n)

## 5. Finding the Minimum Element

numbers = [10, 45, 20, 60, 30]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print(minimum)

Output:
10

Time Complexity: O(n)

## 6. DSA Practice Questions

1. Traverse and print all elements of a list.
2. Find the sum of all elements.
3. Find the largest element.
4. Find the smallest element.

## 7. Key Takeaways

- Traversal means visiting every element.
- A for loop can be used for list traversal.
- Sum, maximum and minimum can be found using traversal.
- Basic traversal takes O(n) time.
