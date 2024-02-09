# O(n^2) time | O(1) space
# Best: O(n) time | O(1) space
# worst: O(n^2) time | O(1) space
# Description: This file contains the implementation of the insertion sort algorithm.
# Type: Insertion Sort
# Use this algorithm when you need a simple sorting algorithm that is efficient for small data sets.
# There is no recursion overhead
# Tiny memory footprint
# It's a stable sort as described above

def insertion_sort(nums):
    """
    Sorts a list of numbers in ascending order using the insertion sort algorithm.

    Parameters:
    nums (list): The list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
            j -= 1
    return nums
