#LINEAR SEARCH 
def LinearSearch(arr, num):
    """
    Linear search, also known as sequential search, is a simple search algorithm that finds the position of a
    target value within a list. It sequentially checks each element of the list until a match is found or the
    entire list has been searched.
    1.Start from the beginning of the list.
    2.Compare the target value with each element in the list.
    3.If a match is found, return the index of the matching element

    Time Complexity : O(n)
    """
    i = 0
    while i < len(arr):
        if arr[i] == num:
            return f"{num} found at index {i}"
        i += 1
    return f"{num} not found"
        

#BINARY SEARCH
def BinarySearch(arr, num):
    """
    Binary search is a divide-and-conquer algorithm that efficiently finds the position of a target value within a
    sorted array. It works by repeatedly dividing the search range in half until the target is found or the search
    range becomes empty.
    1.Set the lower and upper bounds of the search range to the first and last indices of the array.
    2.Repeat until the search range is empty or the target is found:
        *Calculate the middle index of the current search range.
        *If the middle element is equal to the target, return its index.
        *If the target is less than the middle element, update the upper bound to be one less than the middle index.
        *If the target is greater than the middle element, update the lower bound to be one more than the middle index.
    
    Time Complexity : O(logn)
    """
    l = 0  # lower bound
    u = len(arr) - 1  # upper bound
    arr.sort() 

    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == num:
            return f"{num} found at index {mid}"
        else:
            if arr[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
    return f"{num} not found"





