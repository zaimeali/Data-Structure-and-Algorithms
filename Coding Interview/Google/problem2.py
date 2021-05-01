# https://www.youtube.com/watch?v=lD-LuK_VGZI

# find pair of numbers equal to result

def find_pair(arr, result):
    check = []
    for x in arr:
        div = result // x
        if div in check:
            return (div, x)
        check.append(x)
    return None


if __name__ == '__main__':
    arr = [2, 4, 10, 1, 6, 5, 40, -1]
    result = 20
    print(find_pair(arr, result))
