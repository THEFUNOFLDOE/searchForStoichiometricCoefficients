from NSD import nsd, nsk
from numpy import array


class Fraction:
    def __init__(self, num=1, denom=1) -> None:
        self.__num = num
        self.__denom = denom

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def denom(self):
        return self.__denom

    @denom.setter
    def denom(self, denom):
        self.__denom = denom

    def __add__(self, frac):
        newfrac = Fraction()

        if isinstance(frac, float) or isinstance(frac, int):
            frac = Fraction(frac)

        newfrac.__denom = frac.__denom * self.__denom
        newfrac.__num = frac.__denom * self.__num + frac.__num * self.__denom

        k = nsd(newfrac.__num, newfrac.__denom)
        newfrac.__num /= k
        newfrac.__denom /= k

        return newfrac

    def __sub__(self, frac):
        newfrac = Fraction()

        if isinstance(frac, float) or isinstance(frac, int):
            frac = Fraction(frac)

        newfrac.__num = frac.__denom * self.__num - frac.__num * self.__denom
        newfrac.__denom = frac.__denom * self.__denom

        k = nsd(newfrac.__num, newfrac.__denom)
        newfrac.__num /= k
        newfrac.__denom /= k

        return newfrac

    def __mul__(self, frac):
        newfrac = Fraction()

        if isinstance(frac, float) or isinstance(frac, int):
            frac = Fraction(frac)

        newfrac.__num = self.__num * frac.__num
        newfrac.__denom = self.__denom * frac.__denom

        k = nsd(newfrac.__num, newfrac.__denom)
        newfrac.__num /= k
        newfrac.__denom /= k

        return newfrac

    def __truediv__(self, frac):
        newfrac = Fraction()

        if isinstance(frac, float) or isinstance(frac, int):
            frac = Fraction(frac)

        newfrac.__num = self.__num * frac.__denom
        newfrac.__denom = self.__denom * frac.__num

        k = nsd(newfrac.__num, newfrac.__denom)
        newfrac.__num /= k
        newfrac.__denom /= k

        return newfrac

    def __str__(self):
        return f'Fraction({self.__num}, {self.__denom})'

    def __repr__(self):
        return f'Fraction({self.__num}, {self.__denom})'

    def __abs__(self):
        newfrac = Fraction()

        newfrac.__num = abs(self.__num)
        newfrac.__denom = abs(self.__denom)
        return newfrac

    def __gt__(self, frac):
        if isinstance(frac, float) or isinstance(frac, int):
            frac = Fraction(frac)

        if self.__num / self.__denom > frac.__num / frac.__denom:
            return True

        else:
            return False

    def __lt__(self, frac):
        if isinstance(frac, float) or isinstance(frac, int):
            frac = Fraction(frac)

        if self.__num / self.__denom < frac.__num / frac.__denom:
            return True

        else:
            return False

    def getfrac(self):
        return self.__num, self.__denom


# arr1 = array([Fraction(-1, 3), Fraction(1, 4), Fraction(-2, 3), Fraction(1, 5), Fraction(4, -8)])
# arr2 = array([Fraction(1, 6), Fraction(1, 8), Fraction(2, 6), Fraction(1, 10), Fraction(1, 4)])
# print(arr1-arr2)
# print(Fraction(2, 4) > Fraction(1, 2))
