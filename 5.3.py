from random import randrange

rocks = randrange(4, 31)
while rocks > 0:
    print(f"В куче {rocks} камней. Возьмите 1, 2 либо 3 камня")
    try:
        your_pick = int(input())
    except ValueError:
        print("Вы ввели неверное число камней. Введите число 1, 2 либо 3")
        exit()

    while rocks - your_pick < 1:
        print("Кол-во камней в куче не может быть меньше 1")
        your_pick = int(input())
        continue

    while your_pick > 3 or your_pick < 1:
        print("Можно брать только 1, 2 либо 3 камня!")
        try:
            your_pick = int(input())
        except ValueError:
            print("Вы ввели неверное число камней. Введите число 1, 2 либо 3")
            exit()
        continue
    rocks -= your_pick

    if rocks == 1:
        print("Поздравляю, вы выиграли!")
        break

    computer_pick = randrange(1, 4)
    while rocks - computer_pick < 1:
        computer_pick = randrange(1, 4)
    rocks -= computer_pick
    print(f"Компьютер взял {computer_pick} камней")

    if rocks == 1:
        print("Выиграл компьютер")
        break

