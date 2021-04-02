people = [
    {
        "name": "Superman",
        "universe": "DC"
    },
    {
        "name": "Ironman",
        "universe": "Marvel"
    },
    {
        "name": "Starlight",
        "universe": "The Boys"
    },
    {
        "name": "Goku",
        "universe": "Dragon Ball"
    }
]


# def f(person):
#     return person["name"]


# people.sort(key=f)

people.sort(key=lambda person: person["universe"])

print(people)
