#ukol 9
def vyhodnot(pole):
    "vyhodnoti retezec s hernim polem: vyhra, remiza, ani jedno"
    if "xxx" in pole:
        print("x")
    elif "ooo" in pole:
        print("o")
    elif "-" not in pole:
        print("!")
    else:
        print("-")
n = 20
pole = n * "-"
vyhodnot(pole)


#ukol 10
def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    print(pole[:cislo_policka] + symbol + pole[cislo_policka + 1:])

n = 20
pole = n * '-'
symbol = '-'
cislo_policka = 12
tah(pole, cislo_policka, symbol)

#ukol 11
def tah_hrace(pole):
    "Vrátí herní pole se zaznamenaným tahem hráče"
    while True:
        znak = input("Zadej číslo políčka mezi 0-19: ")
        try:
            cislo_policka = int(znak)
        except ValueError:
            print("Zadej cele cislo!")
        else:
            if cislo_policka < 0 or cislo_policka > 19:
               print('Vole, musíš zadat číslo v rozmezí 0-19!')
            elif pole[cislo_policka] != '-':
               print('Políčko {} je obsazené, vyber jiné.'.format(cislo_policka))
            else:
               return tah(pole, cislo_policka, "x")
            break
n = 20
pole = n * '-'
symbol = 'x'
tah_hrace(pole)

#ukol 12
def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        cislo_policka = randrange(len(pole))
        if pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, "o")

from random import randrange

tah_pocitace(pole)

#ukol 13
#ukol 14

