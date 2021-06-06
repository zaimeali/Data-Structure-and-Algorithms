# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def left_rotation(arr, rotate):
    for i in range(rotate):
        temp = arr[1:] + arr[:1]
        arr = temp
    return arr


def sol2(arr, rotate):
    return arr[rotate:] + arr[:rotate]


if __name__ == '__main__':
    repeat1 = 4
    arr1 = [1, 2, 3, 4, 5]

    print(left_rotation(arr1, repeat1))
    print(sol2(arr1, repeat1))
