def insertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and temp <  a[j]:
            a[j+1]=a[j]
            j = j-1
        a[j+1] = temp
    return a

a = [7,4,5,2]
print(insertionSort(a))
