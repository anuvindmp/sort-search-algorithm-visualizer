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
        

