"""
Oppgave 4: Reiseplan
"""
# Lager tomme lister
steder = []; klesplagg = []; avreisedatoer = []

for i in range(5):  # Ber bruker skrive inn input og legger elementet sist i lista.
    steder.append(input("Skriv inn reisemål: "))
    
for i in range(5):    
    klesplagg.append(input("Skriv inn klesplagg: "))

for i in range(5):
    avreisedatoer.append(input("Skriv inn avreisedato: "))

reiseplan = [steder, klesplagg, avreisedatoer]  # Lager en nested list med gjeldende lister

for i in reiseplan:  # Printer ut elementene i nested list
    print(i)

# Ber bruker skrive inn verdier på indekser
i1 = int(input("Skriv inn verdien på index (tall mellom 0 og 2): "))  

i2 = int(input("Skriv inn verdien på index (tall mellom 0 og 4): "))

# Lager betingelsen
condition = 0<=i1<=2 and 0<=i2<=4

if condition is True:  # Hvis betingelsen er sann
    print(reiseplan[i1][i2])  # Skriv ut listeelement
elif condition is False:  # Hvis usann
    print("Ugyldig input")  # Skriv melding

"""
Kjøreeksempel:
Skriv inn reisemål: Drammen
Skriv inn reisemål: Berlin
Skriv inn reisemål: New York City
Skriv inn reisemål: Jakarta
Skriv inn reisemål: Cape Town
Skriv inn klesplagg: Jakke
Skriv inn klesplagg: Genser
Skriv inn klesplagg: T-skjorte
Skriv inn klesplagg: Singlet
Skriv inn klesplagg: Badeshorts
Skriv inn avreisedato: 0112
Skriv inn avreisedato: 0402
Skriv inn avreisedato: 1705
Skriv inn avreisedato: 2507
Skriv inn avreisedato: 1111
['Drammen', 'Berlin', 'New York City', 'Jakarta', 'Cape Town']
['Jakke', 'Genser', 'T-skjorte', 'Singlet', 'Badeshorts']
['0112', '0402', '1705', '2507', '1111']
Skriv inn verdien på index (tall mellom 0 og 2): 1
Skriv inn verdien på index (tall mellom 0 og 4): 2
T-skjorte
"""