# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Inputs:
#   n = 9
#   arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# Output:
#   3

def sockMerchant(n, ar):
    matched = 0
    index = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if i in index:
                break
            if ar[i] == ar[j]:
                index.append(j)
                matched += 1
                break
    return matched


if __name__ == "__main__":
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
