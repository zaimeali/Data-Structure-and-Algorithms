if __name__ == '__main__':
    cup500 = [0, 0, 0, 0, 0]
    cup300 = [0, 0, 0]

    dishCup = 200

    for i in range(len(cup500)):
        cup500[i] = 100

    for j in range(len(cup300)):
        cup300[j] = cup500[j]
        cup500[j] = 0

    if sum(cup500) == dishCup:
        print("200ML Done")
    else:
        print("Use Different Method")
