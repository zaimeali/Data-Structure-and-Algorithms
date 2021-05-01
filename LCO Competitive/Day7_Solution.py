def multiply(x, y):
    if y == 0:
        return 0

    if y > 0:
        return (x + multiply(x, y-1))

    if y < 0:
        return -multiply(x, -y)


people = 1200000
days = 365
print(multiply(people, days))
