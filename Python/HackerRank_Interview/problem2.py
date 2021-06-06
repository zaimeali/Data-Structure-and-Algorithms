# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def split_str(string):
    return [char for char in string]


def count_first_char(string):
    first_char = string[0]
    count = 0
    for char in string:
        if char == first_char:
            count += 1
    return count


def repeat_string(string, num):
    if len(string) == 1:
        return num
    result = ""
    for n in range(num):
        for char in split_str(string):
            if len(result) == num:
                break
            result += char

    return count_first_char(result)


if __name__ == '__main__':
    print(repeat_string('aba', 10))
    print(repeat_string('a', 1000000000000))
    print(repeat_string('x', 970770))
