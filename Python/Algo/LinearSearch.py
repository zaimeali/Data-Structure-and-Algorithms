def linear_search(arr, n, key):
    for x in range(0, n):
        if(arr[x] == key):
            return x
    return -1

arr = [3, 2, 8, 0, 9, 5]
key = 8
n = len(arr)

search = linear_search(arr, n, key)
if search == -1:
    print('Key is not present')
else:
    print("Key is present at", search)