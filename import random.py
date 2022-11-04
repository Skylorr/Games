import random

highDiapazon = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
playGame = True
count = 0
right = 0
score = 0

print("""Компьютер составляет пример. Введите ответ.""")
print("*" * 40)

while (playGame):
    print(f"Ваши очки: {score}")
    print(f"Обработано Задач: {count}")
    print(f"Правильных ответов: {right}")
    print("-" * 20)
    
    x = random.choice(highDiapazon)
    y = int(input(f"Корень из {x}? " )) #x вопрос
    z = int(x ** 0.5)
    
    if y == z:
        print("\nПравильно!\n")
        right += 1
        score += 10
    else:
        print("\nНеправильно!\n")