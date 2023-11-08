def interSearch(arr, target):
    left = 0
    right = len(arr)-1

    while left<=right and arr[left]<=target <=arr[right]:
        if left==right:
            if arr[left]== target:
                return left
            else:
                return "not found"
            
        postion = left +((target-arr[left])*(right-left)) // (arr[right]-arr[left])

        if arr[postion]==target:
            return postion
        elif arr[postion] < target:
            left = postion+1
        else:
            right = postion-1

    return "not found"

arr = [90, 23, 5, 109, 12, 22, 67, 34]
b = sorted(arr)
print(b)
target = 22

res = interSearch(b,target)
print(res)