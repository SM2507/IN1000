"""
Oppgave 4: Repitisjon
"""

mineOrd = []  # Tom liste

def slaaSammen(streng1,streng2):  # Funksjon med to parametere, argumentene skal være to strenger
    return streng1+streng2  # Returner strengene konkatenert.

def skrivUt(liste):  # Funksjon som tar i mot en liste
    for i in liste:  # Skriver ut hvert element i lista.
        print(i)

while True:  # While-løkka, som kjører 'hele tiden'
    inp = input('Skriv "i", "u", eller "s": ')  # tar i mot brukerinput
    if inp == "i":  # Hvis bruker skriver inn i...
        streng_1 = input("Skriv et ord eller setning (1):\n")  # ta i mot en streng fra bruker
        streng_2 = input("Skriv et ord eller setning (2):\n")  # samme...
        mineOrd.append(slaaSammen(streng_1,streng_2))  # Legg til returnverdien fra slaaSammen()
    elif inp == "u":   # Hvis bruker skriver inn u...
        skrivUt(mineOrd)  # Skriv ut det som finnes i lista "mineOrd"
    elif inp == "s":  # Hvis bruker skriver inn s...
        break  # Stopp løkka.