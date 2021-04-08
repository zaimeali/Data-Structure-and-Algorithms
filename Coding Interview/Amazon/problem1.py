# 1. Find the missing number in the array

# You are given an array of positive numbers from 1 to n,
# such that all numbers from 1 to n are present except one number x.
# You have to find x. The input array is not sorted.
# Look at the below array and give it a try before checking the solution.

def find_missing(arr):
    try:
        sorted_arr = sorted(arr)
        missing_number = -1
        for i in range(1, len(sorted_arr)):
            if i not in sorted_arr:
                missing_number = i
                break
        return missing_number
    except:
        print('Exception Occured')


if __name__ == '__main__':
    arr = [3, 7, 1, 2, 8, 4, 5]
    print(find_missing(arr))

# Passed 🙂
