"""
Oppgave 1: Lister
Mohammed Shartaz Mostafa
"""

list1 = [4,5,2]  # Lager liste med tre selvvalgte tall
list1.append(10)  # Legger til tallet 10 bakerst i lista
print(list1[0],list1[2])  # Printer ut element med indeks 0, som er første element.
# Og element med index 2, som er tredje element.

new_list = [input("Skriv inn et navn {} gang(er) til: ".format(4-i))\
for i in range(4)]  # Bruker list comprehension og input for å inn navnene fra bruker
if "Mohammed" in new_list:  # Hvis "Mohammed" finnes i listen...
    print("Du husket meg!")
else:
    print("Glemte du meg?")

merged = list1 + new_list  # Konkatenerer listene til en samlet liste
print(merged)  # print listen
del merged[-2:]  # Sletter nestsiste element og siste element ved hjelp av slicing
print(merged)
"""
Kjøreeksempel
4 2
Skriv inn et navn 4 gang(er) til: 1
Skriv inn et navn 3 gang(er) til: 2
Skriv inn et navn 2 gang(er) til: 3
Skriv inn et navn 1 gang(er) til: 4
Glemte du meg?
[4, 5, 2, 10, '1', '2', '3', '4']
[4, 5, 2, 10, '1', '2']
"""


