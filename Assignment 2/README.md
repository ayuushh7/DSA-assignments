# DSA Assignment 2 - Data Structures Implementation

## Student Details
* **Name:** Ayush
* **Roll Number:** 2501010242
* **Program:** B.Tech CSE (Section C)
* **Subject:** Data Structures (ETCCDS202)

---

## Project Overview
This repository contains my second assignment for the Data Structures course. The goal was to implement the core logic behind basic data structures using Python, focusing on how memory and pointers (references) work in linked structures and arrays.

I have focused on making the code modular and ensuring that edge cases—like deleting from an empty list or popping from an empty stack—are handled properly.

## Files and Modules

| File Name | Implementation Details |
| :--- | :--- |
| **SLL.py** | Implementation of a Singly Linked List with Node class. Key methods: `insert_at_end(val)` to add elements at the end, `delete_by_value(val)` to remove by value, `traverse()` to print the list. Handles edge cases like empty list. Time complexities: Insert O(n), Delete O(n), Traverse O(n). |
| **DLL.py** | Doubly Linked List with nodes having prev and next pointers. Key methods: `insert_after_node(target, x)` to insert after a specific value, `delete_at_position(pos)` to remove at index, `display()` to print the list with arrows. Allows bidirectional traversal. Time complexities: Insert O(n), Delete O(n), Display O(n). |
| **StackSLL.py** | Stack (LIFO) implemented using a Singly Linked List. Key methods: `push(val)` to add to top, `pop()` to remove from top, `peek()` to view top without removing, `traverse()` to print stack. Uses head as top. Time complexities: Push O(1), Pop O(1), Peek O(1). |
| **QueueSLL.py** | Queue (FIFO) implemented using a Singly Linked List with head and tail pointers. Key methods: `enqueue(val)` to add to rear, `dequeue()` to remove from front, `display()` to print queue. Efficient for both operations. Time complexities: Enqueue O(1), Dequeue O(1), Display O(n). |
| **Dynamicarray.py** | Custom resizable array using ctypes for raw arrays. Key methods: `append(x)` to add elements (resizes if needed), `pop()` to remove last, `__getitem__(k)` for indexing, `display()` to show array, size, and capacity. Doubles capacity on resize. Time complexities: Append amortized O(1), Pop O(1), Access O(1). |
| **Parenthesis.py** | Script using a stack (Python list) to check if brackets in an expression are balanced. Supports (), [], {}. Iterates through string, pushes opening brackets, pops and matches closing ones. Returns True if balanced. Time complexity: O(n). |

---

## How to Test the Code
Each script is self-contained. You can run them directly in the terminal to see the test cases I've included at the bottom of each file:

```bash
python SLL.py
python DLL.py
python QueueSLL.py
python StackSLL.py
python Dynamicarray.py
python Parenthesis.py