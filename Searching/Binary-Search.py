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
