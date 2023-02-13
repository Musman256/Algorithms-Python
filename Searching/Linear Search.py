# Create a function where 'arr' is the sorted array and 'x' is the item you are lokking for.
def linear_search(arr, x):
    for i in range(len(arr)):   # Cycle through the array
        if arr[i] == x:         # Check if the selected item is what your're looking for, if not then carry on.
            return i
    return -1
 
# Test array
arr = [8, 7, 5, 6, 9, 1, 3, 2, 4]
x = 5
 
# Function call
result = linear_search(arr, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

'''

Advantages of the Linear Search Algorithm:
 - Simplicity: Linear search is a simple algorithm that can be easily understood
   and implemented. It does not require any special knowledge or preparation of the list before searching.
 - Flexibility: Linear search can be used on any type of list, regardless of whether the list is sorted or not.
 - No Sorting Required: Unlike binary search, which requires that the list be sorted
   before the search can begin, linear search can be used on unsorted lists.

Disadvantages of the Linear Search Algorithm:
 - Efficiency: It is not efficient for larger list instead, algorithms such as binary search are faster.
 - Not Suitable for Large Lists: For large lists, the linear search algorithm can take a long
   time to complete. In these cases, it is often more efficient to use a different search algorithm,
   such as binary search.
 - No Guarantee of Preciseness: Unlike binary search, linear search does not guarantee that the
   target element will be found or that it will be found at a specific index in the list.

'''