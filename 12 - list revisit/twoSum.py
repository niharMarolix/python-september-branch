givenlst = [11,2,15,7,2]
lenOfGivenList = len(givenlst)
target = 9 # [1,3], [2,7]

for currentIndex in range(lenOfGivenList):
    for theNextIndexOfCurrentIndex in range(currentIndex+1, lenOfGivenList):
        if givenlst[currentIndex] + givenlst[theNextIndexOfCurrentIndex] == target:
            print(givenlst[currentIndex], givenlst[theNextIndexOfCurrentIndex])
            print(currentIndex, theNextIndexOfCurrentIndex)
            print("-------------------------")





