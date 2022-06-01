# КАЗИНО 678

from ctypes import *
import time
import random

valuta = "руб."
money = 0
startMoney = 0
playGame = True
defaultMoney = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


def pobeda(result):
    color(14)
    print(f"    Попеда за тобой! Выигрыш составил: {result} {valuta}")
    print(f"    У тебя на счету: {money}")

def proigr(result):
    color(12)
    print(f"     К сожеленю, проигрыш: {result} {valuta}")
    print(f"     у тебя на счету: {money}")
    print(f"    Обязательно нужно отыграеться!")

def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if (digit == v1):
        ret += 1
    if (digit == v2):
        ret += 1
    if (digit == v3):
        ret += 1
    if (digit == v4):
        ret += 1
    if (digit == v5):
        ret += 1
    return ret
def getOHBRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = true
    getD2 = true
    getD3 = true
    getD4 = true
    getD5 = true
    col = 10

    while (getD1
           or getD2           
           or getD3
           or getD4
           or getD5):


        if (getD1):
            d1 += 1
        if (getD2):
            d2 += 1
        if (getD3):
            d3 += 1
        if (getD4):
            d4 += 1
        if (getD5):
            d5 += 1

        if (d1 > 9):
            d1 = 0
        if (d2 < 0):
            d2 = 9
        if (d3 > 9):
            d3 = 0
        if (d4 < 0):
            d4 = 9
        if (d5 > 9):
            d5 = 0
            
        if (random.randit(0, 20) == 1):
            getD1 = False
        if (random.randit(0, 20) == 1):
            getD2 = False
        if (random.randit(0, 20) == 1):
            getD3 = False
        if (random.randit(0, 20) == 1):
            getD4 = False
        if (random.randit(0, 20) == 1):
            getD5 = False

        time.sleep(0.1)
        color(col)
        col += 1
        if (col > 15):
            col = 10
        
        print("    " + "%" * 10)
        print(f"     {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if (maxCount < getMaxCount(d2, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if (maxCount == 2):
        print(f" Совпадение двух чисел! Твой выигрыш в размере: {res}")
    elif (maxCount == 3):
        res *= 2
        print(f" Совпдение трёх чисел! Твой выигрыш 2:1: {res}")
    elif (maxCount == 4):
        res *= 5
        print(f" Совпадение ЧЕТЫРЁХ чисел! Твой выигрыш 5:1: {res}")
    elif (maxCount == 5):
        res *= 10
        print(f" БИНГО! Совпадение всех чисел! Твой выигрыш 10:1: {res}")
    else:
        proigr(res)
        res = 0

    color(11)
    print()
    input(" Нажмите Enter для продолжения...")
    
    return res

# Однорукий бандит
def oneHandBandit():
    global money
    playGame = True
    while (playGame):
        colorLine(3, "ДОБРО ПОЖАЛИТВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(5)
        print(" Правила игры: ")
        print("    1. При совпадении 2-х чисел ставка не списывается")
        print("    2. При совпадении 2-х чисел выигрыш 2:1.")
        print("    3. При совпадении 3-х чисел выигрыш 5:1.")
        print("    4. При совпадении 4-х чисел выигрыш 10:1.")
        print("    0. Ставка 0 для завершения игры\n")

        stavka = getIntInput(0, money, f"    Введи ставку от 0 до {money}: ")
        if (stavka == 0):
            return 0

        money -= stavka
        money += getOHBRes(stavka)

        if (money <= 0):
            playGame = False


# Анимация костей
def getDice():
    count = random.randint(3, 8)
    sleep = 0
    while (count > 0):
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y

#Кости
def dice():
    global money
    playGame = True

    while(playGame):

        print()
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")

        color(7)
        stavka = getIntInput(0, money, f"   Сделай ставку в пределах {money} {valuta}: ")
        if (stavka == 0):
            return 0

        playRound = True
        control = stavka
        oldResulte = getDice()
        firstPlay = True

        while (playRound and stavka > 0 and money > 0):

            if (stavka > money):
                stavka = money

            color(11)
            print(f"\n    В твоём распоряжении {stavka} {valuta}")
            color(12)
            print(f"\n    Текущая сумма чисел на костях: {oldResulte}")
            color(11)
            print("\n    Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
            color(7)
            x = getInput("0123", "    Введи 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ")

            if (x != "0"):
                firstPlay = False
                if (stavka > money):
                    stavka = money

                money -= stavka
                diceResult = getDice()

                # Краткая версия
                win = (oldResulte > diceResult and x == "2") or (oldResulte < diceResult and x == "1")

                if (not x == "3"):
                    if (win):
                        money += stavka + stavka // 5
                        pobeda(stavka // 5)
                        stavka += stavka // 5
                    else:
                        stavka = control
                        proigr(stavka)
                elif (x == "3"):
                    if (oldResulte == diceResult):
                        money += stavka * 3
                        pobeda(stavka * 2)
                        stavka *= 3
                    else:
                        stavka = control
                        proigr(stavka)

                oldResulte = diceResult
            else:
                if (firstPlay):
                    money -= stavka
                    playRound = False

def getRoulette(visible):
    tickTime = random.randint(100, 200) / 10000
    mainTime = 0
    number = random.randint(0, 38)
    increaseTickTime = random.randit(100, 110) / 100
    col = 1

    while (mainTime < 0.7):
        col += 1
        if (col > 15):
            col = 1

        mainTime += tickTime
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if (number > 38):
            number = 0
            print()

        printNumber = number
        if (number == 37):
            printNumber = "00"
        elif (number == 38):
            printNumber = "000"

        print(" Чисел> ",
              printNumber,
              "*" * number,
              " " * (79 - number * 2),
              "*" * number)

        if (visible):
            time.sleep(mainTime)
    
    return number

def roulette():
    global money

    playGame = True

    while (playGame and money > 0):
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(14)
        print(" Ставлю на...")
        print("    1. Чётное (выигрыш 1:1)")
        print("    2. Нечётное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")

        x = getInput("01234","     Твой выбор? ")

        playRoulette = True

        if (x == "3"):
            color(2)
            print()
            print(" Выбери числа:...")
            print("    1. ОТ 1 До 12")
            print("    2. ОТ 13 До 24")
            print("    3. ОТ 25 До 36")
            print("    0. Назад")

            duzhina = getInput("0123",    "Твой выбор? ")

            if (duzhina == "1"):
                textDuzhina = "от 1 до 12"
            elif (duzhina == "2"):
                textDuzhina = "от 13 до 24"
            elif (duzhina == "3"):
                textDuzhina = "от 25 до 36"
            elif (duzhina == "0"):
                playRoulette = False
        elif (x == "4"):
            chislo = getIntInput(0, 36, "    На какое число Ставишь? (0..36): ")
            
        color(7)
        if (x == "0"):
            return 0

        if (playRoulette):
            stavka = getIntInput(0, money, f"    Сколько поставишь? (не больше {money}): ")
            if (stavka == 0):
                return 0

            number = getRoulette(True)

            print()
            color(11)

            if (number < 37):
                print(f"    Выполо число {number}! " + "*" * number)
            else:
                if (number == 37):
                    printNumber = "00"
                elif (number == 38):
                    printNumber = "000"
                print(f"    Выполо число {printNumber}! ")

            if (x == "1"):
                print("    Ты ставил на ЧЁТНОЕ!")
                if (number < 37 and number % 2 == 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            elif (x == "2"):
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if (number < 37 and number % 2 != 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            elif (x == "3"):
                print(f"     Ставка сделана на диапазон чисел {textDuzhina}.")
                winDuzhina = ""
                if (number > 0 and number < 13):
                    winDuzhina = "1"
                elif (number > 12 and number < 25):
                    winDuzhina = "2"
                elif (number > 24 and number < 37):
                    winDuzhina = "3"

                if (duzhina == winDuzhina):
                    money += stavka * 2
                    pobeda(stavka * 3)
                else:
                    money -= stavka
                    proigr(stavka)
            elif (x == "4"):
                print(f"    Ставка сделана на число {chislo}")
                if (number == chislo):
                    money += stavka * 35
                    pobeda(stavka * 36)
                else:
                    money -= stavka
                    proigr(stavka)

            print()
            input(" Нажми Enter для продолжения...")

def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания фийла, Наше Казино закрывается!")
        quit(0)

def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)

def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))

def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while (ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print("    Ваеди целое чесло!")
    return ret

def getInput(digit, message):
    color(7)
    ret = ""
    while (ret =="" or not ret in digit):
        ret = input(message)
    return ret

def main():
    global money, playGame

    money = loadMoney()
    startMoney = money


    while (playGame and money > 0):
        colorLine(10, "Привествую тебя в нашем казино, дружище!")
        color(14)
        print(f" У тебя на счету {money} {valuta}")

        color(6)
        print(" Ты можешь сыграть в:")
        print("    1. Рулетку")
        print("    2. Кости")
        print("    3. Однорукий бандит")
        print("    0. Выход. Ставка 0 в играх - выход.")
        color(7)

        x =  getInput("0123", "   Твой выбор? ")
        
        if (x == "0"):
            print("123123123123")
            playGame = False
        elif (x == "1"):
            roulette()
        elif (x == "2"):
            dice()
        elif (x == "3"):
            oneHandBandit()
        
    colorLine(12, "Жаль что ты покидаешь нас! Но возвращайся скорей!")
    color(13)
    if (money <= 0):
        print(" Упс, ты остался без денег. Возьми микрокредит и возвращайся!")

    color(11)
    if (money > startMoney):
        print("Ну что ж, поздравляем с прибылью!")
        print(f"На начало игры у тебя было {startMoney} {valuta}")
        print(f"Сейчас уже {money} {valuta}! Играй ещё и приумножай!")
    else:
        print(f"К сожеленью, ты проиграл {startMoney - money} {valuta}")
        print("В следующий раз всё обязательно получться!")

    saveMoney(money)

    color(7)
    quit(0)

main()