# Здравствуй, ментор, хорошего дня!

# Список выводящий поле
pole = ["  | a | b | c |", #0
        "---------------", #1
        "1 ", "|   ", "|   ", "|   |", #5
        "---------------", #6
        "2 ", "|   ", "|   ", "|   |", #10
        "---------------", #11
        "3 ", "|   ", "|   ", "|   |", #15
        "---------------" #16
        ]

L = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"] # список координат для проверки

list_nolik =[] # Список ходов нолика
list_krestik = [] # Список ходов крестика
count = 0 # счётчик раундов

# После "---------------" новая строка
def pole_in_consol():
    for element in pole:
        if element == "---------------":
            print("\n" + element)
        else:
            print(element, end="")
pole_in_consol()


# Ход крестика
def hod_krestik():
    print("Ходит крестик!")
    krestik = str(input("Ваш ход в формате 'xx':"))

    # Словарь крестика с индексами для последующей замены в списке "pole"
    krestik_na_pole = {
        "a1": (3, "| X "),
        "b1": (4, "| X "),
        "c1": (5, "| X |"),
        "a2": (8, "| X "),
        "b2": (9, "| X "),
        "c2": (10, "| X |"),
        "a3": (13, "| X "),
        "b3": (14, "| X "),
        "c3": (15, "| X |")
    }
    # проверка хода
    if krestik in L and krestik in krestik_na_pole and krestik not in list_krestik + list_nolik:
        index, text = krestik_na_pole[krestik]
        pole.pop(index)
        pole.insert(index, text)
        pole_in_consol()
    elif krestik in list_krestik or krestik in list_nolik:  # если место уже занято
        print(f"Это место уже занято: '{krestik}'")
        print("Извините, игра сломана, перезапустите игру.")
        exit()
    else:  # если координаты введены неправильно
        print(f"Координаты '{krestik}' отсутствуют.")
        print("Перезапустите игру и ввердите верные координаты.")
        exit()
    list_krestik.append(krestik)


# Ход нолика
def hod_nolika():
    print("Ходит нолик!")

    #nolik_h = str(input("Ваш ход по горизонтали:"))
    #nolik_v = str(input("Ваш ход по вертикали:"))
    nolik = str(input("Ваш ход в формате 'xx':"))

    # Словарь нолика с индексами для последующей замены в списке "pole"
    nolik_na_pole = {
        "a1": (3, "| 0 "),
        "b1": (4, "| 0 "),
        "c1": (5, "| 0 |"),
        "a2": (8, "| 0 "),
        "b2": (9, "| 0 "),
        "c2": (10, "| 0 |"),
        "a3": (13, "| 0 "),
        "b3": (14, "| 0 "),
        "c3": (15, "| 0 |")
    }
    # проверка хода
    if nolik in L and nolik in nolik_na_pole and nolik not in list_nolik + list_krestik:
        index, text = nolik_na_pole[nolik]
        pole.pop(index)
        pole.insert(index, text)
        pole_in_consol()
    elif nolik in list_nolik or nolik in list_krestik: # если место уже занято
        print(f"Это место уже занято: '{nolik}'")
        print("Извините, игра сломана, перезапустите игру.")
        exit()
    else: # если координаты введены неправильно
        print(f"Координаты '{nolik}' отсутствуют.")
        print("Перезапустите игру и ввердите верные координаты.")
        exit()
    list_nolik.append(nolik)

# словарь с содержанием выигрышных комбинаций на поле
list_winner = {1: ("a1", "a2", "a3"),
     2: ("b1", "b2", "b3"),
     3: ("c1", "c2", "c3"),
     4: ("a1", "b1", "c1"),
     5: ("a2", "b2", "c2"),
     6: ("a3", "b3", "c3"),
     7: ("a1", "b2", "c3"),
     8: ("a3", "b2", "c1"),
     }


# функция сравнивания победных комбинаций с ходами нолика
def winner_nolik():
    for key in list_winner:
        if all(item in list_nolik for item in list_winner[key]):
            print("Победил нолик!")
            return True
    return False


# функция сравнивания победных комбинаций с ходами крестика
def winner_krestik():
    for key in list_winner:
        if all(item in list_krestik for item in list_winner[key]):
            print("Победил крестик!")
            return True
    return False


# игру начинает нолик
def gamer_N():
    global count
    game_over = False
    while count < 9 and not game_over:
        count += 1
        hod_nolika()
        if len(list_nolik) >= 3 and winner_nolik():
            game_over = True
            break
        if count >= 9:
            print("Ничья!")
            break
        count += 1
        hod_krestik()
        if len(list_krestik) >= 3 and winner_krestik():
            game_over = True
            break
        if count >= 9:
            print("Ничья!")
            break

# игру начинает крестик
def gamer_K():
    global count
    game_over = False
    while count < 9 and not game_over:
        count += 1
        hod_krestik()
        if len(list_krestik) >= 3 and winner_krestik():
            game_over = True
            break
        if count >= 9:
            print("Ничья!")
            break
        count += 1
        hod_nolika()
        if len(list_nolik) >= 3 and winner_nolik():
            game_over = True
            break
        if count >= 9:
            print("Ничья!")
            break


# функция выбора игрока
gamer = str(input("Напишите 'N' для игры за нолика и 'K' за крестика:"))
if gamer == "N":
    gamer_N()
elif gamer == "K":
    gamer_K()
else:
    print("Такого игрока не существует.")
    print("Перезапустите игру и попробуйте снова.")