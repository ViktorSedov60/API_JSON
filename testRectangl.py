# from rectangl import Rectangle, Square, Circle
#
# r1 = Rectangle(3, 4)
# r2 = Rectangle(12, 5)
#
#
# print("r1.get_area=", r1.get_area())
# print("r2.get_area=", r2.get_area())
#
# sq1 = Square(5)
# sq2 = Square(10)
#
# print(sq1.get_area_square())
# print(sq2.get_area_square())
#
# cr1 = Circle(5)
# cr2 = Circle(5)
#
# print(cr1.get_area_circle())
# print(cr2.get_area_circle())
#
# figure = [r1, r2, sq1, sq2, cr1, cr2]
# for fig in figure:
#     if isinstance(fig,Square):
#         print(fig.get_area_square())
#     elif isinstance(fig,Circle):
#         print(round(fig.get_area_circle(), 2))
#     else:
#         print(fig.get_area())


# def cuts(n):
#
#     if n <= 1:
#         # No cuts possible
#         return 0
#     if n % 2 == 0:
#         # Divide in two halves (takes one cut)
#         # Result is two rolls of length n//2 which can be cut henceforth together
#         # so total will be 1 + cuts for n//2
#         return 1 + cuts(n // 2)
#
#     # Odd: use a cut to reduce to an even number, and find cuts for the even number n-1
#     return 1 + cuts(n - 1)

# # Test
# for n in [0, 1, 2, 3, 5, 6, 16]:
#     print(f'N {n}, cuts {cuts(n)}')



# import math
#
# print(round(10000 / math.log2(10000)))
#
# def p(n):
#     if n == 0:
#
#         print("конец")
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)


# def par_checker(string):
#     stack = [(5+6)*(7+8)/(4+3)]  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0

# par_checker([(5+6)*(7+8)/(4+3)])

pars = {")": "(", "]": "["}

# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0


N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди


def do():  # выполняем приоритетную задачу
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0  # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max  # и циклично перемещаем указатель

def show(): # выводим приоритетную задачу
    print("Задача №%d в приоритете" % (queue[head]))

def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0

def size(): # получаем размер очереди
    if is_empty(): # если она пуста
        return 0 # возвращаем ноль
    elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
        return N_max # значит очередь заполнена
    elif head > tail: # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else: # или если хвост стоит правее начала
        return tail - head


def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max





while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")
