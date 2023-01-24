l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def board():
    for i in range(3):
        print(l[0 + i * 3], " ", l[1 + i * 3], " ", l[2 + i * 3])


def take_in(player):  # делаем ход
    while True:
        num = input("Введите номер поля для ввода для " + player)
        if not (num in "123456789"):  # проверяем на корректность ввода
            print("не верно, введите число от 1 до 9")
            continue
        num = int(num)
        if str(l[num - 1]) in "XO":  # проверяем занятость поля
            print("Это поле уже занято")
            continue
        l[num - 1] = player # если поле свободно и все верно введено ставим символ игрока
        break

def win():
    coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9),
             (3, 5, 7)]  # выиграшные комбинации
    for i in coord:  # проходим по комбинациям и сверям с тем что вводили пользователи
        if l[i[0] - 1] == l[i[1] - 1] == l[i[2] - 1]:
            return l[i[1] - 1]
    else:
        return False


def play_game():
    global l
    c = 0
    while True:
        board()
        if c % 2 == 0:
            take_in("X")
        else:
            take_in("O")
        check = win()
        if check:
            board()
            print(check, "Победил в катке")
            ng = input("Сыграем еще раз? Y | N ")
            if ng == "Y" or ng == "y":
                l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                play_game()
            else:
                break
        c += 1
        if c >= 8:
            board()
            print("ничья в этой партии")
            ng = input("Сыграем еще раз? Y | N ")
            if ng == "Y" or ng == "y":
                l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                play_game()
            else:
                break


play_game()
