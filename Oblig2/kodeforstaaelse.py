"""
Oppgave 4: Kodeforstaaelse og feilsoking
"""
# 1)
"""
Dette er ikke en lovlig kode, fordi man ikke kan "addere" string med en integer.
En string kan bli sett paa som en liste med bokstaver, som med + tegnet blir 
konkatenert med et heltall. Dette er ikke mulig.
Det vil bli type error, dersom tallet som blir tastet inn 
er mindre enn 10.
"""
# 2)
"""
Man vil møte på type error når man kjører programmet, hvis input < 10.
Ellers vil den kjøre fint.
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

a = input("Tast inn et heltall!  ")
b = int(a)
if b < 10:
    print(b + ("Hei!"))