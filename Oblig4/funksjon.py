"""
Oppgave 1: Parametere og returverdier
"""

#1)
def adder(tall1, tall2):  # Definerer adder funksjonen
    return tall1 + tall2  # Returnerer parameterne summet sammen

a = adder(1,1)  # Kaller på funksjonen med argumenter 1 og 1.
b = adder(2,2)  # Kaller på funksjonen med argumenter 2 og 2.

 # Printer en passende tekst
print("1 og 1 som argumenter i adder-funksjonen returnerer {}".format(a)) 
print("2 og 2 som argumenter i adder-funksjonen returnerer {}".format(b))

"""
Kjøreeksempel:
1 og 1 som argument i adder-funksjonen returnerer 2
2 og 2 som argument i adder-funksjonen returnerer 4
"""
"""
#2)
streng = input("Skriv inn en tekststreng: ")  # Ber brukeren skrive en streng
bokstav = input("Skriv inn en bokstav: ")  # Ber brukeren skrive inn en bokstav
# Printer hvor mange ganger den oppgitte bokstaven forekommer i strengen
print("Bokstaven {} forekommer {} ganger i {}.".format(\
bokstav,streng.count(bokstav) , streng))


Kjøreeksempel:
Skriv inn en tekststreng: tekst
Skriv inn en bokstav: t
Bokstaven t forekommer 2 ganger i tekst.
"""
#3)
def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)

streng = input("Skriv inn en tekststreng: ")  # Ber brukeren skrive en streng
bokstav = input("Skriv inn en bokstav: ")  # Ber brukeren skrive inn en bokstav
cnt = tellForekomst(streng, bokstav)  # Kaller tellForekomst funksjon, med streng og bokstav 
# som argumenter.
# Printer hvor mange ganger den oppgitte bokstaven forekommer i strengen
print("Bokstaven {} forekommer {} ganger i {}.".format(\
bokstav,cnt, streng)) 
"""
Kjøreeksempel:
Skriv inn en tekststreng: Tekst
Skriv inn en bokstav: k
Bokstaven k forekommer 1 ganger i Tekst.
"""
