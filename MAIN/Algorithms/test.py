def SelectionSort(nums):
    """
    The algorithm repeatedly selects the smallest (or largest, depending on the order desired) element from the 
    unsorted sub-list and swaps it with the first element of the unsorted sub-list. This process is repeated until 
    the entire list is sorted.
    1.Start with the entire list considered as an unsorted sub-list.
    2.Find the smallest (or largest) element in the unsorted sub-list.
    3.Swap the found element with the first element of the unsorted sub-list.
    4.Move the boundary between the sorted and unsorted sub-lists one element to the right.
    5.Repeat steps 2-4 until the entire list is sorted

    Time Complexity : O(n^2)
    """
    for i in range(len(nums)-1):
        minPos = i  
        for j in range (i, len(nums)):
            if nums[j] < nums[minPos]:
                nums[j],nums[minPos] = nums[minPos], nums[j]
    return nums



n = [5,3,8,6,7,2]
print(SelectionSort(n))