Ayush 
btech cse core - C
2501010242
## Overview
This report analyzes the observed performance of Insertion Sort, Merge Sort, and Quick Sort on datasets of sizes 1000, 5000, and 10000 with three input types: random, sorted, and reverse-sorted.

---

## Observed Performance vs Theory

### Insertion Sort
Insertion Sort showed strong dependence on input order:
- **Sorted input**: fastest performance, matching best-case time complexity **O(n)**
- **Random input**: slower, approaching **O(n²)**
- **Reverse input**: slowest, confirming worst-case **O(n²)**

This aligns with theory since more shifts are required as disorder increases.

---

### Merge Sort
Merge Sort performance was consistent across all input types:
- Time scaled uniformly with input size
- No noticeable difference between random, sorted, or reverse inputs

This confirms its time complexity of **O(n log n)** in all cases, due to its divide-and-conquer structure.

---

### Quick Sort
Quick Sort behavior depended heavily on pivot selection:
- **Random input**: efficient, close to **O(n log n)**
- **Sorted / Reverse input (last pivot)**: significantly slower

Worst-case behavior:
- Occurs when pivot is always smallest or largest element
- Leads to unbalanced partitions of size `n-1` and `0`
- Time complexity degrades to **O(n²)**
- Recursion depth becomes **O(n)**, which can cause stack overflow

Using a randomized pivot improves performance and avoids this issue.

---

## Stability and In-place Properties

| Algorithm      | Stable | In-place | Notes |
|----------------|--------|----------|-------|
| Insertion Sort | Yes    | Yes      | Maintains relative order of equal elements |
| Merge Sort     | Yes    | No       | Requires O(n) extra space for merging |
| Quick Sort     | No     | Yes      | Swaps can change order of equal elements |

---

## Conclusion
- Insertion Sort is efficient only for small or nearly sorted data
- Merge Sort provides consistent and reliable performance
- Quick Sort is fast on average but sensitive to pivot choice
- Experimental results closely match theoretical expectations