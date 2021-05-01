def getLargestNumber(arr):
    arr = list(set(arr))
    return arr[len(arr) - 1]


if __name__ == '__main__':
    lefty = [12, 13, 8, 10, 17]
    print(lefty)
    lefty = list(set(lefty))
    print(lefty)
    maxNum = lefty[len(lefty) - 1]
    print(f"Maximum Number is {maxNum}")

    print(f"The Largest Number is {getLargestNumber(lefty)}")
