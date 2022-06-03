from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

def setupHours():
    global state01, state02, state03, state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fastSpeed01, fastSpeed01, fastSpeed01, fastSpeed04

    weather = randint(1, 5)
    timeDay = randint(1, 5)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) // 100
    winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) // 100
    winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) // 100
    winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) // 100

    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fastSpeed01 = False
    fastSpeed02 = False
    fastSpeed03 = False
    fastSpeed04 = False

def winRound(hours):
    global x01, x02, x03, x04, money

    res = "К финишу пришла лошадь"
    if (hours == 1):
        res += nameHorse01
        win = summ01.get() * winCoeff01
    elif (hours == 2):
        res += nameHorse02
        win = summ02.get() * winCoeff02
    elif (hours == 3):
        res += nameHorse03
        win = summ03.get() * winCoeff03
    elif (hours == 4):
        res += nameHorse04
        win = summ04.get() * winCoeff04

    if (hours > 0):
        res += f"! Вы выиграли {int(win)} {valuta}. "
        if (win > 0):
            res += "Поздравляем! Средства уже зачислены на Ваш счет!"
            insertText(f"Этот забег пренёс вам {int(win)} {valuta}.")
        else:
            res += "К сожелению, Ваша лошадь была неправильной. Попробуйте ещё раз!"
            insertText("Делайте ставку! Увеличевайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    else:
        messagebox.showinfo("Всё плохо", "До финиша не дошёл никто. Забег признан несостоявшимся. Все ставки возвращены.")
        insertText("Забег признан несостоявшимся.")
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(Money))
    
    setupHours()
    startButton["state"] = "normal"
    stavka01["state"] = "readonly"
    stavka02["state"] = "readonly"
    stavka03["state"] = "readonly"
    stavka04["state"] = "readonly"
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsPlaceWindow()

    refreshCombo(eventObject="")
    vieWeather()
    healthHorse()
    insertText(f"Ваши средства: {int(money)} {valuta}.")

    if (money < 1):
        messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
        quit(0)

def problemHorse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global state01, state02, state03, state04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    horse = randint(1, 4)

    maxRand = 10000

    if (horse == 1 and play01 == True and x01 > 0):
        if (randint(0, maxRand) < state01 * 5):
            reverse01 = not reverse01
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse01} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state01 * 5):
            play01 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse01} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state01 * 5 and not fastSpeed01):
            messagebox.showinfo("Великолепно!", f"{nameHorse01} перестала притворяться и ускорилась!")
            fastSpeed01 = True

    elif (horse == 2 and play02 == True and x02 > 0):
        if (randint(0, maxRand) < state02 * 5):
            reverse02 = not reverse02
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse02} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state02 * 5):
            play02 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse02} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state02 * 5 and not fastSpeed02):
            messagebox.showinfo("Великолепно!", f"{nameHorse02} перестала притворяться и ускорилась!")
            fastSpeed02 = True

    elif (horse == 3 and play03 == True and x03 > 0):
        if (randint(0, maxRand) < state03 * 5):
            reverse03 = not reverse03
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse03} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state03 * 5):
            play03 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse03} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state03 * 5 and not fastSpeed03):
            messagebox.showinfo("Великолепно!", f"{nameHorse03} перестала притворяться и ускорилась!")
            fastSpeed03 = True

    elif (horse == 1 and play04 == True and x04 > 0):
        if (randint(0, maxRand) < state04 * 5):
            reverse04 = not reverse04
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse04} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state04 * 5):
            play04 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse04} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state04 * 5 and not fastSpeed04):
            messagebox.showinfo("Великолепно!", f"{nameHorse04} перестала притворяться и ускорилась!")
            fastSpeed04 = True

def getHealth(name, state, win):
    s = f"Лошадь {name} "
    if (state == 5):
        s += "Мучается несварением желудка."
    elif (state == 4):
        s += "плохо спала. Подёргивается веко."
    elif (state == 3):
        s += "сурова и беспощадна."
    elif (state == 2):
        s += "в отличном настроении, покушала хорошо."
    elif (state == 1):
        s += "Просто ракета!"

    s += f" ({win}:1)"
    return s

def healthHorse():
    insertText(getHealth(nameHorse01, state01, winCoeff01))
    insertText(getHealth(nameHorse02, state02, winCoeff02))
    insertText(getHealth(nameHorse03, state03, winCoeff03))
    insertText(getHealth(nameHorse04, state04, winCoeff04))

def vieWeather():
    s = "Сейчас на ипподроме "
    if (timeDay == 1):
        s += "ночь, "
    elif (timeDay == 2):
        s += "утро, "
    elif (timeDay == 3):
        s += "день, "
    elif (timeDay == 4):
        s += "вечер, "

    if (weather == 1):
        s += "льёт сильный дождь."
    elif (weather == 2):
        s += "моросит дождик."
    elif (weather == 3):
        s += "облачно, на горизонте."
    elif (weather == 4):
        s += "безоблочно, ветер."
    elif (weather == 5):
        s += "безоблочно, прекрасная погода!"
    insertText(s)

