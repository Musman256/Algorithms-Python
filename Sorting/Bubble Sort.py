def bubble_sort(arr):
    n = len(arr)
 
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]: # Check if the two vaules are in the right place,
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # and if not then swap them.
    return arr
 
# Test array
arr = [64, 34, 25, 12, 22, 11, 90]
 
# Function call
result = bubble_sort(arr)
 
print("Sorted array is:", result)

'''

Advantages of the Bubble Sort Algorithm:
 - Its a simple algorithm that can be easily implemented on a computer.
 - Its a efficient way to check if the list is in order (n-1 comparisons).
 - Doesn't use much memory.

Disadvantages of the Bubble Sort Algorithm:
 - Enefficient: Its an inefficient way to sort a list, for a list with n items, the worst case
   scenario would involve in doing (n(n-1))/2 comparisons.
 - Large lists: Does not cope well with large lists.

'''