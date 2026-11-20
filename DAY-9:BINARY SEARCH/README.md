
# Day 9 – Binary Search

## Overview

Binary Search is an efficient searching algorithm that finds a target element by repeatedly dividing a sorted list into two halves.

Unlike Linear Search, Binary Search does not check every element one by one.

**Important:** Binary Search requires a sorted list.

## Topics Covered

- Introduction to Binary Search
- Importance of sorted arrays
- Understanding low, high and mid
- Finding the middle element
- Searching the left half
- Searching the right half
- Implementing Binary Search using Python
- Time complexity analysis
- Linear Search vs Binary Search

## How Binary Search Works

Example:

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 60
```

### Steps

1. Set `low = 0` and `high = len(numbers) - 1`.
2. Calculate the middle index using `(low + high) // 2`.
3. Compare the middle element with the target.
4. If equal, the target is found.
5. If the target is smaller, search the left half.
6. If the target is greater, search the right half.
7. Repeat until the target is found or the search range becomes empty.

## Important Variables

| Variable | Meaning |
|---|---|
| `low` | Starting index of the search range |
| `high` | Ending index of the search range |
| `mid` | Middle index of the search range |
| `target` | Element to be searched |
| `position` | Stores the index when the target is found |

### Middle Index Formula

```python
mid = (low + high) // 2
```

## Python Implementation

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

target = 60

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
    print("Element found at index:", position)

else:
    print("Element not found")
```

## Time Complexity

| Case | Complexity |
|---|---|
| Best case | O(1) |
| Average case | O(log n) |
| Worst case | O(log n) |

## Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|---|---|---|
| Approach | Checks one by one | Divides into halves |
| Sorted list required | No | Yes |
| Best case | O(1) | O(1) |
| Worst case | O(n) | O(log n) |

## Key Learning Points

- Binary Search works only on sorted data.
- It repeatedly divides the search range into two halves.
- `low`, `high` and `mid` control the search.
- `while low <= high` continues searching while elements remain.
- `break` stops the loop when the target is found.
- Binary Search is efficient for large sorted datasets.

## Practice Programs

The `practice.py` file includes:

1. Search for an element in a sorted list.
2. Search for an absent element.
3. Compare Linear Search and Binary Search.
4. Count the number of comparisons.
5. Additional independent practice.

## Learning Objectives

- Understand the Binary Search algorithm.
- Implement Binary Search using Python.
- Understand how to update low and high.
- Calculate the middle index.
- Analyse time complexity.
- Compare Linear Search and Binary Search.

## Progress Tracker

- [ ] Understand Binary Search.
- [ ] Understand low, high and mid.
- [ ] Understand the searching process.
- [ ] Implement Binary Search independently.
- [ ] Practise different target values.
- [ ] Compare Linear Search and Binary Search.

