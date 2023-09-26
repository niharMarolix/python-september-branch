list = [4,5,6,7,8,10,11]
target = 18

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if target == list[i] + list[j]:
            print([i,j])
