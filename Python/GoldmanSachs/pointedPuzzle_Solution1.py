# arr = [3, 4, 2]
arr = [1, 2, 1, 3, 2, 3]
pointNum = 0
while True:
    if len(arr) == 0:
        break
    maxNum = max(arr)
    less = maxNum - 1
    more = maxNum + 1

    pointLess = 0
    pointMore = 0

    if less in arr:
        while True:
            if less in arr:
                arr.remove(less)
            if less not in arr:
                break
    if more in arr:
        while True:
            if more in arr:
                arr.remove(more)
            if more not in arr:
                break

    countNum = arr.count(maxNum)
    pointNum += countNum * maxNum

    while True:
        if maxNum in arr:
            arr.remove(maxNum)
        if maxNum not in arr:
            break

print(pointNum)
