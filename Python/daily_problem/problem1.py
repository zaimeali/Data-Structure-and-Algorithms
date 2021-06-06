# Pagination Problem Solution

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

posts = []
temp = []
for i in range(len(arr)):
    if i % 10 == 0 and i > 2:
        posts.append(temp)
        temp = []
        temp.append(arr[i])
    else:
        temp.append(arr[i])

posts.append(temp)

print(arr)
print(posts)