def moveHorse():
    global x01, x02, x03, x04

    if (randint(0, 100) < 20):
        problemHorse()

    speed01 = (randint(l, timeDay + weather) + randint(l, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(l, timeDay + weather) + randint(l, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(l, timeDay + weather) + randint(l, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(l, timeDay + weather) + randint(l, int((7 - state04)) * 3)) / randint(10, 175)

    multiple = 3
    speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

    if (play01):
        if (not reverse01):
            x01 += speed01
        else:
            x01 -= speed01
    if (play02):
        if (not reverse02):
            x02 += speed02
        else:
            x02 -= speed02
    if (play03):
        if (not reverse03):
            x03 += speed03
        else:
            x03 -= speed03
    if (play04):
        if (not reverse04):
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceInWinwow()

    allPLay = play01 or play02 or play03 or play04
    allx = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    allReverse = reverse01 and reverse02 and reverse03 and reverse04

    if (not allPlay or allx or allReverse):
        winRound(0)
        return 0

    if (x01 < 952 and
        x02 < 952 and
        x03 < 952 and
        x04 < 952):
        root.after(5, moveHorse)
    else:
        if (x01 >= 952):
            winRound(1)
        elif (x02 >= 952):
            winRound(2)
        elif (x03 >= 952):
            winRound(3)
        elif (x04 >= 952):
            winRound(4)

def runHorse():
    global money
    startButton["state"] = "disabled"
    stavka01["state"] = "disabled"
    stavka01["state"] = "disabled"
    stavka01["state"] = "disabled"
    stavka01["state"] = "disabled"
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()

def refreshCombo(eventObject):
    summ = summ01.get() + summ2.get() + summ03.get() + summ04.get()
    labeAllMoney["text"] = f"У вас на счету: {int(money - summ)} {valuta}."

    stavka01["values"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02["values"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03["values"] = getValues(int(money - summ01.get() - summ02.get() - summ04.get()))
    stavka04["values"] = getValues(int(money - summ01.get() - summ02.get() - summ03.get()))

    if (summ > 0):
        startButton["state"] = "normal"
    else:
        startButton["state"] = "disabled"

    if (summ01.get() > 0):
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if (summ02.get() > 0):
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if (summ03.get() > 0):
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if (summ04.get() > 0):
        horse04Game.set(True)
    else:
        horse04Game.set(False)

def getValues(summa):
    value = []
    if (summa > 9):
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if (summa > 0):
            value.append(summa)
    return value

def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файл не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наш Ипподром закрывается!")
        quit(0)

def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)

def horsPlaceWindow():
    hours01.place(x=int(x01), y=20)
    hours02.place(x=int(x01), y=100)
    hours03.place(x=int(x01), y=180)
    hours04.place(x=int(x01), y=260)

root = Tk()

WIDTH = 1024
HEIGHT = 600

x01 = 20
x02 = 20
x03 = 20
x04 = 20

nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Прожорливый"
nameHorse04 = "Копытце"

reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False
play01 = True
play02 = True
play03 = True
play04 = True
fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False

defaultMoney = 10000
money = 0
valuta = "руб"
weather = randint(1, 5)
timeDay = randint(1, 5)

state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.title("ИППОДРОМ")

root.resizable(False, False)

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

road_image = PhotoImage(file="road.png")
road = Label(root, image=road_image)
road.place(x=0, y=17)

horse01_image = PhotoImage(file="horse01.png")
horse01 = Label(root, image=horse01_image)

horse02_image = PhotoImage(file="horse02.png")
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file="horse03.png")
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file="horse04.png")
horse04 = Label(root, image=horse04_image)

horsPlaceWindow()

startButton = Button(text="СТАРТ", font="arial 20", widht=61, background="#37AA37")
startButton.place(x=20, y=370)
startButton["state"] = "disabled"

textDiary = Text(width=70, height=8, warp=WORD)
textDiary.place(x=430, y=450)

scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set

money = loadMoney()

if (money <= 0):
    messagebox.showinfo("Стоп!", "На ИППОДРОМ без средств заходить нельзя!")
    quit(0)

labelAllMoney = Lable(text=f"Осталось средств: {money} {valuta}.", font="Arial 12")
labelAllMoney.place(x=20, y=565)

labelHorse01 = Lable(text="Ставка на лошадь №1")
labelHorse01.place(x=20, y=450)

labelHorse01 = Lable(text="Ставка на лошадь №2")
labelHorse01.place(x=20, y=480)

labelHorse01 = Lable(text="Ставка на лошадь №3")
labelHorse01.place(x=20, y=510)

labelHorse01 = Lable(text="Ставка на лошадь №4")
labelHorse01.place(x=20, y=540)

horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

horseCheck01["state"] = "disabled"
horseCheck02["state"] = "disabled"
horseCheck03["state"] = "disabled"
horseCheck04["state"] = "disabled"

stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

stavka01["state"] = "readonly"
state01.place(x=280, y=450)

stavka01["state"] = "readonly"
state01.place(x=280, y=480)

stavka01["state"] = "readonly"
state01.place(x=280, y=510)

stavka01["state"] = "readonly"
state01.place(x=280, y=540)

summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

refreshCombo("")
stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

startButton["command"] = runHorse

vieWeather()
healthHorse()

root.mainloop()
