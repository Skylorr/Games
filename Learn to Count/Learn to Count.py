import random

lowDiapazon = 10
highDiapazon = 100
sign = 0
playGame = True
count = 0
right = 0
score = 0

print("""Компьютер составляет пример. Введите ответ.
Для завершения работы введите STOP""")
print("*" * 40)

while (playGame):
    print(f"Ваши очки: {score}")
    print(f"Обработано Задач: {count}")
    print(f"Правильных ответов: {right}")
    print("-" * 20)

    sign = random.randint(0, 3)

    if (sign == 0):
        z = random.randint(lowDiapazon, highDiapazon)
        x = random.randint(lowDiapazon, z)
        y = z - x
        if (random.randint(0, 1) == 0):
          print(f"{x} + {y} = ?")
        else:
          print(f"{y} + {x} = ?")

    elif (sign == 1):
        x = random.randint(lowDiapazon, highDiapazon)
        y = random.randint(0, x - lowDiapazon)
        z = x - y
        print(f"{x} - {y} = ?")

    elif (sign == 2):
        x = random.randint(1, (highDiapazon - lowDiapazon) //
                           random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) //x
        z = x * y
        print(f"{x} * {y} = ?")
    
    elif (sign == 3):
        x = random.randint(1, (highDiapazon - lowDiapazon) //
                           random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        if (y == 0):
            y = 1
        x = x * y
        z = x // y
        print(f"{x} / {y} = ?")

    user = ""
    while (not user.isdigit()
           and user.upper() != "STOP!"
           and user.upper() != "S"
           and user.upper() != "S"
           and user.upper() != "STOP"):
        user = input("Ваш ответ? ")

        if (user.upper() == "HELP"
                or user == "?"
                or user == ","
                or user.upper() == "HELP"):
            if (z > 9):
                print(f"Последняя цифра ответа: {z % 10}")
            else:
                print("Ответ состоит из одной цифры, подсказка не возможна.")
            score -= 10
        elif (user.upper() == "STOP"
                or user.upper() == "S"
                or user.upper() == "S"
                or user.upper() == "STOP"):
            playGame = False
        else:
            count += 1
            if (int(user) == z):
                print("\nПрвыильно!\n")
                right += 1
                score += 10
            else:
                print(f"\nОтвет неправельный... Правильно: {z}")
                print(f"Выможите ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)\n")
                score -= 20

print("*" * 45);
print("СТАТИСТИКА ИГРЫ:")
print(f"Всего примеров: {count}")
print(f"Правильных ответов: {right}")
print(f"Неправильных ответов {count - right}")
if (count > 0):
    print(f"Процент верных ответов: {int(right / count * 100)}%")
else:
    print("Процент верных ответов: 0%")
print("Возвращайтесь!")




