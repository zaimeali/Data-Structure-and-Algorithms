def binary_sort(arr):
    arr_len = len(arr) - 1
    for x in range(arr_len):
        for y in range(arr_len - x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    
    return arr

unsort_arr = [7, 5, 1, 8, 3]
print("Unsorted Array")
print(unsort_arr)

print("\nSorted Array")
print(binary_sort(unsort_arr))