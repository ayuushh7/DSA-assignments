
# Unit 1 Assignment: Recursion and Algorithmic Analysis
**Student Name:** Ayush

**Roll number:** 2501010242

**Batch:** B.Tech CSE Core

**Section:** C

**Course:** Data Structures Lab (ETCCDS202)


---

## 1. Factorial and Fibonacci (Naive vs. Memoized)

In this task, I implemented recursive functions to calculate Factorials and Fibonacci numbers. I also explored **Memoization** to optimize recursive calls.

### Key Logic:
- **Factorial:** Uses a simple top-down recursion where $n! = n \times (n-1)!$.
- **Fibonacci (Naive):** A standard recursive approach. It is easy to write but very slow for larger numbers.
- **Fibonacci (Memoized):** I used a dictionary to store previously calculated values. If the function is called for the same number again, it returns the stored result instead of recalculating.

### Complexity Justification:
| Algorithm | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| Factorial | $O(n)$ | $O(n)$ | $n$ recursive calls are added to the stack. |
| Fibonacci (Naive) | $O(2^n)$ | $O(n)$ | Each call branches into two more, creating an exponential tree. |
| Fibonacci (Memoized)| $O(n)$ | $O(n)$ | Each value is computed only once and stored in memory. |



---

## 2. Tower of Hanoi (N=3)

The Tower of Hanoi is a classic puzzle that demonstrates the power of recursive "Divide and Conquer."

### Recursive Trace for N=3:
To move 3 disks from Source (A) to Destination (C) using Auxiliary (B):
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. **Move disk 3 from A to C** (The largest disk moves to the base)
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

### Key Logic:
- **Base Case:** If only one disk, move it directly.
- **Recursive Steps:** Move n-1 disks out of the way, move the nth disk, then move the n-1 disks on top.

### Complexity Justification:
| Algorithm | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| Tower of Hanoi | $O(2^n)$ | $O(n)$ | Each move requires two recursive calls for n-1, leading to exponential time. |



---

## 3. Recursive Binary Search

In this task, I implemented a recursive binary search algorithm to find an element in a sorted array.

### Key Logic:
- **Base Case:** If the low index exceeds high, the element is not found.
- **Recursive Steps:** Calculate the mid index. If the mid element matches the key, return mid. If key is smaller, search left half; if larger, search right half.

### Complexity Justification:
| Algorithm | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| Recursive Binary Search | $O(\log n)$ | $O(\log n)$ | The array is halved each recursive call, leading to logarithmic time and stack space. |



---

## Files in Assignment 1 Folder:
- `task1_recursion.py`: Contains implementations for factorial and Fibonacci with naive and memoized versions.
- `task2_hanoi.py`: Implements the Tower of Hanoi puzzle with a trace for N=3.
- `task3_binary_search.py`: Recursive binary search on a sorted array.
- `README.md`: This documentation file.



**Complexity:** The total moves required is $2^n - 1$. For $N=3$, that is 7 moves. Therefore, the time complexity is **$O(2^n)$**.

---

## 3. Recursive Binary Search

Binary Search is an efficient searching algorithm that works on **sorted** arrays.

### How it works:
The algorithm finds the middle element of the array. If the target is smaller than the middle, it searches the left half; if larger, it searches the right half. This process continues until the element is found or the search space is empty.

### Recurrence Intuition:
Since we divide the problem size by half ($n/2$) at every recursive step, the relation is:
$$T(n) = T(n/2) + \text{constant comparison time}$$

**Analysis:**
- **Time Complexity:** $O(\log n)$ because the search space reduces logarithmically.
- **Space Complexity:** $O(\log n)$ due to the recursive call stack depth.



---

## Conclusion
This assignment helped me understand that while recursion makes code cleaner and easier to read, it can be inefficient without optimization. Techniques like **Memoization** are essential for reducing time complexity from exponential to linear.
