import numpy as np
from colorama import init, Fore, Back, Style
import argparse


def found(path_arr0, start_point, fin_point):
    """
    нахождение путей
    :param path_arr0: входной массив (в фомате 1;0)
    :param start_point: начальная точка
    :param fin_point: конечная точка
    :return:
    """
    path_arr = path_arr0.copy() * -1
    path_arr[start_point] = 1
    weight = 1
    for i in range(len(path_arr) * len(path_arr[0])):
        weight += 1
        for y in range(len(path_arr)):
            for x in range(len(path_arr[y])):
                if path_arr[y][x] == (weight - 1):
                    if y > 0 and path_arr[y - 1][x] == 0:
                        path_arr[y - 1][x] = weight
                    if y < (len(path_arr) - 1) and path_arr[y + 1][x] == 0:
                        path_arr[y + 1][x] = weight
                    if x > 0 and path_arr[y][x - 1] == 0:
                        path_arr[y][x - 1] = weight
                    if x < (len(path_arr[y]) - 1) and path_arr[y][x + 1] == 0:
                        path_arr[y][x + 1] = weight

                    if (abs(y - fin_point[0]) + abs(x - fin_point[1])) == 1:
                        path_arr[fin_point[0]][fin_point[1]] = weight
                        return weight, path_arr
    Exception("Путь не найден!")


def best_path(path_arr, fin_point, result0):
    """
    Вывод наилучшего пути
    :param path_arr: массив всех путей
    :param fin_point: конечная точка
    :param result0: массив на основе которого печатается
    :return:
    """
    result = result0.copy()
    y = fin_point[0]
    x = fin_point[1]
    weight = path_arr[fin_point]
    result[fin_point] = -weight
    while weight:
        weight -= 1
        if y > 0 and path_arr[y - 1][x] == weight:
            result[y - 1][x] = -weight  # 'down'
            y -= 1
        elif y < (len(path_arr) - 1) and path_arr[y + 1][x] == weight:
            result[y + 1][x] = -weight  # 'up'
            y += 1
        elif x > 0 and path_arr[y][x - 1] == weight:
            result[y][x - 1] = -weight  # 'right'
            x -= 1
        elif x < (len(path_arr[y]) - 1) and path_arr[y][x + 1] == weight:
            result[y][x + 1] = -weight  # 'left'
            x += 1
    return result  # result[1:]


def get_mas_in_out_point(labirint):
    """
    Поиск начальных и конечных точек
    :param labirint: входной лабиринт(0;1;2)
    :return:
    """
    poz_out = []
    le = len(labirint)
    # print(le)
    lem = le - 1

    poz_in = []
    for i in range(le):
        for j in range(le):
            if labirint[i, j] == 2:
                poz_in.append((i, j))

    for i in range(le):
        for j in range(le):
            if (i == 0 or i == lem or j == 0 or j == lem) and labirint[i, j] == 0:
                poz_out.append((i, j))

    return poz_in, poz_out


def color_print(arr):
    """
       Выводит красиво матрицу
       :param arr: массив
       :return:
       """
    init()
    for i in arr:
        print(Back.GREEN, end="")
        for j in i:
            if j == 0:
                print(Fore.BLACK + '0', end="   ")
            elif j == 1:
                print(Fore.RED + '1', end="   ")
            elif j < 0:
                if j >= -9:
                    print(Fore.BLUE + str(j), end="  ")
                else:
                    print(Fore.BLUE + str(j), end=" ")
        print(Style.RESET_ALL)
    print(Style.RESET_ALL, end="")


def str_to_list(s):
    """
    строка в numpy массив
    :param s:
    :return:
    """
    s = s.split("\n")
    ll = None
    for ss in s:
        if ll is None:
            ll = np.array([[int(i) for i in ss.split()]])
            # print(ll)
        else:
            # print(ss)
            ll = np.append(ll, [[int(i) for i in ss.split()]], axis=0)
            # print(ll)
    return ll


def file_to_arr(f_name):
    """
    Прочитать файл в массив
    :param f_name: имя файла
    :return: np-array
    """
    with open(f_name, "r") as file:
        s = file.readlines()
    s = ''.join(s)
    return str_to_list(s)


def get_all_param_path(poz_in, poz_outs, labirint):
    """
    Все варианты 'лучших' путей выхода
    :param poz_in: наачальная точка
    :param poz_outs: список выходов
    :param labirint: лабиринт
    :return: [len, start, end]...
    """
    param = []
    for poz_out in poz_outs:
        w, _ = found(labirint, poz_in, poz_out)
        param.append((w, poz_in, poz_out))
    return param


def get_best_param_of_two(param1, param2):
    """
    Наилучший выход для 2 участников
    :param param1: лучшие параметры первого
    :param param2: лучшие параметры второго
    :return: (len, [ [start1, end1], [start2, end2] ])
    """
    best_param = None
    for p1 in param1:
        for p2 in param2:
            if p1[2] != p2[2]:
                if best_param is None or best_param[0] > p1[0] + p2[0]:
                    best_param = (p1[0] + p2[0], [[p1[1], p1[2]], [p2[1], p2[2]]])
    return best_param


def get_print_param(best_param, labirint, lab_print):
    """
    Напечатать лучший выход
    :param best_param: лучший параметр
    :param labirint: лабиринт
    :param lab_print: лабиринт на который накладываем
    :return: np-array
    """
    _, path = found(labirint, best_param[0], best_param[1])
    return best_path(path, best_param[1], lab_print)


def main():
    parser = argparse.ArgumentParser(description='minotavr')
    parser.add_argument('f', type=str, help="Path to the query file")
    args = parser.parse_args()
    labirint0 = file_to_arr(args.f)
    # labirint0 = file_to_arr('arr.txt')
    labirint = labirint0 % 2

    poz_ins, poz_outs = get_mas_in_out_point(labirint0)

    params = []
    for poz_in in poz_ins:
        params.append(get_all_param_path(poz_in, poz_outs, labirint))

    best_params = get_best_param_of_two(params[0], params[1])

    res = get_print_param(best_params[1][0], labirint, labirint)
    res = get_print_param(best_params[1][1], labirint, res)

    color_print(res)


if __name__ == '__main__':
    main()
