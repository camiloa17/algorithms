# O(nlogn) time | O(logn) space
# Best: O(nlogn) time | O(logn) space
# Worst: O(n^2) time | O(logn) space because of the recursion overhead
# Type: Quick Sort
# Use this algorithm when you need a simple sorting algorithm that is efficient for large data sets.
# It's an in-place sort, meaning it doesn't require any additional memory to perform the sort.
def quick_sort(nums, low, high):
    """
    Sorts a list of numbers using the QuickSort algorithm.

    Args:
        nums (list): The list of numbers to be sorted.
        low (int): The starting index of the sublist to be sorted.
        high (int): The ending index of the sublist to be sorted.

    Returns:
        list: The sorted list of numbers.
    """
    # The function first checks if the low index is less than the high index.
    if low < high:
        # If it is, the function calls the partition function to partition the list around a pivot element.
        part = partition(nums, low, high)
        # The function then recursively calls itself on the two sublists to the left and right of the pivot element.
        quick_sort(nums, low, part - 1)
        quick_sort(nums, part + 1, high)
    # Finally, the function returns the sorted list.
    return nums


def partition(nums, low, high):
    """
    Partitions the given list of numbers around a pivot element.

    Args:
        nums (list): The list of numbers to be partitioned.
        low (int): The starting index of the partition.
        high (int): The ending index of the partition.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    # The function first selects the pivot element as the last element in the list.
    pivot = nums[high]
    # The function then initializes a counter i to the low index.
    i = low
    # The function then iterates through the list from the low index to the high index - 1.
    for j in range(low, high):
        # If the current element is less than the pivot element, the function swaps the current element with the element at index i and increments i.
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            # The function then increments i.
            i += 1
    # The function then swaps the pivot element with the element at index i.
    nums[i], nums[high] = nums[high], nums[i]

    return i
