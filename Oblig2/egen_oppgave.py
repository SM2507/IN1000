"""
Oppgave 5: Egen Oppgave
Skriv et program til en quiz med så mange spørsmål som du vil, med en 
vanskelighetsgrad som du selv ønsker. Sørg for at koden gir tilbakemelding 
ved riktig og gale svar, og printer du poengsummen på slutten av quizzen. 
"""

print("Velkommen til quiz programmet! Du har ikke noe valg, deltakelse er obligatorisk.\n\
Svar enten a, b, c eller d \
ved å taste inn korrespoderende bokstav. \n\
Tar du feil er får du ikke poeng. Hvert spørsmål er verdt 1 poeng.\
\n")

input("Trykk enter for å gå videre\n")
score = 0
One = input("Hva er hovedstaden i Norge?\n\
a. Oslo\n\
b. Danmark\n\
c. Mars \n\
d. Uranus\n\
Ditt svar: ")
if One == "a":
    print("Det er KORREKT\n")
    score += 1
else:
    print("Galt\n")

Two = input("På hvilken dag fant 9/11 sted?\n\
a. 9. november 2001\n\
b. 25. desember 1001\n\
c. 11. september 2001\n\
d. 29. februar 2019\n\
Ditt svar: ")
if Two == "c":
    print("Helt riktig\n")
    score += 1
else: 
    print("Hvordan tok du feil der? Svaret er i spørsmålet.\n")

Three = input("Hvor mange måneder i året har 28 dager?\n\
a. 12\n\
b. 11\n\
c. 1/4\n\
d. 1\n\
Ditt svar:  ")
if Three == "a":
    print("Riktig!\n")
    score += 1
    if score == 3:
        print("Du er et geni")
else: 
    print("Galt")

print("{}/3 mulige poeng".format(score))


