import numpy as np
from colorama import init, Fore, Back, Style


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


def main():
    # Выход из лабиринта .Волновой алгоритм
    # labirint0 = np.array([
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 0, 2, 0, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    #     [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    #     [1, 0, 1, 1, 0, 1, 0, 0, 2, 1],
    #     [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    #     [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    #     [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    #     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    # ])
    s = "1 1 1 1 1 1 1 1 1 1 \n \
         1 0 0 0 0 2 0 0 0 1 \n \
         1 0 1 1 1 1 0 1 1 1 \n \
         1 0 1 1 0 0 0 1 1 1 \n \
         1 0 1 1 0 1 0 0 2 1 \n \
         1 0 0 0 0 1 0 1 0 1 \n \
         1 1 0 1 1 1 0 1 0 1 \n \
         0 0 1 0 1 1 0 0 0 1 \n \
         1 0 0 0 0 0 0 1 0 1 \n \
         1 0 1 1 1 1 1 1 1 1"

    # Координаты входа [2,0], координаты выхода [7,0]. В которой 1 - это стена, 0 - это путь.
    labirint0 = str_to_list(s)
    # print(labirint0)
    labirint = labirint0 % 2
    # print(labirint0)
    # pozIn = (2, 0)
    # pozOut = (7, 0)

    poz_in, poz_out = get_mas_in_out_point(labirint0)
    # pozIn = poz_in[1]

    param1 = []  # [len, strat, end]
    pozIn = poz_in[0]
    for pozOut in poz_out:
        w, path = found(labirint, pozIn, pozOut)
        param1.append((w, pozIn, pozOut))

    param2 = []  # [len, strat, end]
    pozIn = poz_in[1]
    for pozOut in poz_out:
        w, path = found(labirint, pozIn, pozOut)
        param2.append((w, pozIn, pozOut))

    best_param = []  # [len, start1, end1, start2, end2]
    flag = True
    for p1 in param1:
        for p2 in param2:
            if p1[2] != p2[2]:
                if flag or best_param[0] > p1[0] + p2[0]:
                    flag = False
                    best_param = [p1[0] + p2[0], p1[1], p1[2], p2[1], p2[2]]

    w1, path_best1 = found(labirint, best_param[1], best_param[2])
    # print(best_param)

    result1 = best_path(path_best1, best_param[2], labirint)

    w2, path_best2 = found(labirint, best_param[3], best_param[4])
    result2 = best_path(path_best2, best_param[4], result1)

    color_print(result2)
    # print(result1)
    # print(result2)
    # print(result1 & result2)
    # print(w)
    # result = best_path(path, pozOut, labirint)
    # print(result)


if __name__ == '__main__':
    main()
