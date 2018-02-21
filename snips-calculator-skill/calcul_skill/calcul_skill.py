# coding: utf-8

from math import sqrt

def type_checker(number_to_check):
    if number_to_check % 1 == 0:
        number_to_check = int(float(number_to_check))
    return number_to_check

class Calculator:
    def __init__(self,locale=None):
        pass
    def addition(self, number1, number2):
        total = number1 + number2
        total = type_checker(total)
        return "Le résultat est {}".format(total)

    def division(self, number1, number2):
        total = number1 / number2
        total = type_checker(total)
        return "Le résultat est {}".format(total)

    def multiplication(self, number1, number2):
        total = number1 * number2
        total = type_checker(total)
        return "Le résultat est {}".format(total)

    def squared(self, number1):
        total = number1 * number1
        total = type_checker(total)
        return "Le résultat est {}".format(total)

    def racine(self, number1):
        total = sqrt(number1)
        total = type_checker(total)
        return "Le résultat est {}".format(total)

if  __name__ == "__main__":
    heysnips = Calculator()
    """
    print heysnips.addition(3,4)
    print heysnips.soustraction(2, 3)
    print heysnips.multiplication(2, 3)
    print heysnips.squared(3)
    #var = float(str(heysnips.racine(2))
    #print round(2.48687, 3)
    """
