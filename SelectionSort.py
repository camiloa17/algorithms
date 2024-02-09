# O(n^2) time | O(1) space
# Best: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
# Type: Selection Sort
# Use this algorithm when you need a simple sorting algorithm that is efficient for small data sets.
def selection_sort(nums):
    """
    Sorts a list of numbers in ascending order using the selection sort algorithm.

    Parameters:
    nums (list): The list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    n = len(nums)
    # Iterate through the list
    for i in range(n - 1):
        # Assume the current index has the minimum value
        min_index = i
        for j in range(i + 1, n):
            # If a smaller value is found, update min_index
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the minimum value with the current index
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
