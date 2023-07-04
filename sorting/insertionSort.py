"""
LOGIC
take the array as 2 parts sorted sublist and unsorted sublist
two loops - outer: from 1 to len(arr) - 1 (INCREMENTAL LOOP): UNSORTED
            inner: (DECREMENTAL LOOP till 0)
"""
arr = []
arr = list(map(int, input().split()))

#OUTER LOOP - UNSORTED LIST TRAVERAL
for i in range(1, len(arr)):
    temp = arr[i]
    j = i-1
    #INNER LOOP - SORTED LIST (assumption) traversed decrementally
    while(j>=0 and temp<arr[j]):
        arr[j+1] = arr[j]
        j -= 1
    # IF THE WHILE LOOP IS NOT EXECUTED THE BELOW STATEMENT WILL NOT PRODUCE ANY CHANGES
    arr[j+1] = temp

print(arr)

"""
TIME COMPLEXITY
best - O(N)
worst - O(N^2)
avg - O(N^2)
SPACE COMPLEXITY - O(1)

BOUNDARY CASES - 
takes the maximum time to sort if elements are sorted in reverse order
takes minimum time (Order of n) when elements are already sorted. 

-- STABLE ALG
--  used when number of elements is small
"""