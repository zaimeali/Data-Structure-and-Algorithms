def calculate_amount(competitor_1, competitor_2):
    name1 = competitor_1['name']
    name2 = competitor_2['name']

    price1 = competitor_1['price']
    price2 = competitor_2['price']

    quantity1 = competitor_1['quantity']
    quantity2 = competitor_2['quantity']

    totalSold_1 = price1 * quantity1
    totalSold_2 = price2 * quantity2

    if totalSold_1 > totalSold_2:
        print(f"{name1} sold the most with the total amount of {totalSold_1}")
    else:
        print(f"{name2} sold the most with the total amount of {totalSold_2}")


if __name__ == '__main__':

    quantity1 = int(input("How much glasses Kara sold: "))
    quantity2 = int(input("How much glasses Rani sold: "))

    kara = {
        "name": "kara",
        "price": 5,
        "quantity": quantity1
    }
    rani = {
        "name": "rani",
        "price": 7,
        "quantity": quantity2
    }

    calculate_amount(kara, rani)
