"""
Oppgave 6: Egen oppgave
Løkker og lister; bruk dem til å skrive et program som lar bruker registrere
venners bursdager og lagrer informasjonen. Brukeren skal kunne skrive et navn i terminalen
og få tilbakemelding på når vennen har brusdag. Hvis personen ikke er registrert, så skal
programmet gi beskjed om det.
"""
# Bruker list comprehension til å lage en liste med navn etter å ha spurt om hvor mange
# som skal registreres. Bruker så det tallet til å bestemme hvor mange ganger 
# løkka skal kjøres.
navn = [input("Skriv inn navnet til venn nr {}: ".format(i+1))\
for i in range(int(input("Skriv inn antall venner du vil registrere:\n")))]

# Bruker igjen list comprehension til å registrere bursdagsdatoer. I form av string
# for brukerens frihet.
burs = [input("Når har {} bursdag? \n".format(navn[i] ))for i in range(len(navn))]

# Spør om hvem sin bursdag som skal printes til konsollen.
person = input("Hvem sin bursdag vil du ha skrevet ut? \n")

# If test for å sjekke om navnet finnes i lista. 
if person in navn:
    bursdag = burs[navn.index(person)]
    print("{} har bursdag {}".format(person, bursdag))  # Printer navn og bursdag
else:
    print("Denne personen finnes ikke i registeret.")  # feilmelding