from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Square import square
from Calculator.SquareRoot import squareRoot
from Calculator.Division import division
from Calculator.Product import product
from HelperFunctions.TypeTesting import typeFunction


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        if typeFunction(a) == True and typeFunction(b) == True:
            self.result = addition(a, b)
            return self.result

    def subtract(self, a, b):
        if typeFunction(a) == True and typeFunction(b) == True:
            self.result = subtraction(a, b)
            return self.result

    def square(self, a):
        if typeFunction(a) == True :
            self.result = square(a)
            return self.result

    def SquareRoot(self, a):
        if typeFunction(a) == True :
            self.result = squareRoot(a)
            return self.result

    def Division(self, a, b):
        if typeFunction(a) == True and typeFunction(b) == True:
            self.result = division(a, b)
            return self.result

    def Product(self, a, b):
        if typeFunction(a) == True and typeFunction(b) == True:
            self.result = product(a, b)
            return self.result
