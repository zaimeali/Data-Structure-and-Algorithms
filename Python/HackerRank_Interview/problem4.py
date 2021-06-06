# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def num_delete(first, second):
    delete = 0
    for char in first:
        if not char in second:
            delete += 1
    for char in second:
        if not char in first:
            delete += 1
    return delete


if __name__ == '__main__':
    first = 'cde'
    second = 'abc'

    print(num_delete(first, second))
