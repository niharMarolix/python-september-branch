def binaryS(arr, target):
    left = 0
    right = len(arr)-1

    while left<= right:
        mid = (left+right)//2

        if arr[mid]== target:
            print(mid)
            break
        elif arr[mid]>target:
            right = right-1
        elif arr[mid]<target:
            left = left+1

arr = [1,2,5,23,9,10,3,-193,-2,72]
b = sorted(arr)
print(b)

target = -2
binaryS(b, target)