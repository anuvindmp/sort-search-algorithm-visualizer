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

n = [5, 3, 8, 6, 7, 2]
MergeSort(n)
print(n)
