def selection_sort(arr):
    for x in range(len(arr)):
        minimum = x  # assuming first index element as minimum
        for y in range(x + 1, len(arr)):
            if(arr[y] < arr[minimum]):
                minimum = y
        arr[x], arr[minimum] = arr[minimum], arr[x]

    return arr


unsort_arr = [7, 5, 1, 8, 3]
print("Unsorted Array")
print(unsort_arr)

print("\nSorted Array")
print(selection_sort(unsort_arr))