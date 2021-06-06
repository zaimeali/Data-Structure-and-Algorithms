# https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/

def naive_pattern_search(search, pattern):
    sizeSearch = len(search)
    sizePattern = len(pattern)
    for i in range(0, sizePattern - sizeSearch + 1):
        if search == pattern[i:i+sizeSearch]:
            print(f"Pattern found at index {i}")


if __name__ == '__main__':
    print("Test Case 1")
    pattern = "THIS IS A TEST TEXT"
    search = "TEST"
    naive_pattern_search(search, pattern)

    print("\nTest Case 2")
    pattern = "AABAACAADAABAABA"
    search = "AABA"
    naive_pattern_search(search, pattern)
