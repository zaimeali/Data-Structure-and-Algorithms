# https://www.youtube.com/watch?v=hPUSrHPdo-4

# Implement a func which given an array of integers, return a new array for which
#   every index carries the value of the product of the remaining elements

# Test Case: 1
#  Input: [1, 3, 2, 4, 5]
#  Output: [120, 40, 60, 30, 24]

# Test Case: 2
#  Input: [4, 10, 3]
#  Output: [30, 12, 40]

def arrMultiply(arr):
    result = 1
    for item in arr:
        result *= item
    return result


def productArrSolution1(arr):   # O(n^2)
    resultArr = []
    arrSize = len(arr)
    for i in range(arrSize):
        productRes = 1
        if i == 0:
            resultArr.append(arrMultiply(arr[i+1:arrSize]))
            continue
        if i == arrSize - 1:
            resultArr.append(arrMultiply(arr[:i]))
            continue
        productRes *= arrMultiply(arr[:i])
        productRes *= arrMultiply(arr[i+1:])
        resultArr.append(productRes)

    return resultArr


def productArrSolution2(arr):  # O(N^2)
    # delete that index and multiply rest
    arrSize = len(arr)
    productArr = []
    for i in range(arrSize):
        temp = arr[:i] + arr[i+1:]
        productArr.append(arrMultiply(temp))
    return productArr


if __name__ == '__main__':
    testcase1 = [1, 3, 2, 4, 5]
    print(testcase1)
    print(productArrSolution1(testcase1))
    print(productArrSolution2(testcase1))

    print()

    testcase2 = [4, 10, 3]
    print(testcase2)
    print(productArrSolution1(testcase2))
    print(productArrSolution2(testcase2))
