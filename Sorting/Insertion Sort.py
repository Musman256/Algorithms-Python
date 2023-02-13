def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
 
    return arr
 
# Test array
arr = [64, 34, 25, 12, 22, 11, 90]
 
# Function call
result = insertion_sort(arr)
 
print("Sorted array is:", result)

'''

Advantages of the Merge Sort Algorithm:
 - Its is easily coded.
 - It is good for small lists - for this reason as insertion/merge hybrid is used.
 - Doesn't require additional memory.
 - It is very quick to add items to an already ordered list.
 - Its also very quick at checking that a list is already sorted.

Disadvantages of the Merge Sort Algorithm:
 - Cannot cope well with large lists. Worst case scenarion involves doing (n(n-1))/2 comparisons.

'''