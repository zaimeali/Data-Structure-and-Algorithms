from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self): pass

    # @abstractmethod
    # def perimeter(self): pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

# Shape class cannot be initiate with an object
# you have to implement the method in a child class
square = Square(5)
print(square.get_area())