def shell_sort(arr):
    gap = len(arr) // 2
    while(gap > 0):
        for x in range(gap, len(arr)):
            y = arr[x]
            z = x
            while z >= gap and arr[z-gap]>y:
                arr[z] = arr[z-gap]
                z -= gap

            arr[z] = y
        gap //= 2

    return arr


unsort_arr = [7, 5, 1, 8, 3]
print("Unsorted Array")
print(unsort_arr)

print("\nSorted Array")
print(shell_sort(unsort_arr))