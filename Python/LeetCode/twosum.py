def twosum(arr, target):
    sizeArr = len(arr)
    for i in range(sizeArr):
        result = target - arr[i]
        if result in arr:
            resultIndex = arr.index(result)
            if i != resultIndex:
                return sorted([i, resultIndex])
    return []


def twosum_sol1(arr, target):
    sizeArr = len(arr)
    for i in range(sizeArr):
        first = arr[i]
        nextIndex = i + 1
        for j in range(nextIndex, sizeArr):
            second = arr[j]
            result = first + second
            if result == target:
                return [i, j]

    return []


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9

    print(twosum(arr, target))
    print(twosum_sol1(arr, target))

    print("\n")

    arr = [3, 2, 4]
    target = 6

    print(twosum(arr, target))
    print(twosum_sol1(arr, target))

    print("\n")

    arr = [3, 3]
    target = 6

    print(twosum(arr, target))
    print(twosum_sol1(arr, target))

    print("\n")

    arr = [-1, -2, -3, -4, -5]
    target = -8

    print(twosum(arr, target))
    print(twosum_sol1(arr, target))

    print("\n")

    arr = [0, 4, 3, 0]
    target = 0

    print(twosum(arr, target))
    print(twosum_sol1(arr, target))
