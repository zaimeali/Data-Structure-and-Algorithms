# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Input: [0, 0, 0, 0, 1, 0]
#   Remove 1 or Exclude -> Indices = [0, 1, 2, 3, 5]
# Output: 0 -> 2 -> 3 -> 5 = 3 Jumps

# Input: [0, 0, 1, 0, 0, 1, 0]
# Output: 0 -> 1 -> 3 -> 4 -> 6 = 4 Jumps

def jumps(arr):
    jump = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            continue
        if i < len(arr) - 1:
            if arr[i] == 0 and arr[i + 1] == 0:
                jump += 1
    # consec = 0
    # index = 0
    # for item in arr:
    #     if item == 1:
    #         index += 1
    #         continue

    #     if (len(arr) - 2) > index:
    #         if arr[item] == 0 and arr[index + 1] == 0 and arr[index + 2] == 0:
    #             index += 1
    #             continue

    #     if item == 0 and (len(arr) - 1 > index):
    #         index += 1
    #         jump += 1
    # for item in range(len(arr)):
    #     if arr[item] == 1:
    #         continue
    #     # if consec == 2:
    #     #     consec = 0
    #     #     jump -= 1
    #     #     continue
    # #         # consec += 1
    #     if (len(arr) - 2) > item:
    #         if arr[item] == 0 and arr[item + 1] == 0 and arr[item + 2] == 0:
    #             print(item, item + 1)
    #             item += 1
    #     if arr[item] == 0 and (len(arr) - 1 > item):
    #         jump += 1

    return jump


if __name__ == '__main__':
    testcase1 = [0, 0, 0, 0, 1, 0]   # Output -> 3 Jumps
    print(jumps(testcase1))

    testcase2 = [0, 0, 1, 0, 0, 1, 0]   # Output -> 4 Jumps
    print(jumps(testcase2))

    testcase3 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]   # Output -> 6 Jumps
    # print(jumps(testcase3))
