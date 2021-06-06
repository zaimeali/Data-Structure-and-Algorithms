# Pivot = Half

#  return half(pivot) if there exists an element in the array such that the sum of elements to its left is equal to the sum
#  of elements to its right. Otherwise, return 0.

def solution1(arr):
    pivot = len(arr) // 2
    l = sum(arr[:pivot])
    r = sum(arr[pivot+1:])

    while True:
        if l == r:
            break
        if l < r:
            pivot += 1
        if l > r:
            pivot -= 1
        l = sum(arr[:pivot])
        r = sum(arr[pivot+1:])

    print(pivot)


def solution2(arr):
    l = 0
    r = sum(arr)

    pivot = 0
    for i in range(len(arr)):
        r -= arr[i]
        if l == r:
            pivot = i
            break
        l += arr[i]

    print(pivot)


if __name__ == '__main__':
    test_case1 = [1, 2, 3, 4, 6]
    solution1(test_case1)
    solution2(test_case1)

    test_case2 = [1, 2, 3, 3]
    solution1(test_case2)
    solution2(test_case2)
