if __name__ == '__main__':
    name_str = "Zaime Osama Faraz Mahboob Maaz Anas Ibrahim Zaime Mutahir Atta Anas"
    names = name_str.split(" ")

    unique = set()
    for name in names:
        if name in unique:
            print(name)
        unique.add(name)
