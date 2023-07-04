"""
LOGIC
Divide the array into half and check whether target is in the portion - 0 to mid-1 or in the other portion - mid+1 to h
If it is equal to the target return the index
Perform this repeatedly
If an element is not found -1 is returned
"""

def binarySearch(nums, target):
    l, h = 0, len(nums)-1
    while(l<=h):
        mid = (l + h)//2

        if nums[mid] == target:
            return mid
                
        elif nums[mid] > target:
            h = mid-1
        else:
            l = mid+1

    return -1
    
n = int(input("Enter no. of elements in array: "))
nums = [ ]
for _ in range(n):
        ele = int(input())
        nums.append(ele)
target = int(input("Enter the element to search for - "))
index = binarySearch(nums, target)
print(index)

"""
TIME COMPLEXITY - 
worst case - O(logN)
best case - O(1) - elements are already sorted
avg case - O(logN)
SPACE COMPLEXITY - O(1)


--SUITABLE FOR LARGE DATASETS


"""
