"""
Oppgave 1: Regnefunksjoner
"""

def addisjon(para1,para2):  # Definerer funksjon, som tar inn to argumenter.
    return para1+para2  # returnerer dem addert 
# Printer en passende streng som kaller på funksjonen.
print("1 og 1 som argumenter i addisjon() returnerer {}".format(addisjon(1,1)))

def subtraksjon(para1,para2):  # Definerer funksjon, som tar inn to argumenter.
    return para1-para2  # Returner den første subtrahert fra den andre.

def divisjon(para1,para2):  # Definerer funksjon, som tar inn to argumenter.
    return para1/para2  # Returnerer den første dividert med den andre. 

assert addisjon(1,1) == 2  # Ber programme teste om betingelsen er sann, hvis ikke skriv feilmelding
assert addisjon(-1,-1) == -2  # samme...
assert addisjon(1,-1) == 0
assert subtraksjon(1,1) == 0
assert subtraksjon(-1,-1) == 0
assert subtraksjon(1,-1) == 2
assert divisjon(1,1) == 1
assert divisjon(-1,-1) == 1
assert divisjon(1,-1) == -1  # ...samme

def tommerTilCm(antallTommer): # Definerer en funksjon tar inn et tall som argument.
    assert antallTommer > 0  # Sjekk om argumentet er større enn 0.
    return antallTommer*2.54  # returner tallet konvertert.

print(tommerTilCm(10))  # Tester funksjonen over og printer ut returverdien

def skrivBeregninger():  # Definer en funksjon uten parametere.
    a = float(input("Skriv inn tall1: "))  # Ber bruker skrive inn et tall
    b = float(input("Skriv inn tall2: "))

    print("Resultat av summering: ", addisjon(a,b))  # Skriver ut en streng, kaller på addisjon()
    print("Resultat av subtraksjon: ", subtraksjon(a,b))  # tilsvarende
    print("Resultat av divisjon: ", divisjon(a,b))  # tilsvarende

    print("Konverter fra tommer til cm: ")
    # Kaller på tommerTilCm() og skriver ut en passende streng
    print("Resultat: {} cm".format(tommerTilCm(float(input("Skriv inn et tall: ")))))

skrivBeregninger()  # Kaller på funksjonen over.

"""
Kjøreeksempel:
1 og 1 som argumenter i addisjon() returnerer 225.4
Skriv inn tall1: 3
Skriv inn tall2: 5
Resultat av summering:  8.0
Resultat av subtraksjon:  -2.0
Resultat av divisjon:  0.6
Konverter fra tommer til cm:
Skriv inn et tall: 5
Resultat: 12.7 cm
"""