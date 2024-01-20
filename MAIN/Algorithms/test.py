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

n = [2,6,2,8,1,6,9,3]
print(BubbleSort(n))