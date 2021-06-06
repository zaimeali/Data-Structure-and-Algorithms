def arrayManipulation(n, queries):
    arr = []
    for i in range(n):
        arr.append(0)

    for item in queries:
        l = item[0] - 1
        r = item[1]
        k = item[2]

        for i in range(l, r):
            arr[i] += k

    return max(arr)


if __name__ == '__main__':
    queries = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100],
    ]

    n = 5

    result = arrayManipulation(n, queries)
    print(result)
