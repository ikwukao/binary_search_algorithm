# Binary Search Algorithm in Python

A Python implementation of the **Binary Search** algorithm using Object-Oriented programming principles and efficient searching techniques. This project demonstrates how binary search quickly locates a target value in a **sorted list** by repeatedly dividing the search interval in half.

In addition to locating a value, this implementation records the sequence of values inspected during the search, making it an excellent educational tool for understanding how binary search works internally.

---

## Overview

Binary Search is one of the most efficient searching algorithms for sorted collections. Instead of checking every element sequentially, it repeatedly compares the target value with the middle element and eliminates half of the remaining search space after each comparison.

This implementation returns:

- The path of values examined during the search.
- The index of the target value if found.
- An informative message if the target does not exist.

---

## Features

- Efficient Binary Search implementation
- Works with sorted lists
- Tracks the search path
- Returns the target index when found
- Gracefully handles values that are not present
- Clean and beginner-friendly implementation
- Well-documented and easy to understand

---

## Project Structure

```text
binary-search/
│
├── main.py
└── README.md
```

---

## Algorithm Workflow

1. Start with the entire sorted list.
2. Find the middle element.
3. Compare the target with the middle value.
4. If they match, return the result.
5. If the target is larger, search the right half.
6. If the target is smaller, search the left half.
7. Repeat until the value is found or the search space is empty.

---

## Example Usage

```python
print(binary_search([1, 2, 3, 4, 5], 3))

print(binary_search([1, 2, 3, 4, 5, 9], 4))

print(binary_search([1, 3, 5, 9, 14, 22], 10))
```

---

## Example Output

```text
([3], 'Value found at index 2')

([3, 5, 4], 'Value found at index 3')

([], 'Value not found')
```

> **Note:** If you update the function to return the search path even when the value is not found, the final output will include the values inspected before the search terminated.

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

---

## Space Complexity

| Complexity |
|------------|
| O(log n) |

The additional space is used to store the sequence of inspected values during the search.

---

## Concepts Demonstrated

This project demonstrates several important computer science concepts:

- Binary Search
- Divide and Conquer
- Searching Algorithms
- Algorithm Analysis
- Time Complexity
- Space Complexity
- Python Functions
- Lists
- Control Flow
- Problem Solving

---

## Requirements

- Python 3.8 or later

No external libraries are required.

---

## Running the Program

Clone the repository:

```bash
git clone https://github.com/ikwukao/binary_search_algorithm.git
```

Navigate into the project directory:

```bash
cd binary_search_algorithm
```

Run the program:

```bash
python3 main.py
```

---

## Learning Objectives

By completing this project, you will understand:

- How Binary Search works
- Why Binary Search requires a sorted list
- How Divide and Conquer algorithms reduce search time
- The difference between Binary Search and Linear Search
- How algorithm efficiency is measured using Big O notation

---

## Possible Improvements

Future enhancements could include:

- Recursive Binary Search implementation
- Generic support for different data types
- Automatic sorting before searching
- Input validation
- Unit tests
- Performance benchmarking
- Interactive command-line interface
- Visualization of each search step

---

## Author

Created as part of my Python Algorithms learning journey through the **freeCodeCamp Scientific Computing with Python** curriculum.

---

## License

This project is licensed for educational and personal learning purposes.
