def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
 
        merge_sort(L)
        merge_sort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
    return arr
 
# Test array
arr = [64, 34, 25, 12, 22, 11, 90]
 
# Function call
result = merge_sort(arr)
 
print("Sorted array is:", result)

'''

Advantages of the Merge Sort Algorithm:
 - Efficiency: More efficient and quicker than bubble sort algorithm and inserton sort algorithm.
 - Consistency: It has a very consistant running time regardless of how ordered
   the items in the original list are.

Disadvantages of the Merge Sort Algorithm:
 - Speed: It is slower than other algorithms for small lists.
 - Even if the list is already sorted, it still goes through the whole process of merging and splitting.
 - It uses mre memory to create the seperate lists.

'''