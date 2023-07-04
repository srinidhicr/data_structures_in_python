"""
LOGIC
Repeatedly selects the minimum element in the array and swaps it with the unsorted part of the array
Smallest element moves to the front sorted portion of array
"""

#not stable
arr = []
arr = list(map(int, input().split()))

for i in range(len(arr)):
    mini = arr[i]
    pos = i
    for j in range(i+1, len(arr)):
        #find the minimum in the unsorted array
        if arr[j] < mini: 
            mini = arr[j]
            pos = j
    if arr[i] > mini: #swap
        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp 
print(arr)

"""
TIME COMPLEXITY 
worst - O(N^2) 
worst - O(N^2) 
SPACE COMPLEXITY: O(1)

Selection sort can be made Stable if instead of swapping, 
the minimum element is placed in its position without swapping 
i.e. by placing the number in its position by pushing every element 
one step forward (shift all elements to left by 1). 

"""
