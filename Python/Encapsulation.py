class NickName():
    def __init__(self):
        self.first_name = 'Zaime'
        self.__last_name = 'Ali' # Private

    def get_LastName(self):
        return self.__last_name

    def set_LastName(self, t):
        self.__last_name = t

zaime = NickName()

print(zaime.first_name)
# print(zaime.__last_name) # cannot be accessed because it is private variable
print(zaime.get_LastName())
print(zaime.set_LastName('Rizwan'))
print(zaime.get_LastName())