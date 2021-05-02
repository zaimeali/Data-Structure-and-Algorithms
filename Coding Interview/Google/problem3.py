# Google Video https://www.youtube.com/watch?v=XKu_SEDAykw

# [1, 2, 3, 9] no pair equal to 8
# [1, 2, 4, 4] => 4, 4 = 8

def solution1(arr, result):  # Complexity: O(n) because it is linear
    # arr.sort() # if sorting then complexity will be O(N*logN)
    low = 0
    high = len(arr) - 1

    while low < high:
        val = arr[low] + arr[high]
        if val == result:
            return True, (arr[low], arr[high])
        if val > result:
            high -= 1
        if val < result:
            low += 1

    return False


def solution2(arr, result):  # Linear Solution O(n)
    comp = set()
    for num in arr:
        if num in comp:
            return True, (num, result - num)
        comp.add(result - num)

    return False


if __name__ == '__main__':
    arr1 = [1, 2, 3, 9]
    arr2 = [1, 2, 4, 4]
    arr3 = [7, 4, 1, 2]
    arr4 = [5, 2, 9, 3]

    result = 8

    # if not sorted first sort
    # arr.sort()

    print("Solution 1:")
    print(solution1(arr1, result))
    print(solution1(arr2, result))
    print(solution1(arr3, result))
    print(solution1(arr4, result))

    print("-=-=-=-=-=-=-=-")

    print("Solution 2:")
    print(solution2(arr1, result))
    print(solution2(arr2, result))
    print(solution2(arr3, result))
    print(solution2(arr4, result))

    print("-=-=-=-=-=-=-=-")
