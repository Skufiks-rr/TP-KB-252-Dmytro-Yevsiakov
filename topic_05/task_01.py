import random

choices = ["stone", "scissor", "paper"]

player = input("Введіть stone, scissor або paper: ")

if player not in choices:
    print("Помилка: неправильний вибір")
else:
    computer = random.choice(choices)

    print("Ваш вибір:", player)
    print("Вибір комп'ютера:", computer)

    if player == computer:
        print("Нічия!")
    elif (
        (player == "stone" and computer == "scissor") or
        (player == "scissor" and computer == "paper") or
        (player == "paper" and computer == "stone")
    ):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")
        