"""
Binary Search Algorithm

A Python implementation of the Binary Search algorithm for efficiently
finding a target value within a sorted list.

Binary Search works by repeatedly dividing the search interval in half,
eliminating the half in which the target value cannot exist until the
value is found or the search interval becomes empty.

This implementation also records the sequence of values inspected during
the search, providing insight into how the algorithm reaches its result.

Features:
- Efficient binary search on sorted lists
- Tracks the search path
- Returns the index of the target when found
- Returns an informative message if the target is not found

Time Complexity:
    Best Case:    O(1)
    Average Case: O(log n)
    Worst Case:   O(log n)

Space Complexity:
    O(log n) (due to storing the search path)

Created as part of the freeCodeCamp Python Algorithms curriculum.
"""


# =========================================================
# BINARY SEARCH IMPLEMENTATION
# =========================================================


def binary_search(search_list, value):
    """
    Perform a binary search on a sorted list.

    Args:
        search_list (list):
            A sorted list of comparable elements.

        value:
            The target value to search for.

    Returns:
        tuple:
            A tuple containing:

            - A list of the values inspected during the search.
            - A message indicating whether the value was found.
    """

    # Record every value inspected during the search.
    path_to_target = []

    # Initialize the search boundaries.
    low = 0
    high = len(search_list) - 1

    # Continue searching while the search interval is valid.
    while low <= high:
        # Compute the middle index.
        mid = (low + high) // 2

        # Retrieve the value at the middle position.
        value_at_middle = search_list[mid]

        # Record the inspected value.
        path_to_target.append(value_at_middle)

        # Target found.
        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"

        # Search the right half.
        elif value > value_at_middle:
            low = mid + 1

        # Search the left half.
        else:
            high = mid - 1

    # Target value was not found.
    return [], "Value not found"


# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

# Search for a value that exists.
print(binary_search([1, 2, 3, 4, 5], 3))

# Search for another existing value.
print(binary_search([1, 2, 3, 4, 5, 9], 4))

# Search for a value that does not exist.
print(binary_search([1, 3, 5, 9, 14, 22], 10))
