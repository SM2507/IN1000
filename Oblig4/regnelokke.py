"""
Oppgave 2: Regning med løkker
"""
#1)

liste = []  # Lager en tom liste
while True:  # Så lenge betingelsen er sann, kjør følgende:
    inp = float(input("Skriv inn et tall: "))  # Ber bruker taste inn et tall.
    if inp == 0:  # Hvis bruker har tastet 0, bryt løkka
        break
    liste.append(inp)  # Legger til tallet bakerst i lista


for i in liste:  # Printer hvert element, i, i lista.
    print(i)

minsum = 0  # Definerer en minsum variabel utenfor løkka
for i in liste:  # Tar hvert element i lista og summerer den med summen av de forrige
    minsum += i

print("Summer av alle elementer i liste er {}".format(minsum))  # Printer summen

a = liste[0]
for i in range(len(liste)-1):  # Sjekker om det neste elementet i lista er større enn det forrige
    if a < liste[i+1]:
        mini = a  # Hvis sann, er mini = forrige element
    elif a >= liste[i+1]:
        mini = liste[i+1]  # Hvis ikke, er mini = neste element
        a = liste[i+1]  # Lagrer a som det minste elementet hittil

print("Minimum i lista er {}".format(mini))  # Printer minimum

a = liste[0]
for i in range(len(liste)-1):  # Sjekker om det neste elementet i lista er større enn det forrige
    if a > liste[i+1]:  # Hvis a er større enn neste element, maxi = a
        maxi = a
    elif a <= liste[i+1]:  # Hvis ikke, er maxi = neste element
        maxi = liste[i+1]
        a = liste[i+1]  # Lagrer a som det største elementet hittil

print("Maksimum i lista er {}".format(maxi))  # Printer maximum

"""
Kjøreeksempel:
Skriv inn et tall: 20
Skriv inn et tall: 45
Skriv inn et tall: 11
Skriv inn et tall: 9
Skriv inn et tall: 0
20.045.0
11.0
9.0
Summer av alle elementer i liste er 85.0
Minimum i lista er 9.0
Maksimum i lista er 45.0
"""