if __name__ == '__main__':
    try:
        totalCost = 0

        numSweaters = 3
        priceSweater = 68

        numComputerGames = 1
        priceComputerGame = 75

        numBracelets = 2
        priceBracelet = 43

        numBracelets -= 1  # return one bracelet
        priceComputerGame -= 10
        totalCost = (numSweaters * priceSweater) + (numComputerGames *
                                                    priceComputerGame) + (numBracelets * priceBracelet)

        print(f"Total Cost is {totalCost}")

    except:
        print('Error')
