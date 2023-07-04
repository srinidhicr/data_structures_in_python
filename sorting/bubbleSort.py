"""
LOGIC
In each pass compare adjacent elements and swap if they are descending
At the end of a pass, the highest element is moved to the end
"""

arr = [5, 2, 7, 6, 3, 8, 1]

print("Enter array elements separated by space - ")
arr = []
arr = list(map(int, input().split()))


# traverse through all array elements for each PASS
for i in range(len(arr)):
    # comparing elements in one pass
    # len(arr) - i - 1 elements are sorted at the end
    swap = False
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]: #swap
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            swap = True
    if swap == False:
        break
print(arr)

"""
TIME COMPLEXITY - 
worst case - O(N^2)
best case - O(N) - elements are already sorted
avg case - O(N^2)
SPACE COMPLEXITY - O(1)

BOUNDARY CONDS:
Bubble sort takes minimum time (Order of n) when elements are already sorted. 
Hence best to check if the array is already sorted or not before, to avoid O(N^2) time complexity.

--STABLE ALG 
(A sorting algorithm is said to be stable if two objects with equal or same keys appear
in the same order in sorted output as they appear in the input array to be sorted.)
--SLOW FOR LARGE DATASETS


"""

