def BubbleSort(nums):
    """
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
    compares adjacent elements, and swaps them if they are in the wrong order.
    1.Start from the beginning of the list.
    2.Compare each pair of adjacent elements.
    3.If the elements are in the wrong order, swap them.
    4.Continue this process until the end of the list is reached.
    5.Repeat steps 1-4 until no swaps are needed, indicating the list is sorted

    Time complexity : O(n^2)
    """
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]
    return nums

def InsertionSort(arr):
    '''
    This algorithm basically divides the array into 2 parts - sorted and unsorted. Initially, the first element is in the sorted part and then it keeps adding the other elements to the sorted part. Before adding, it checks if the left neighbour of the element is smaller than the element, otherwise it swaps. It keeps swapping till the element's left neighbour is smaller than the element and adds the element to the sorted part. It does this for all elements and the array is ultimately sorted.

    Time complexity : O(n^2)
    '''
    for i in range(1,len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    
    return arr