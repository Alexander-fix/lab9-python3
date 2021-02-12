# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Payment (зарплата). В классе должны быть представлены поля:
# фамилия-имя-отчество, оклад, год поступления на работу, процент надбавки,
# подоходный налог, количество отработанных дней в месяце, количество рабочих
# дней в месяце, начисленная и удержанная суммы. Реализовать методы: вычисления
# начисленной суммы, вычисления удержанной суммы, вычисления суммы, выдаваемой
# на руки, вычисления стажа. Стаж вычисляется как полное количество лет, 
# прошедших от года поступления на работу, до текущего года. Начисления
# представляют собой сумму, начисленную за отрабо танные дни, и
# надбавки, то есть доли от первой суммы. Удержания представ ляют собой
# отчисления в пенсионный фонд (1% от начисленной суммы) и подоходный налог. 
# Подоходный налог составляет 13% от начисленной сум мы без отчислений в
# пенсионный фонд.

class Payment:

    def __init__(
        self,
        name=' ',
        year=0,
        oklad=0,
        percent=0,
        workedday=0,
        workingday=1
    ):

        self.name = str(name)
        self.year = int(year)
        self.oklad = int(oklad)
        self.percent = float(percent)
        self.workedday = int(workedday)
        self.workingday = int(workingday)
        self.amount = 0
        self.heldAmount = 0
        self.handAmount = 0
        self.expir = 0

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def read(self):
        name = input('Введите Ф.И.О: ')
        oklad = input('Введите оклад: ')
        year = input('Введите год вашего поступления на работу: ')
        percent = input('Введите процент надбавки: ')
        workedday = input('Введите количество отработанных дней в месяце: ')
        workingday = input('Введите количество рабочих дней в месяце: ')

        self.name = str(name)
        self.oklad = int(oklad)
        self.year = int(year)
        self.percent = float(percent)
        self.workedday = int(workedday)
        self.workingday = int(workingday)

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def display(self):
        print(f"Начисленная зарплата: {round(self.amount)}")
        print(f"Сумма вычетов: {round(self.heldAmount)}")
        print(f"Выданная на руки заработная плата: {round(self.handAmount)}")
        print(f"Размер трудового стажа: {self.expir} ")

    def accruedAmount(self):
        a = self.oklad / self.workingday
        b = a * self.workedday
        percent = self.percent / 100 + 1
        self.amount = b * percent

    def withheldAmount(self):
        plata = (self.oklad / self.workingday) * self.workedday
        self.heldAmount = (plata * 0.13) + (plata * 0.01)

    def handedAmount(self):
        self.handAmount = self.amount - self.heldAmount

    def experience(self):
        self.expir = 2021 - self.year


if __name__ == '__main__':
    s = Payment()
    s.read()
    s.display()
