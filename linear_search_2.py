def linear_search(arr, key):
    left = 0
    length = len(arr)
    right = length - 1

    for left in range(0, right, 1):
        if arr[left] == key:
            return left
        elif arr[right] == key:
            return right
        else:
            return -1
        
        left += 1
        right -= 1

n = int(input("Enter number of elements : "))

arr = []
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

k = int(input("Enter the element to be searched : "))

result = linear_search(arr, k)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

