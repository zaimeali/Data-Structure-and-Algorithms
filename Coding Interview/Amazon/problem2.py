# 2. Determine if the sum of two integers is equal to the given value

# Given an array of integers and a value,
# determine if there are any two integers in the array whose sum is equal to the given value.
# Return true if the sum exists and return false if it does not.

def solution_by_educative(A, val):
    found_values = set()               # for unique value
    for a in A:                        # iterate loop => foreach
        if val - a in found_values:    # checking if calculate value is in set => 10 - 7 = 3
            return True                # if found then true

        # or add that number => 3 and it will be in a list at that 3
        found_values.add(a)

    return False                       # if not found then false


def find_sum_of_two(A, val):
    try:
        found = False
        for x in range(len(A)):
            for y in range(x + 1, len(A)):
                if A[x] + A[y] == val:
                    found = True
                    return found
                    # print(f"{A[x]}+{A[y]}={val}", end=", ")
                    # print(str(A[x])+"+"+str(A[y])+"="+str(val), end=", ")

        # if not(found):
            # print(f"No 2 values sum up to {val}")
        return found

    except:
        print('Exception Occured')


if __name__ == '__main__':
    arr = [5, 7, 1, 2, 8, 4, 3]
    print(find_sum_of_two(arr, 10))
    print(solution_by_educative(arr, 10))

# passed
