# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC): # its nothing but the method where we just have to give fun/method name and then write that fun in second class with retun value but its compulsory to write meths of abs class
  # we can not create methods of abs class we just define func and those func are declared in other class
    @abstractmethod  # we cant create objects of abs meth
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def _init_(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())