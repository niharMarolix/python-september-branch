# bubble sort

def bs(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
a = [1,4,3,6,8,20,24,-1]
(bs(a))
print(a)