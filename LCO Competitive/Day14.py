def printAllCombination(arr):
    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return [arr]

    I = []
    for i in range(len(arr)):
        m = arr[i]
        remLst = arr[:i] + arr[i+1:]
        for p in printAllCombination(remLst):
            I.append([m] + p)

    return I


def fourPairCombination(arr):
    combination = []
    for person in arr:
        for ret in arr:
            temp = []
            for com_person in arr:
                if person != ret:
                    temp.append(ret)
                temp.append(person)
            combination.append(temp)
    print(combination)


if __name__ == '__main__':
    people = ['Ram', 'Anuj', 'Deepak', 'Ravi']
    fourPairCombination(people)
    print("================")
    print(printAllCombination(people))
