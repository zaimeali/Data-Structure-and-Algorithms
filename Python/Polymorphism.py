class Language:
    def greeting(self): 
        print('Salam')

class Urdu(Language):
    pass

class English(Language):
    def greeting(self):
        print('Hello')

class French(Language):
    def greeting(self):
        print('Bonjour')

# def intro(language):
#     language.greeting()

urdu = Urdu()
print(urdu.greeting())

eng = English()
print(eng.greeting())

french = French()
print(french.greeting())

