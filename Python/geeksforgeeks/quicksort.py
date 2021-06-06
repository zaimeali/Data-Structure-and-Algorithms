def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


if __name__ == '__main__':
    arr = [23, 32, 2, 100, 52, 10]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)

# Time Complexity
    # Best => O(n.log n)
    # Worst => O(n^2)
    # Average => O(n.log n)
# Space Complexity
    # O(log n)
