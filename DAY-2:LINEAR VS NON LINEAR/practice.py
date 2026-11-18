
# DAY 2 - LINEAR VS NONLINEAR DATA STRUCTURES

# --------------------------------------------------
# PROGRAM 1: Classify data structures
# Explanation:
# Linear data structures arrange elements sequentially.
# Nonlinear structures organize elements hierarchically
# or through interconnected relationships.

linear = ["Array", "Linked List", "Stack", "Queue"]
nonlinear = ["Tree", "Graph"]

print("Linear Data Structures:")

for item in linear:
    print(item)

print("\nNonlinear Data Structures:")

for item in nonlinear:
    print(item)


# --------------------------------------------------
# PROGRAM 2: Stack implementation
# Explanation:
# Stack follows LIFO (Last In, First Out).
# append() inserts an element at the top.
# pop() removes the last inserted element.

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

stack.pop()

print("After Pop:", stack)

# Output:
# Stack: [10, 20, 30]
# After Pop: [10, 20]


# --------------------------------------------------
# PROGRAM 3: Queue implementation
# Explanation:
# Queue follows FIFO (First In, First Out).
# append() adds an element at the rear.
# pop(0) removes the first element.

queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

queue.pop(0)

print("After Dequeue:", queue)

# Output:
# Queue: [10, 20, 30]
# After Dequeue: [20, 30]


# --------------------------------------------------
# PROGRAM 4: Stack Peek operation
# Explanation:
# Peek means viewing the top element without removing it.
# The last element is the top of our stack.

stack = [10, 20, 30]

print("Top Element:", stack[-1])
print("Stack:", stack)

# Output:
# Top Element: 30
# Stack: [10, 20, 30]


# --------------------------------------------------
# PROGRAM 5: Queue Front operation
# Explanation:
# Front gives the first element in the queue.
# It does not remove that element.

queue = [10, 20, 30]

print("Front Element:", queue[0])

# Output: Front Element: 10


# --------------------------------------------------
# PROGRAM 6: Reverse a list using a stack
# Explanation:
# A stack follows LIFO.
# Removing elements one by one reverses their order.

stack = [10, 20, 30, 40]

while len(stack) > 0:
    print(stack.pop())

# Output:
# 40
# 30
# 20
# 10
