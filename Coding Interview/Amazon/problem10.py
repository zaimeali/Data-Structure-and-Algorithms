def find_kth_permutation(v, k, result):
    if len(v) == 0:
        return result
    permutation = 1
    for i in range(1, len(v) + 1):
        permutation *= i

    return permutation


if __name__ == '__main__':
    try:
        v = [1, 2, 3]
        # v = []
        k = 6
        print(find_kth_permutation(v, k, []))
    except:
        print('Error')
