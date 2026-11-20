# Day 8 – Linear Search

## 📌 Topic
**Linear Search in Python**

## 🎯 Learning Objectives
- Understand the concept of Linear Search.
- Search for a specific element in a list.
- Find the index of an element.
- Handle cases where the target element is not present.
- Count the occurrences of an element.
- Find all indexes where an element appears.
- Understand the use of `break`, `found`, and `position`.

## 📖 What is Linear Search?

Linear Search is a simple searching algorithm that checks each element in a list one by one until the target element is found or the list ends.

It starts from the first element and moves sequentially through the list.

### Example

```python
numbers = [10, 20, 30, 40, 50]
target = 30
```

The searching process:

1. Check whether 10 == 30 → False
2. Check whether 20 == 30 → False
3. Check whether 30 == 30 → True
4. Element found at index 2.

## 💻 Programs Practiced

| No. | Program | Concept Used |
|---|---|---|
| 1 | Search for an element in a list | Linear Search |
| 2 | Search when the target is absent | Boolean flag |
| 3 | Count element occurrences | Counter variable |
| 4 | Find all indexes of a target | List and append() |
| 5 | Find first index without index() | Position variable and break |
| 6 | User-input-based Linear Search | input() and conditional statements |

## 🔑 Important Python Concepts

- `for` loop – Iterates through list elements or indexes.
- `range()` – Generates a sequence of indexes.
- `len()` – Returns the number of elements in a list.
- `if` condition – Checks whether the target matches an element.
- `break` – Stops the loop when the target is found.
- `found` – Boolean variable used to track whether an element exists.
- `count += 1` – Increases the occurrence counter.
- `append()` – Adds an index to a list.
- `position = -1` – Indicates that the target has not been found.

## ⏱️ Time Complexity

- Best Case: O(1) – Target is found at the first position.
- Worst Case: O(n) – Target is at the last position or is absent.
- Average Case: O(n) – Elements may need to be checked sequentially.

**Space Complexity:** O(1) for basic Linear Search without storing additional indexes.


## 💡 Key Takeaway

Linear Search is one of the simplest searching algorithms. It is useful for understanding how searching works and forms the foundation for learning more advanced searching algorithms such as Binary Search.

---
