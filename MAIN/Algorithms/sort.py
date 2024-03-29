#BUBBLE SORT
def BubbleSort(arr):
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
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr


#INSERTION SORT
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


#SELECTION SORT
def SelectionSort(arr):
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
    for i in range(len(arr)-1):
        minPos = i  
        for j in range (i, len(arr)):
            if arr[j] < arr[minPos]:
                arr[j],arr[minPos] = arr[minPos], arr[j]
    return arr


#MERGE SORT
def MergeSort(arr):
    """Merge Sort is a divide-and-conquer sorting algorithm. It works by dividing the input array into two halves,
      recursively sorting each half, and then merging the sorted halves to produce a single sorted array. This 
      process continues until the entire array is sorted.
      1.Divide: Divide the unsorted list into two halves.
      2.Conquer: Recursively sort each half.
      3.Merge: Merge the sorted halves to produce a single sorted array.

      Time Complexity : O(nlogn)
      """
    if len(arr) > 1:
        leftArray = arr[:len(arr) // 2]
        rightArray = arr[len(arr) // 2:]

        # recursion:
        MergeSort(leftArray)
        MergeSort(rightArray)
        # merge step:
        i = j = k = 0  # indices for leftArray, rightArray, and merged array

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1
        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1



#HEAP SORT
def Swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def SiftDown(arr, i, upper):
    while True:
        l, r = i*2+1, i*2+2
        if max(l,r) < upper:
            if arr[i] >= max(arr[l], arr[r]): break
            elif arr[l] > arr[r]:
                Swap(arr, i, l)
                i = l
            else:
                Swap(arr, i, r)
                i = r
        
        elif l < upper:
            if arr[l] > arr[i]:
                Swap(arr, i, l)
                i = l
            else: break
        
        elif r < upper:
            if arr[l] > arr[i]:
                Swap(arr, i, r)
                i = r
            else: break
        else: break
            
def HeapSort(arr):
    '''
    Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure to build a max-heap or min-heap. Here's a basic overview of how heapsort works, along with a simple implementation in Python:

    Heapsort Overview:
    Build Heap:

    The first step of heapsort involves building a binary heap from the input array. This can be done in linear time.
    For a max-heap, the heap property is that the value of each node is greater than or equal to the values of its children.
    For a min-heap, the heap property is that the value of each node is less than or equal to the values of its children.
    Heapify:

    After building the heap, the largest (for max-heap) or smallest (for min-heap) element is at the root.
    Swap the root with the last element of the array, decrease the size of the heap, and heapify the root.
    Repeat this process until the heap is empty.

    Time complexity : O(nlogn)
    '''
    for i in range((len(arr)-2//2), -1, -1):
        SiftDown(arr, i, len(arr))
    
    for end in range(len(arr)-1, 0, -1):
        Swap(arr, 0, end)
        SiftDown(arr, 0, end)
    
    return arr

#QUICK SORT
def QuickSort(l, h, arr):
    """Quick sort uses divide and conquer method to solve. It works by comparing an element with other elements and swap with itself
        if the new element is found to be smaller.
        
        Time complexity is O(n^2) or O(n(log(n)))"""
    if l < h:
        pivot_index = partition(l, h, arr)
        QuickSort(l, pivot_index, arr)
        QuickSort(pivot_index + 1, h, arr)

def partition(l, h, arr):
    pivot = arr[l]
    i, j = l, h

    while True:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]


#RADIX SORT(LSD)
def RadixSort(arr):
    """Radix sort is a non-comparison based algorithm, it uses stable sorting technique to arrange the numbers
    By taking each unit digit the sorting is done first. Then 10's digit is taken and sorted and at last the hundreds digit is used to sort
    
    Time Complexity is O(d*(n+k))"""
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count[i] to store the position of the digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to the original array
    for i in range(n):
        arr[i] = output[i]
