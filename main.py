"""Documentation to a programm"""


def create_rectangle():
    while True:
        print("Введите координату x левой верхней точки прямоугольника")
        x1 = int_check()
        print("Введите координату y левой верхней точки прямоугольника")
        y1 = int_check()
        print("Введите координату x правой нижней точки прямоугольника")
        x2 = int_check()
        print("Введите координату y правой нижней точки прямоугольника")
        y2 = int_check()
        if x1 < x2 and y1 > y2 and x1 != x2 and y1 != y2:
            break
        else:
            print("Неправильный ввод, введите числа еще раз")
    return [x1, y1, x2, y2]


def int_check():
    """Function docs"""
    value = input()
    try:
        int(value)
    except ValueError:
        print('Ошибка. Некорректный тип данных. Введите число')
        value = int_check()
    return int(value)


def cg_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    """Function docs"""
    centre1 = [(x2 - x1) / 2 + x1, (y1 - y2) / 2 + y2]
    centre2 = [(x4 - x3) / 2 + x3, (y3 - y4) / 2 + y4]
    if centre1[0] > centre2[0]:
        delta_x = centre1[0] - centre2[0]
    else:
        delta_x = centre2[0] - centre1[0]
    if centre1[1] > centre2[1]:
        delta_y = centre1[1] - centre2[1]
    else:
        delta_y = centre2[1] - centre1[1]
    print((delta_y ** 2 + delta_x ** 2) ** 0.5)


def corner_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    """Function docs"""
    if x2 > x1:
        deltax1 = x2 - x1
    else:
        deltax1 = x1 - x2

    if y2 > y1:
        deltay1 = y2 - y1
    else:
        deltay1 = y1 - y2

    if x3 > x4:
        deltax2 = x3 - x4
    else:
        deltax2 = x4 - x3

    if y3 > y4:
        deltay2 = y3 - y4
    else:
        deltay2 = y4 - y3
    print((deltax1 ** 2 + deltay1 ** 2) ** 0.5 + (
            deltax2 ** 2 + deltay2 ** 2) ** 0.5)


def main():
    """Function docs"""
    flag1 = False
    flag2 = False
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    x3 = None
    y3 = None
    x4 = None
    y4 = None
    while True:
        print("Список команд\n"
              "\t1. Создать (изменить) первый прямоугольник\n"
              "\t2. Создать (изменить) второй прямоугольник\n"
              "\t3. Найти расстояние между центрами\n"
              "\t4. Найти сумму расстояний между верхними левыми и нижними "
              "правыми углами\n"
              "\t5. Завершить программу\n")
        print("Введите номер команды:")
        action = int_check()
        if action == 1:
            x1, y1, x2, y2 = create_rectangle()
            flag1 = True
        elif action == 2:
            x3, y3, x4, y4 = create_rectangle()
            flag2 = True
        elif action == 3 and flag1 and flag2:
            cg_distance(x1, y1, x2, y2, x3, y3, x4, y4)
        elif action == 4 and flag1 and flag2:
            corner_distance(x1, y1, x2, y2, x3, y3, x4, y4)
        elif action == 5:
            break
        else:
            print("Такой команды нет, либо прямоугольники не созданы")


if __name__ == "__main__":
    main()
