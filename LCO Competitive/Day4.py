def lco_solution(bought, quantity):
    totalContainer = 0
    while bought >= quantity:
        bought -= quantity
        totalContainer += 1
    print(f"Number of Container: {totalContainer}")


def total_package(bought, quantity):
    num_package = bought // quantity
    print(f"Number of packages are: {num_package}")


if __name__ == '__main__':
    bought = 400
    package = 8

    total_package(bought, package)
    lco_solution(bought, package)
