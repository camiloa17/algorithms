# O(logn) time | O(1) space
# Best: O(1) time | O(1) space
# Worst: O(logn) time | O(1) space
# Type: Binary Search
# Use this algorithm when you need to quickly find an element in a sorted list.
# This is a simple implementation of the binary search algorithm.
def binary_search(data, followers):
    """
    Perform binary search on a list of dictionaries based on the 'followers' key.

    Args:
        data (list[dict]): The list of dictionaries to search.
        followers (int): The number of followers to search for.

    Returns:
        str or None: The name of the dictionary with matching 'followers' value, or None if not found.
    """

    """The function begins by initializing two pointers, left and right, to the start and end of the data list, 
    respectively. These pointers define the current search range within the list."""
    left = 0
    right = len(data) - 1
    # The function then enters a loop that continues as long as the left pointer is less than or equal to the right pointer.
    while left <= right:
        # The function calculates the middle index of the current search range and compares the 'followers' value at that index with the target value.
        middle = (left + right) // 2
        # If the middle value is less than the target value, the function updates the left pointer to the middle index + 1.
        if data[middle]["followers"] < followers:
            left = middle + 1
        # If the middle value is greater than the target value, the function updates the right pointer to the middle index - 1.
        elif data[middle]["followers"] > followers:
            right = middle - 1
        # If the middle value is equal to the target value, the function returns the name of the dictionary at the middle index.
        else:
            return data[middle]["name"]

    return None
