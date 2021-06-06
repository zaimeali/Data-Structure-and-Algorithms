arr = [1, 2, 1, 3, 2, 3]
sortedArr = sorted(arr)

pointNum = 0
while True:
    if len(sortedArr) == 0:
        break

    maxNum = max(sortedArr)
    indexMax = sortedArr.index(maxNum)
    countMax = sortedArr.count(maxNum)

    pointNum += countMax * maxNum

    sortedArr = sortedArr[:indexMax]

    less = maxNum - 1
    if less in sortedArr:
        indexLess = sortedArr.index(less)
        sortedArr = sortedArr[:indexLess]

print(pointNum)
