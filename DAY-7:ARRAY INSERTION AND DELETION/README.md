
# Day 7 – Array Insertion and Deletion

## Topics Covered
- What is an array?
- What is insertion?
- Insertion at the beginning.
- Insertion at the end.
- Insertion at a particular position.
- What is deletion?
- Deleting elements by value and index.
- Finding the position of an element.

## 1. Array

An array is an ordered collection of elements.

Python uses lists for practising array operations.

Example:
```python
numbers = [10, 20, 30, 40, 50]
```

Python indexing starts from 0.

## 2. Insertion

Insertion means adding a new element to a list.

### Insertion methods

- `insert(0, value)` – Insert at beginning.
- `append(value)` – Insert at end.
- `insert(index, value)` – Insert at a particular position.

## 3. Deletion

Deletion means removing an element from a list.

### Deletion methods

- `remove(value)` – Delete by value.
- `pop(index)` – Delete by index.
- `del list[index]` – Delete using index.
- `pop()` – Delete the last element.

## 4. Finding Position

The `index()` method returns the index of an element.

Example:
```python
numbers = [10, 20, 30, 40]

print(numbers.index(30))
```

Output: 2

## 5. Time Complexity

| Operation | Complexity |
|---|---|
| Access by index | O(1) |
| Insertion at beginning | O(n) |
| Insertion at end | O(1) amortized |
| Deletion at beginning | O(n) |
| Searching | O(n) |

## Key Points

- Python list indexing starts at 0.
- Lists are mutable.
- append() adds an element at the end.
- insert() adds an element at a specified index.
- remove() deletes by value.
- pop() deletes by index.
- index() finds the position of an element.

## Practice Completed

- [ ] Insert an element into a list.
- [ ] Delete an element from a list.
- [ ] Find the position of an element.
- [ ] Complete additional practice problems.
