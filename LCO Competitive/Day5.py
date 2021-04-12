def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def best_record(arr):
    sort_round = bubble_sort(arr)
    min_round = sort_round[0]
    return min_round


if __name__ == '__main__':
    round = [66, 57, 54, 53, 64, 52, 59]
    best_round = best_record(round)
    print(f"Best Round: {best_round}")
