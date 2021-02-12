# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triad (тройка чисел); определить методы изменения полей и
# вычисления суммы чисел. Определить производный класс Triangle
# с полями-сторонами. Определить методы вычисления углов и площади
# треугольника.

import math


class Triad:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        self.__b = b

    def get_c(self):
        return self.__c

    def set_c(self, c):
        self.__c = c

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        for part in parts:
            if part == 0:
                raise ValueError()
        self.set_a(parts[0])
        self.set_b(parts[1])
        self.set_c(parts[2])

    def sum(self):
        return self.__a + self.__b + self.__c


class Triangle(Triad):
    def __init__(self, a=0, b=0, c=0, alpha=0, beta=0, gamma=0):
        super(Triangle, self).__init__(a, b, c)
        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma

    def __angles(self):
        self.__alpha = math.degrees(math.acos((self.get_b() ** 2 + self.get_c() ** 2 - self.get_a() ** 2)
                                              / (2 * self.get_c() * self.get_b())))
        self.__beta = math.degrees(math.acos((self.get_a() ** 2 + self.get_c() ** 2 - self.get_b() ** 2)
                                             / (2 * self.get_a() * self.get_c())))
        self.__gamma = math.degrees(math.acos((self.get_a() ** 2 + self.get_b() ** 2 - self.get_c() ** 2)
                                              / (2 * self.get_a() * self.get_b())))
        return self.__alpha, self.__beta, self.__gamma

    @property
    def get_angles(self):
        return self.__angles()

    def read(self, prompt=None):
        Triad.read(self, prompt)
        return self.get_angles

    def square(self):
        p = (self.get_a() + self.get_b() + self.get_c()) * 0.5
        return math.sqrt(p * (p - self.get_a()) * (p - self.get_b()) * (p - self.get_c()))


if __name__ == '__main__':
    T1 = Triangle()
    T1.read(f'Стороны треугольника: ')
    print("Искомые величины: \n"
          "Углы треугольника: {} \n"
          "Сумма сторон: {} \n"
          "Площадь {}".format(T1.get_angles, T1.sum(), T1.square()))
