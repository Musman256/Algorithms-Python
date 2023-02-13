# Create a function where 'arr' is the sorted array and 'x' is the item you are lokking for.
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # Check if x is greater, less or equal than the mid element.
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1
 
# Test array.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
 
# Function call.
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

'''

Advantages of the Binary Search Algorithm:
 - Efficiency: Binary search is an efficient algorithm for searching
   a sorted list. It is faster than a linear search.
 - Precision: Binary search is a precise algorithm that
   always finds the correct location of the target element in the list
   or determines that the element is not in the list.

Disadvantages of the Binary Search Algorithm:
 - Sorted Lists Only: The algorithm can only be used on sorted lists, so
   the list must be sorted before the search can begin. This can add an
   additional step and complexity to the search process.
 - Complexity: Although the time complexity of the binary search algorithm is
   faster than a linear search, it can still be more complex to implement, especially
   for those who are not familiar with the algorithm.
 - Not Suitable for Small Lists: For small lists, the efficiency gains of binary search
   may not be significant enough to justify the additional complexity of the algorithm.
   In these cases, a simple linear search may be a better choice.

'''