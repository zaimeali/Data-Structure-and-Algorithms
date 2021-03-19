def insertion_sort(arr):
    for x in range(1, len(arr)):
        k = arr[x]  # element present at index 1
        j = x - 1
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
    return arr


unsort_arr = [7, 5, 1, 8, 3]
print("Unsorted Array")
print(unsort_arr)

print("\nSorted Array")
print(insertion_sort(unsort_arr))