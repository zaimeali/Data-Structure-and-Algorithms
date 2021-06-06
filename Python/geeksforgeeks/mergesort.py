def mergesort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        L = arr[:r]
        M = arr[r:]

        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [23, 32, 2, 100, 52, 10]
    mergesort(arr)
    print(arr)

# Time Complexity
    # Best => O(n.logn)
    # Worst => O(n.logn)
    # Average => O(n.logn)
# Space Complexity
    # O(n)
