# O(n^2) time | O(1) space
# Best: O(n) time | O(1) space
# worst: O(n^2) time | O(1) space
# Type: Bubble Sort
# Description: This is a simple implementation of the bubble sort algorithm.
# It's one of the slowest sorting algorithms, but can be useful for a quick.
# script or when the amount of data to be sorted is guaranteed to be small.
def bubble_sort(nums):
    """
    Sorts a list of numbers using the bubble sort algorithm.

    Args:
        nums (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.
    """
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums
