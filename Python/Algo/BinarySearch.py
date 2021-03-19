def binary_search(arr, n, key):
    l = 0
    matched = False
    while(l <= n and not matched):
        mid = (l+n) // 2
        if arr[mid] == key:
            matched = True
            break
        else:
            if key < arr[mid]:
                n = mid - 1
            else: 
                l = mid + 1
    if(matched): return mid
    else: return -1

arr = [3, 2, 0, 9, 5]
key = 8
n = len(arr) - 1

search = binary_search(arr, n, key)
if search == -1:
    print('Key is not present')
else:
    print("Key is present at", search)