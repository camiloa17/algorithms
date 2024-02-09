# O(n log n) time | O(n) space
# Best: O(n log n) time | O(n) space
# Worst: O(n log n) time | O(n) space because of the recursion overhead
# Type: Merge Sort
# Description: This is a simple implementation of the merge sort algorithm.
# use it when memory is not issue and you need a stable sorting algorithm.
def merge_sort(nums):
    """
    Sorts a list of numbers using the merge sort algorithm.

    Args:
        nums (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.
    """
    #The function first checks if the length of the list is less than 2.
    #If it is, the function simply returns the list because a list with
    # one or zero elements is already sorted.
    if len(nums) < 2:
        return nums
    # if the list has more than one element, the function proceeds to divide the list into two halves
    # and recursively calls itself on each half.
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2 :])
    # The function then merges the two sorted halves into a single sorted list and returns the result.
    return merge(first, second)


def merge(first, second):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        first (list): The first sorted list.
        second (list): The second sorted list.

    Returns:
        list: A new list containing all elements from both input lists, sorted in ascending order.
    """
    # will contain the sorted and merged elements from both input lists.
    final = []
    # initializes two counters i and j to 0.
    # These counters will be used to keep track 
    # of the current index in the first and second lists, respectively
    i = 0
    j = 0
    # This loop is responsible for merging the elements from first and second
    # into final in sorted order.
    # The loop runs as long as there are elements in both first and second.
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    # The loop then appends any remaining elements from first and second to final.
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    # Finally, the function returns final.
    return final
