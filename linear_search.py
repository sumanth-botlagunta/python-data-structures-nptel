# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def search(arr, n, x):

    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
# input array size
n = int(input("Enter number of elements : "))
arr = []
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
n = len(arr)

x = int(input("Enter the element to be searched : "))

# Function call
result = search(arr, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
