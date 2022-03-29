# S figur-c
# herimetr treugiol, S P=a+b+c; S=Vp(p-a)(p-c)(p-b)
# priamougol P=2(a+b); S=ab
# krug P=2пr; S=пr**

import math
# print("введите длины сторон треугольника")
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# p = a+b+c / 2
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print("P=%d; s=%.2f" % (a + b + c, s))


# print("введите длины сторон прямоугольника")
# a = int(input("a="))
# b = int(input("b="))
# print("P=%d; s=%.2f" % ((a + b) * 2, a * b))


# print("введите радиус круга")
# r = int(input("r="))
# print("P=%.2f; s=%.2f" % (2 * math.pi * r, math.pi * r ** 2))

# print(" 1- прямоугольник, 2- треугольник, 3- груг")
# figure = input("Выберите фигуру")
#
# if figure == "1":
#     a = float(input('a='))
#     b = float(input('b='))
#     print("P=%d; s=%.2f" % ((a + b) * 2, a * b))
#
# elif figure == "2":
#     a = float(input('a='))
#     b = float(input('b='))
#     c = float(input('c='))
#     p = a + b + c / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %2f" % s)
#
# elif figure == "3":
#     r = float(input("Радиус круга R="))
#     print("Площадь: %.2f" % (math.pi * r ** 2))
#
# else:
#     print('Ошибка ввода')

#  # 2 task извлеч цифры из числа и манипуляции с ними, например из трехзначного
# n = int(input('Введите трeхзначное число: '))
# nam1 = n % 10
# print(nam1)
# nam2 = n % 100 // 10
# print(nam2)
# nam3 = n // 100
# print(nam3)
# print('Сумма цифр:', nam1 + nam2 + nam3)
# print('Произведение цифр:', nam1 * nam2 * nam3)


# # найти максимальное число
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
#
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c
# print(m)

# # среди чисел найти среднее
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
#
# if (b < a < c or c < a < b):
#     print("Среднее ", a)
# elif (a < b < c or c < b < a):
#     print('Среднее ', c)
# else:
#     print('Среднее ', c)


# # Найти нечетное число
# from  random import  random
# a = int(random() * 100)
# print(a)
# b = int(random() * 100)
# print(b)
#
# if a % 2 == 0 and b % 2 == 0 or a % 2 != 0 and b % 2 != 0:
#     a +=1
# print(a, b)
# if a % 2 != 0:
#     print(a)
# else:
#     print(b)


# # Угадай число
# import  random
# num = random.randint(1, 100)
# while True:
#     print("")
#     quess = int(input("введите число  "))
#     if quess == num:
#         print(" Угадал OK")
#         break
#     elif quess < num:
#         print("Ввел меньшее число")
#     elif quess > num:
#         print("Ввел большее число")


# # Переверни число
# num = int(input('Введите  число: '))
# num1 = 0
#
# while num > 0:
#     digit = num % 10 # последняя цифра
#     num = num // 10  # удаляем последнюю цифру
#     num1 = num1 * 10
#     num1 += digit
# print('Обратное ему число:  ', num1 )

# # посчитать четные и нечетные цифры числа, введенные с клавы
# a = int(input('Введите  число: '))
# even = 0
# odd = 0
# while a > 0:
#     if a % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     a = a // 10
# print("Even: %d, odd: %d" % (even, odd))

# # Вычислить факториал циклом while и for
# n = int(input('Введите  число: '))
# factorial = 1
# while n > 1 :
#     factorial *= n
#     n -= 1
# print(factorial)
#
# for i in range(2, n + 1):
#     factorial *= i
# print(factorial)

# # Вложенный цикл на примере таблицы умножения
# for i in range(1, 10):
#     for j in range (1, 10):
#         print(i * j, end="\t")
#     print("\n")

# # циклом по последовательности
# lst = []
# for i in range(18, 1 ,-4):
#     lst.append(i)
# print(lst)

# # из последовательности вывести элементы которые и меньше 30 и делятся на 3 без остатка
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
#
# sm = 0
# for i in lst:
#     if(i < 30) and (i % 3 == 0):
#         print(i)
#     else:
#         sm += i
# print(sm)

# def calc(a, b, operation):
#
#     if operation == "+":
#         result = a + b
#     elif operation == "-":
#         result = a - b
#     elif operation == "*":
#         result = a * b
#     elif operation == "/":
#         if b != 0:
#             result = a / b
#         else:
#             result = "xren"
#     return result
#
#
# if __name__ == "__main__":
#     print(calc(30, 15, "+"))
#     print(calc(30, 15, "-"))
#     print(calc(30, 15, "*"))
#     print(calc(30, 15, "/"))


# class НазваниеКласса:
#   методы_класса
# Название_объекта = название класса

# class Person:
#     name = "Viktor"
#     def display_info(self):
#         print("Hi, my name is ", self.name)
# person_1 = Person()
# person_1.display_info()


class Progres:
    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.cashe ={}

    def get(self, pos):
        if pos in self.cashe:
            return self.cashe[pos]
        else:
            num = self.start + self.step*pos
            self.cashe[pos] = num
            return num
class A:
    def __init__(self):
        self._a = "123"

    @property
    def a(self):
        return " ".join([self._a, "from A"])

    @a.setter
    def a(self, new):
        if type(new) == str:
            self._a = new




a = A()
print(a.a)
a.a = "12"
print(a.a)
