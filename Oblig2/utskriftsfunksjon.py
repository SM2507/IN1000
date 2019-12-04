"""
Oppgave 1: Utskriftsprosedyre
"""

#1)
"""
print("Hei, {}!. Du er fra {}.".format(input("Skriv inn navn: "), \
input("Hvor kommer du fra? ")))


Kjøreeksempel
Skriv inn navn: Mohammed
Hvor kommer du fra? Drammen
Hei, Mohammed!. Du er fra Drammen.
"""
#2)

def fittefunksjon():
    navn = input("Skriv inn navn: ")
    sted = input("Hvor kommer du fra? ")
    print("Hei, {}!. Du er fra {}.\n".format(navn, sted))
# Bruker string formatering for å holde koden kort, og printe resultatene direkte.
# Input-funksjonen er også i formatteringen for å slippe å lage en variabel som må "huskes".

# Bruker en for løkke for å slippe å skrive samme kode flere ganger (D.R.Y)

for i in range(3):
    fittefunksjon()

"""
Kjøreeksempel
Skriv inn navn: Espen Askeladd
Hvor kommer du fra? Oslo
Hei, Espen Askeladd!. Du er fra Oslo.

Skriv inn navn: Donald Duck
Hvor kommer du fra? Andeby
Hei, Donald Duck!. Du er fra Andeby.

Skriv inn navn: Minni Mus
Hvor kommer du fra? Museby
Hei, Minni Mus!. Du er fra Museby.
"""